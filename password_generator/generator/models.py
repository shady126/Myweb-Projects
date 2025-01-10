from django.db import models

# Create your models here.
class GeneratedPassword(models.Model):
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.password