from django.contrib import admin
from .models import Author,Reader,Editor
#from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage


# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    
    fields=["name","title"]

class AuthorAdmin(admin.ModelAdmin):
    exclude=["birth_date"]


class FlatPageAdmin(admin.ModelAdmin):
    fields=["url","title","content"]

    
admin.site.register(Author,AuthorAdmin)
