from django.contrib import admin
from .models import Author,Reader,Editor
from admin import custom_admin_site

# Register your models here.
@admin.register(Author,Reader,Editor,site=custom_admin_site)
class PersonAdmin(admin.ModelAdmin):
    pass

