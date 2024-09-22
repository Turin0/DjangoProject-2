from django.contrib import admin
from task1.models import *
# Register your models here.

admin.site.register(Game)


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance', 'age')
