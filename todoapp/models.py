from django.db import models

# Create your models here.
class ToDoList(models.Model):
    task=models.TextField()
    category=models.CharField(max_length=20,default="default")
    date=models.DateField(null=True,blank=True)
    time=models.TimeField(null=True,blank=True)


    def __str__(self):
        return self.category
