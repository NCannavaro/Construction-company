from django.urls import path

from task_manager.views import index, ProjectListView, TaskListView, EmployeeListView

urlpatterns = [
    path("", index, name="index"),
    path("employees/", EmployeeListView.as_view(), name="employee-list"),
    path("projects/", ProjectListView.as_view(), name="project-list"),
    path("tasks/", TaskListView.as_view(), name="task-list"),

]

app_name = "task_manager"
