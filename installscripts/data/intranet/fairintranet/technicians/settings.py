from __future__ import unicode_literals
from __future__ import absolute_import

from django.conf import settings
from django.utils.translation import ugettext_lazy

LABEL_VALIDATION = getattr(
    settings,
    'TECHNICIANS_LABEL_VALIDATION',
    r'[A-Z]'
)

LABEL_VALIDATION_HELP = getattr(
    settings,
    'TECHNICIANS_LABEL_VALIDATION_HELP',
    ugettext_lazy("Please input a label with type X1234567, i.e. 'C0012345'")
)
