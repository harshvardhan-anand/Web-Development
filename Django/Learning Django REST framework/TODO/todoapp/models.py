from django.db import models

# Create your models here.
class Student(models.Model):
    roll = models.IntegerField(unique=True, blank=False)
    city = models.CharField(max_length=10, default='')
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class School(models.Model):
    fkey = models.ForeignKey(Student, on_delete=models.CASCADE)
    school = models.CharField(max_length=100, null=True)
