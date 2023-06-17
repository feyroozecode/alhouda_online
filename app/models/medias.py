from django.db import models


class Media(models.Model):
    audio_file = models.FileField(upload_to='publications/media/audios/', blank=True, null=True)
    video_file = models.FileField(upload_to='publications/media/videos/', blank=True, null=True)
    pdf_file = models.FileField(upload_to='publications/media/pdfs/', blank=True, null=True)

    def __str__(self):
        return f"Media: {self.id}"
    
class Audio(models.Model):
    file = models.FileField(upload_to='courses/audios/')

    def __str__(self):
        return self.file.name

class Video(models.Model):
    file = models.FileField(upload_to='courses/videos/')

    def __str__(self):
        return self.file.name

class PDF(models.Model):
    file = models.FileField(upload_to='courses/pdfs/')

    def __str__(self):
        return self.file.name
