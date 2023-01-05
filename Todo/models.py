from django.db import models

# Create your models here.
class ToDoList(models.Model):
    SLNo = models.AutoField(primary_key=True, auto_created=True)
    Title=models.CharField(max_length=200)
    Desc=models.CharField(max_length=500)
    
   
    


