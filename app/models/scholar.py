from django.db import models

class Scholar(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='scholars/images/', blank=True, null=True)

    def __str__(self):
        return self.name