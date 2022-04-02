from statistics import mode
from django.db import models
class Cores(models.Model):
    cours_name=models.CharField(max_length=200,default="python")
    def __str__(self) -> str:
        return self.cours_name
class Question(models.Model):
    cours=models.ForeignKey(Cores,on_delete=models.CASCADE)
    queson=models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.queson
class Choose(models.Model):
    qution=models.ForeignKey(Question, on_delete=models.CASCADE)
    opetion1=models.CharField(max_length=200)
    opetion2=models.CharField(max_length=200)
    opetion3=models.CharField(max_length=200)
    opetion4=models.CharField(max_length=200)
    
class CorrectAns(models.Model):
    qution=models.ForeignKey(Question, on_delete=models.CASCADE)
    corectAnser=models.CharField(max_length=200)
    
