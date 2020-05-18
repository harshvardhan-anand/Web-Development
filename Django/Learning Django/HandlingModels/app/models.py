from django.db import models

# Create your models here.
class PersonDetails(models.Model):
    user_id = models.CharField(unique=True, primary_key=True, max_length=50)
    name_of_person = models.TextField()
    phone_no = models.IntegerField()

class Article(models.Model):
    foreign_key = models.ForeignKey(PersonDetails, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()


