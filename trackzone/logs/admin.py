from django.contrib import admin
from .models import LogEntry

# admin.site.register(LogEntry)
@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'weight', 'note', 'date')

# Register your models here.
