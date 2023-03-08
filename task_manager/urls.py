from django.urls import path

from task_manager.views import (
    index,
    ProjectListView,
    TaskListView,
    EmployeeListView,
    EmployeeDetailView,
    TaskDetailView,
    ProjectDetailView,
    EmployeeCreationView,
    EmployeeUpdateView,
    TaskCreateView,
    TaskUpdateView,
    EmployeeDeleteView,
    toggle_assign_to_task, ProjectCreateView,
)

urlpatterns = [
    path("", index, name="index"),
    path("employees/", EmployeeListView.as_view(), name="employee-list"),
    path("employees/<int:pk>/",
         EmployeeDetailView.as_view(),
         name="employee-detail"
         ),
    path("employees/create/",
         EmployeeCreationView.as_view(),
         name="employee-create"
         ),
    path("employees/update/<int:pk>/",
         EmployeeUpdateView.as_view(),
         name="employee-update"
         ),
    path("employees/delete/<int:pk>/",
         EmployeeDeleteView.as_view(), name="employee-delete"
         ),

    path("projects/", ProjectListView.as_view(), name="project-list"),
    path("projects/<int:pk>",
         ProjectDetailView.as_view(),
         name="project-detail"
         ),
    path("projects/create/",
         ProjectCreateView.as_view(),
         name="project-create"
         ),

    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/update/<int:pk>/",
         TaskUpdateView.as_view(),
         name="task-update"
         ),
    path(
        "tasks/<int:pk>/toggle-assign/",
        toggle_assign_to_task,
        name="toggle-tasks-assign",
    ),
]

app_name = "task_manager"
