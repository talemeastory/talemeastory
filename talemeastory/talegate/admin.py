from django.contrib import admin
from .models import StoryBook, Story, Excerpt


# Register your models here.
@admin.register(StoryBook)
class StoryBookAdmin(admin.ModelAdmin):
    pass


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Excerpt)
class ExcerptAdmin(admin.ModelAdmin):
    pass
