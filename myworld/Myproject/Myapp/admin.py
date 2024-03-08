from django.contrib import admin
from .models import Author,Reader,Editor


# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Author,AuthorAdmin)