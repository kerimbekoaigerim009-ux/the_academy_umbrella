from django.db import models

class Character(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to = 'images/')
    description = models.TextField()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


