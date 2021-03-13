from django.db import models
from django.conf import settings
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=500)
    subtitle = models.CharField(max_length=500, blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='books', on_delete=models.CASCADE)
    isbn = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.title} by {self.author}"