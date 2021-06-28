from django.db import models
from User.models import User
from datetime import datetime

class StudentQuestion(models.Model):
    ques = models.CharField(max_length=1000, null=False, blank=False)
    quesDate = models.DateField(default=datetime.now())
    student = models.ForeignKey(to=User, on_delete=models.CASCADE)
    activeStatus = models.BooleanField(default=True)

class Answers(models.Model):
    ans = models.CharField(max_length=5000, null=False, blank=False)
    ansDate = models.DateField(default=datetime.now())
    question = models.ForeignKey(to=StudentQuestion, on_delete=models.CASCADE)
    faculty = models.ForeignKey(to=User, on_delete=models.CASCADE)