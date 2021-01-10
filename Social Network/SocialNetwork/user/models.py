from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.conf import settings
from django.urls import reverse
from django.contrib.auth import get_user_model
# Create your models here.

def get_image_file_path(instance, filename):
    return f'{instance.user.id}/post/{filename}'

class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='images', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50)
    slug = models.SlugField(blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to=get_image_file_path)
    created = models.DateTimeField(auto_now_add=True)
    user_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='image_liked', blank=True)
    user_like_count = models.PositiveIntegerField(default=0, db_index=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("user:detail_dash", kwargs={
            "user_id": self.user.id,
            'post_id':self.id
        })

class Contact(models.Model):
    user_from = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='followed_by', on_delete=models.CASCADE)
    user_to = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='followed_to', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created_on',)

    def __str__(self):
        return f'{self.user_from} follows {self.user_to}'

user = get_user_model()
user.add_to_class('following', models.ManyToManyField(
    'self', related_name='follower', through=Contact, symmetrical=False))