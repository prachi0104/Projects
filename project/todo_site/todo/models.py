from django.db import models
from django.utils import timezone
# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    is_done=models.BooleanField(default=False)
 

    """ def __str__(self):
        return self.title """
    



