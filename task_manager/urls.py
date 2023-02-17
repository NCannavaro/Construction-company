from django.urls import path

from task_manager.views import index, ProjectListView, TaskListView

urlpatterns = [
    path("", index, name="index"),
    path("projects/", ProjectListView.as_view(), name="projects-list"),
    path("task/", TaskListView.as_view(), name="task-list"),

]

app_name = "task_manager"
