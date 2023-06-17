from django.db import models
from .scholar import Scholar

class Course(models.Model):
    scholar = models.ForeignKey(Scholar, on_delete=models.CASCADE, related_name='courses')
    title = models.CharField(max_length=255)
    description = models.TextField()

    # Course materials
    audio_files = models.ManyToManyField('Audio', blank=True)
    video_files = models.ManyToManyField('Video', blank=True)
    pdf_files = models.ManyToManyField('PDF', blank=True)
    text_content = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title