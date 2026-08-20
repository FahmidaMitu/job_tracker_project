from django.contrib import admin
from .models import JobApplication, Category, Interview

admin.site.register(Category)
admin.site.register(JobApplication)
admin.site.register(Interview)