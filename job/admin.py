from django.contrib import admin

# Register your models here.

from .models import Job , Category,job_applies
admin.site.register(Job)
admin.site.register(Category)
admin.site.register(job_applies)