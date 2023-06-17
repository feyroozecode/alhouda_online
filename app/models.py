from django.db import models

class Scholar(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='scholars/images/', blank=True, null=True)
    courses = models.ManyToManyField('Course', related_name='scholars_courses', blank=True)
    
    def __str__(self):
        return self.name
    
class Course(models.Model):
    scholar = models.ForeignKey(
        Scholar, on_delete=models.CASCADE, related_name='courses_of_scholar',
       
    )
    title = models.CharField(max_length=255)
    description = models.TextField()

    # Course materials
    audio_files = models.ManyToManyField('Audio', blank=True)
    video_files = models.ManyToManyField('Video', blank=True)
    pdf_files = models.ManyToManyField('PDF', blank=True)
    text_content = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

# Media
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

# publication
class Publication(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_of_pub = models.DateField()
    media = models.ForeignKey('Media', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
