from django.db import models

class Publication(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_of_pub = models.DateField()
    media = models.ForeignKey('Media', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
