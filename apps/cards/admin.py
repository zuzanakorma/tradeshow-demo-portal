from django.contrib import admin
from .models import Card, Tag

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_filter = ("title", "tags")
    list_display = ("title", "tags")

admin.site.register(Card)
admin.site.register(Tag)
