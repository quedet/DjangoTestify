from django.db import models


# Create your models here.
class Todo(models.Model):
    content = models.CharField(max_length=200, unique=True)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created'])
        ]