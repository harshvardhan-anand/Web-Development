from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from .receivers import create_profile

User = get_user_model()

post_save.connect(receiver=create_profile, sender=User)