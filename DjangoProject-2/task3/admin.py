from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Post)
class PanelAdmin(admin.ModelAdmin):
    list_display = ('title', 'post', 'data')
    search_fields = ('title',)
    list_filter = ('title', 'data')
