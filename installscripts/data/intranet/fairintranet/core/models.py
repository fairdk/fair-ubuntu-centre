from __future__ import unicode_literals
from __future__ import absolute_import

from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel


COMMON_CONTENT_PANELS = [
    FieldPanel('title', classname="full title"),
    FieldPanel('body', classname="full"),
    ImageChooserPanel('cover_image'),
    FieldPanel('slug'),
    FieldPanel('show_in_menus',),
]

RESOURCE_PANELS = [
    ImageChooserPanel('thumbnail'),
    FieldPanel('resource_link'),
    FieldPanel('author'),
    FieldPanel('year'),
    FieldPanel('country'),
    FieldPanel('short_description'),
]


class HomePage(Page):
    body = RichTextField(null=True, blank=True, verbose_name=_("Body / main text on page"),)
    cover_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    
    def child_collections(self):
        return Collection.objects.descendant_of(self)
    
    class Meta:
        verbose_name = _("Standard article")
        verbose_name = _("Standard articles")


HomePage.content_panels = COMMON_CONTENT_PANELS

HomePage.promote_panels = [
    FieldPanel('seo_title',),
    FieldPanel('search_description',),
]


class Resource(models.Model):
    
    short_description = models.CharField(
        max_length=512,
        null=True,
        blank=True,
    )
    # This is not a URLField, because it doesn't validate non-domain
    # http://server/path/
    resource_link = models.CharField(
        verbose_name=_("resource link"),
        help_text=_("Find a book or movie file available on the intranet and copy the link here, e.g. http://localserver/path/to/book.pdf",),
        max_length=512,
    )
    thumbnail = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    year = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name=_("year of publication"))
    author = models.CharField(max_length=64, null=True, blank=True, verbose_name=_("author / director"))
    country = models.CharField(max_length=64, null=True, blank=True, verbose_name=_("country of origin"))

    class Meta:
        abstract = True


class EBook(HomePage, Resource):
    pass

EBook.content_panels = COMMON_CONTENT_PANELS + RESOURCE_PANELS


class Movie(HomePage, Resource):
    duration = models.CharField(max_length=64, null=True, blank=True)

Movie.content_panels = COMMON_CONTENT_PANELS + RESOURCE_PANELS + [FieldPanel('duration')]


class Collection(HomePage):
    
    icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name=_("icon"),
        help_text=_("Cheerful icon to display on buttons next to the title"),
    )
    icon_predefined = models.CharField(
        max_length=64,
        default="folder-open",
        verbose_name=_("default icon"),
        choices=[
            (x, x) for x in [
                'folder-open',
                'video-camera',
                'truck',
                'rocket',
                'road',
                'question',
                'graduation-cap',
            ]
        ]
    )
    license = models.CharField(max_length=64, null=True, blank=True, verbose_name=_("license"))
    button_caption = models.CharField(max_length=64, null=True, blank=True, verbose_name=_("button caption"))
    
    def get_movies(self):
        return Movie.objects.descendant_of(self)

    def get_ebooks(self):
        return EBook.objects.descendant_of(self)


Collection.content_panels = COMMON_CONTENT_PANELS + [
    ImageChooserPanel('icon'),
    FieldPanel('icon_predefined'),
    FieldPanel('license'),
    FieldPanel('button_caption'),
]


class ExternalCollection(Collection):
    retrieved = models.DateField(null=True, blank=True, verbose_name=_("Retrieval date"), help_text=_("When this collection was copied from the internet"))

ExternalCollection.content_panels = Collection.content_panels + [
    FieldPanel('retrieved'),
]


class ResourceUsage(models.Model):
    
    ebook = models.ForeignKey('EBook', null=True, blank=True)
    movie = models.ForeignKey('Movie', null=True, blank=True)
    external_collection = models.ForeignKey('ExternalCollection', null=True, blank=True)
    clicks = models.PositiveIntegerField(default=0)
    from_date = models.DateField()
    to_date = models.DateField()
    
    class Meta:
        verbose_name = _("resource usage")
        verbose_name_plural = _("resource usages")
        ordering = ('from_date', 'to_date')
    
    @classmethod
    def count_click(cls, **kwargs):
        """"""
        if 'movie' not in kwargs and 'ebook' not in kwargs and 'external_collection' not in kwargs:
            raise RuntimeError("You must specify either movie or ebook or external_collection")
        from_date = timezone.now().replace(day=1).date()
        if from_date.month < 12:
            to_date = from_date.replace(month=from_date.month + 1)
        else:
            to_date = from_date.replace(month=1, year=from_date.year + 1)
        kwargs['from_date'] = from_date
        kwargs['to_date'] = to_date
        usage, _ = cls.objects.get_or_create(**kwargs)
        usage.clicks += 1
        usage.save()
        return usage