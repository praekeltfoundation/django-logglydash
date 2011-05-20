from logglydash import loggly

from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import Message
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save)
def post_save_callback(sender, instance, created, **kwargs):
    if instance.__class__ not in [LogEntry, Message]:
        if created:
            logger = loggly.getLogger()
            logger.info('action=create,object=%s.%s,id=%s' % (instance.__module__, instance.__class__.__name__, instance.pk))
