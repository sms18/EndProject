from django.db import models

# Create your models here.
class categories(models.Model):
     categoryName=models.CharField(max_length=50)
     
class courses(models.Model):
    coursesName=models.CharField(max_length=50)
    Description=models.CharField(max_length=50)
    image=models.CharField(max_length=100)
    is_puplish=models.BooleanField()
    cateoryID=models.ForeignKey(categories,on_delete=models.CASCADE)
    
class booking(models.Model):
    fristname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email=models.EmailField(max_length=250)
    phone=models.IntegerField()
    age=models.IntegerField()
    coursesID=models.ForeignKey(courses,on_delete=models.CASCADE)
    
    