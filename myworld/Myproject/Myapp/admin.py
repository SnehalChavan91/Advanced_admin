from django.contrib import admin
from .models import Author,Reader,Editor


# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    
    actions_on_top=False
    actions_on_bottom=True
    date_hierarchy = "pub_date"
    
admin.site.register(Author,AuthorAdmin)