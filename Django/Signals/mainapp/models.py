from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(blank=True, max_length=50)
    date_of_birth = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.user.username
