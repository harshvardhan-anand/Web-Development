from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import Image

@receiver(m2m_changed, sender=Image.user_like.through)
def update_user_like_count(sender, instance, **kwargs):
    instance.user_like_count = instance.user_like.count()
    instance.save()