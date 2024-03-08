from django.contrib import admin
from .models import Author,Reader,Editor


# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    
    list_display=["name","title","view_birth_date"]

    @admin.display(empty_value='???')
    def view_birth_date(self,obj):
        return obj.birth_date

admin.site.register(Author,AuthorAdmin)