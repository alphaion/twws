from enum import unique
from django.db import models
import calendar
# Create your models here.

class BookModel(models.Model):
    title=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    cover=models.ImageField(upload_to="Book_Cover", height_field=None, width_field=None, max_length=None)
    currently_reading=models.BooleanField(default=False)

    def __str__(self):
        return self.title


class BookOfMonth(models.Model):

    MONTH_CHOICES = [(str(i), calendar.month_name[i]) for i in range(1,13)] 
    book=models.ForeignKey(BookModel,on_delete=models.CASCADE)
    month = models.CharField(max_length=9, choices=MONTH_CHOICES, unique=True)

    def __str__(self):
        return self.month
            
class Review(models.Model):
    pass
    
