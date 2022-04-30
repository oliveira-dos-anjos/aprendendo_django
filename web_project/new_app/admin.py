from django.contrib import admin
from .models import post


@admin.register(post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", 'slug', 'author', 'created', 'updated')
    prepopulated_fields = {'slug':("title",)}

