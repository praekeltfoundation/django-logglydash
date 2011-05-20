from django.db import models
from django.utils.translation import ugettext as _

class Metric(models.Model):
    """Tracked Metric"""
    title = models.CharField(
        max_length=100,
        help_text=_("A short, descriptive title for this metric"),
    )
    query = models.CharField(
        max_length=512,
        help_text=_("Loggly search query."),
    )
