from django.contrib import admin
from .models import *

# Register your models here.


# @admin.register(Story)
# class StoryAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in Story._meta.fields]


@admin.register(Excerpt)
class ExcerptAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Excerpt._meta.fields]
