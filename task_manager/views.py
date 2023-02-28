from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

from task_manager.forms import EmployeeCreationForm
from task_manager.models import Employee, Project, Task


@login_required
def index(request):
    """View function for the home page of the site."""

    num_employees = Employee.objects.count()
    num_projects = Project.objects.count()
    num_tasks = Task.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_employees": num_employees,
        "num_projects": num_projects,
        "num_tasks": num_tasks,
        "num_visits": num_visits + 1,
    }

    return render(request, "task_manager/index.html", context=context)


class EmployeeListView(generic.ListView):
    model = Employee
    template_name = "task_manager/employee_list.html"


class EmployeeDetailView(LoginRequiredMixin, generic.DetailView):
    model = Employee
    # queryset = Employee.objects.all().prefetch_related("tasks__project")


class EmployeeCreationView(LoginRequiredMixin, generic.CreateView):
    model = Employee
    form_class = EmployeeCreationForm


class ProjectListView(generic.ListView):
    model = Project
    template_name = "task_manager/project_list.html"


class ProjectDetailView(LoginRequiredMixin, generic.DetailView):
    model = Project


class TaskListView(generic.ListView):
    model = Task
    template_name = "task_manager/task_list.html"


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task
