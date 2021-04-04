from django.contrib import admin

from .views import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'title', 'deadline', 'priority')
    search_fields = ('owner', 'title')
    list_editable = ('priority', )
    empty_value_display = '-пусто-'


admin.site.register(Task, TaskAdmin)