from django import forms
from django.contrib import admin
from .models import Author,Reader,Editor,Person
#from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage


# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    
    fields=["name","title"]

class AuthorAdmin(admin.ModelAdmin):
    exclude=["birth_date"]


class FlatPageAdmin(admin.ModelAdmin):
    fieldsets=[(None,{"fields":["url","title","content","sites"],},),("Advanced options",{
        "classes":["collapse"],
        "fields":["registration_required","template_name"],
    },),]


class PersonForm(forms.ModelForm):
    class Meta:
        model=Person
        exclude=["name"]

class PersonAdmin(admin.ModelAdmin):
    exclude=["age"]
    form=PersonForm

    
admin.site.register(Author,AuthorAdmin)
