from django.db import models
from django.contrib.auth.models import User

class Textbook(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    edition = models.CharField(max_length=50, blank=True, null=True)
    author = models.CharField(max_length=255)
    course_code = models.CharField(max_length=20)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} ({self.course_code})"

class UserProfile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.user.username
