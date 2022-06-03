from django.contrib import admin

#local moduls
from main_app.models import Item

# register your models here.
admin.site.register(Item)