from django.contrib import admin

from gallery.models import Photo, Comment

# Register your models here.
admin.site.register(Photo)
admin.site.register(Comment)