from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Student(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    grade = models.CharField(max_length=3)
    photo = models.ImageField(upload_to='student_photos/',blank=True,null=True)

    def __self__(self):
        return f"{self.name} ({self.user.name})"