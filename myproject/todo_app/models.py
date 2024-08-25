from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    due_data = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.title