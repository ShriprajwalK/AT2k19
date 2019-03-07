from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import NewsPost

admin.site.register(NewsPost)
