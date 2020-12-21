from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
# Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self):
        # https://stackoverflow.com/questions/8972866/correct-way-to-use-super-argument-passing
        return super(PublishedManager, self).get_queryset().filter(status='published')

class Post(models.Model):
    STATUS_CHOICE = (
        ('draft', 'DRAFT'),
        ('published', 'PUBLISHED')
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique_for_date='publish')
    # creating many to one field, many posts can be written by single user
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICE)
    objects = models.Manager()
    published = PublishedManager()
    tags = TaggableManager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse(
            'blog:post_detail',
            args=[
                self.publish.year,
                self.publish.month,
                self.publish.day,
                self.slug
            ]
        )

class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    comment = models.TextField()
    name = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f"Commented on {self.post} by {self.name}"

