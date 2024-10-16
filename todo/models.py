from django.db import models

# Create your models here.


#Model for todo app 


class Task(models.Model):
    title = models.CharField(max_length=200)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=False)
    completed=models.BooleanField(default=False)

    def __str__(self):
        return self.title
