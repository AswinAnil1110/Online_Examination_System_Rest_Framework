from django.db import models

# Create your models here.
class QuestionDb(models.Model):
    question = models.CharField(max_length=100)
    option_a = models.CharField(max_length=100)
    option_b = models.CharField(max_length=100)
    option_c = models.CharField(max_length=100)
    option_d = models.CharField(max_length=100)
    correct_answer = models.CharField(max_length=100)
    
class SubmissionDb(models.Model):
    student_name = models.CharField(max_length=100)
    question_id = models.IntegerField()
    answer = models.CharField(max_length=2)
    status = models.CharField(max_length=10,default='pending')
