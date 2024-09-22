from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'post', 'date')
    search_fields = ('title',)
    list_filter = ('title', 'date')
