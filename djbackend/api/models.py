from django.db import models

# Create your models here.

class TodoList (models.Model) :
    event = models.CharField(max_length = 100)
    dateAdded = models.DateTimeField("Date added ",default = None)
    due = models.DateTimeField("Due date to complete",default = None)






