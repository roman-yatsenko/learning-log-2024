from django.db import models

# Create your models here.

class Topic(models.Model):
    """Тема, яку вивчає користувач"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """Повертає символьне подання моделі"""
        return self.text
        