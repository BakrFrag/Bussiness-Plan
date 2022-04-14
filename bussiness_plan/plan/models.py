from django.db import models

from django.contrib.auth.models import User;

class Section(models.Model):
    name=models.CharField(max_length=256,unique=True)

class Question(models.Model):
    section = models.ForeignKey(Section , on_delete=models.CASCADE)
    question=models.CharField(max_length=256)
    def __str__(self):
        return self.question

class Answer(models.Model):
    answer= models.CharField(max_length=256)
    def __str__(self):
        return self.answer

class BussinessPlan(models.Model):
    answer=models.ForeignKey(Answer,on_delete=models.CASCADE)
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)


