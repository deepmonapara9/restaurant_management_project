from django.contrib import admin
from .models import *


# Custom Admins
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name','price','available')
    list_filter = ('available')
    search_fields = ('name', 'description')



# Register your models here.
admin.site.register(Item,ItemAdmin)