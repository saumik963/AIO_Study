from django.contrib import admin
from .models import Notes


@admin.register(Notes)
class NotesAdmin(admin.ModelAdmin):
    list_display = ['user', 'Title',
                    'Description', 'is_completed', 'time']
    fields = ['user', 'Title', 'Description',
              'is_completed', 'time']
    readonly_fields = ['time']
