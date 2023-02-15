from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from task_manager.models import Task, Project, TypeOfWork, Position, Employee

admin.site.register(Project)
admin.site.register(TypeOfWork)
admin.site.register(Position)
admin.site.register(Task)

admin.site.register(Employee, UserAdmin)
