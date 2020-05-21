from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    # We are using one-to-one relation because we want to take 
    # those data from the user which are not present in the basic 
    # admin pannel.
    # This will create basic template to register which have 
    # username, name, password etc... that all you can see when you 
    # go to basic admin pannel or when you create superuser
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Additional information
    profile_pic = models.ImageField(blank=True, 
                                    upload_to='profile_pic')

    def __str__(self):
        # when we print this class we will get the string which 
        # will be the username of user. 
        # All the methods of User class is given here:-
        # https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#django.contrib.auth.models.User
        return self.user.username
