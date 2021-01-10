from django.db import models
from django.conf import settings

# Create your models here.

def get_custom_file_path(instance, filename):
    return f'{instance.user.id}/profilepic/{filename}'
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    dob = models.DateField(null=True)
    photo = models.ImageField(upload_to=get_custom_file_path, blank=True)

    def __str__(self):
        return f"{self.user.username}"