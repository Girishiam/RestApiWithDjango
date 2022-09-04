from django.db import models

# Create your models here.

class Movies(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Movies'
        verbose_name_plural = 'Movies'

    def __str__(self):
        return self.name