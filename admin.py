from django.contrib import admin

# Register your models here.
from analytics.models import Author


class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Author, AuthorAdmin)