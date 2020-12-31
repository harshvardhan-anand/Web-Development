from django.db import models
from django.conf import settings

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    dob = models.DateField(null=True)
    photo = models.ImageField(upload_to=f'profilepic/', blank=True)

    def __str__(self):
        return f"{self.user.username}"