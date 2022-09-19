from django.db import models

# Create your models here.


class UsersDetails(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    email = models.CharField(max_length=30,null=True)
    pass1 = models.CharField(max_length=30,null=True)
    pass2 = models.CharField(max_length=30,null=True)
    username = models.CharField(max_length=30,null=True)

class Polls(models.Model):
    email = models.CharField(max_length=30,null=True)
    question=models.CharField(max_length=30,null=True)
    opt1=models.CharField(max_length=30,null=True)
    opt2=models.CharField(max_length=30,null=True)
    opt3=models.CharField(max_length=30,null=True)
    opt4=models.CharField(max_length=30,null=True)
    created_on_date=models.DateTimeField(max_length=30,auto_now_add=True)
 
 
    
    

    
