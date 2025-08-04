from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'user', 'status', 'priority', 'start_date', 'due_date', 'created_at', 'updated_at']

admin.site.register(Task, TaskAdmin)
