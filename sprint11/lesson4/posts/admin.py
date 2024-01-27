from django.contrib import admin

from .models import Group, Post

# Register your models here.

admin.site.register(Post)
admin.site.register(Group)
