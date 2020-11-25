from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager

# Create your models here.

# we pass the parameter in super function to skip the use of that class.
# It will tell python to look into MRO after the class given as argument in super().
class PublishedManager(models.Manager):
    def get_queryset(self):
        # print(self.__class__.mro())
        return super(PublishedManager, self).get_queryset().filter(status='published')
        
class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                                related_name='blog_post')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    objects = models.Manager() #default manager
    published = PublishedManager() #custom manager
    tags = TaggableManager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.publish.year, self.publish.month, 
                                                self.publish.day, self.slug])


class Comment(models.Model):
    email = models.EmailField()
    body = models.TextField()
    name = models.CharField(max_length=50)
    #------------------------------------#
    post = models.ForeignKey(Post, related_name='comment_related_to_post', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField()

    def __str__(self):
        return f"{self.body} by {self.name}"