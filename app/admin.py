from django.contrib import admin

from app.models import Course, Publication, Scholar

# Register your models here.
admin.site.register(Scholar)
admin.site.register(Course)
admin.site.register(Publication)
