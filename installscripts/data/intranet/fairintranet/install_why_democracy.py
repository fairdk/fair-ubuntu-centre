import os
from django.utils.text import slugify
from core import models

movies = open("why_democracy.lst").read().split("\n\n")

parent = models.Collection.objects.get(id=7)

for pos,m in enumerate(movies):
    data = m.split("\n")
    slug=slugify(unicode(data[0]))
    models.Movie.objects.create(
        numchild=0,
        depth=parent.depth+1,
        show_in_menus=True,
        path=parent.path + "{pos:s}".format(pos=str(pos+1).zfill(4)),
        url_path=os.path.join(parent.url_path, slug) + "/",
        slug=slug,
        title=data[0],
        live=True,
        short_description=data[3],
        author=data[2],
        duration=data[1],
        resource_link="http://fairserver/movies/why_democracy/.m3u",
     )

parent.numchild = len(movies)
parent.save()
