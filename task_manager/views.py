from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic

from task_manager.forms import (
    EmployeeCreationForm,
    EmployeeUpdateForm,
    ProjectsSearchForm,
    TaskForm,
    ProjectsCreateForm,
    EmployeesSearchForm, TaskSearchForm
)
from task_manager.models import Employee, Project, Task


@login_required
def index(request):
    """View function for the home page of the site."""

    num_employees = Employee.objects.count()
    num_projects = Project.objects.count()
    num_tasks = Task.objects.count()
    tasks = Employee.objects.aggregate(
        finished_tasks=Sum("number_of_completed_tasks")
    )

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_employees": num_employees,
        "num_projects": num_projects,
        "num_tasks": num_tasks,
        "tasks": tasks["finished_tasks"],
        "num_visits": num_visits + 1,
    }

    return render(request, "task_manager/index.html", context=context)


class EmployeeListView(LoginRequiredMixin, generic.ListView):
    model = Employee
    template_name = "task_manager/employee_list.html"
    paginate_by = 5
    queryset = Employee.objects.prefetch_related(
        "tasks__project"
    ).select_related("position")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(EmployeeListView, self).get_context_data(**kwargs)

        last_name = self.request.GET.get("last_name", "")
        context["search_form"] = EmployeesSearchForm(
            initial={
                "last_name": last_name
            }
        )
        return context

    def get_queryset(self):
        queryset = Employee.objects.all()

        form = EmployeesSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                last_name__icontains=form.cleaned_data["last_name"]
            )
        return queryset


class EmployeeDetailView(LoginRequiredMixin, generic.DetailView):
    model = Employee
    queryset = Employee.objects.prefetch_related(
        "tasks__project"
    ).select_related("position")


class EmployeeCreationView(LoginRequiredMixin, generic.CreateView):
    model = Employee
    form_class = EmployeeCreationForm


class EmployeeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Employee
    form_class = EmployeeUpdateForm

    def get_success_url(self):
        return reverse("task_manager:employee-detail", args=(self.object.id,))


class EmployeeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Employee
    success_url = reverse_lazy("task_manager:employee-list")


class ProjectListView(LoginRequiredMixin, generic.ListView):
    model = Project
    template_name = "task_manager/project_list.html"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProjectListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")
        context["search_form"] = ProjectsSearchForm(
            initial={
                "name": name
            }
        )
        return context

    def get_queryset(self):
        queryset = Project.objects.all()

        form = ProjectsSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )
        return queryset


class ProjectDetailView(LoginRequiredMixin, generic.DetailView):
    model = Project


class ProjectCreateView(LoginRequiredMixin, generic.CreateView):
    model = Project
    form_class = ProjectsCreateForm

    def get_success_url(self):
        return reverse("task_manager:project-detail", args=(self.object.id,))


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = "task_manager/task_list.html"
    paginate_by = 5
    queryset = Task.objects.select_related(
        "project", "type_of_work"
    ).prefetch_related("employees__position",)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)

        project = self.request.GET.get("project", "")
        context["search_form"] = TaskSearchForm(
            initial={
                "project": project
            }
        )
        return context

    def get_queryset(self):
        queryset = Task.objects.all()

        form = TaskSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                project__name__icontains=form.cleaned_data["project"]
            )
        return queryset


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task_manager:task-list")


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task_manager:task-list")


@login_required
def toggle_assign_to_task(request, pk):
    employee = Employee.objects.get(id=request.user.id)
    if (
        Task.objects.get(id=pk) in employee.tasks.all()
    ):  # probably could check if car exists
        employee.tasks.remove(pk)
    else:
        employee.tasks.add(pk)
    return HttpResponseRedirect(
        reverse_lazy("task_manager:task-detail", args=[pk])
    )


@login_required
def closing_task(request, pk):
    task = Task.objects.get(id=pk)
    employee = Employee.objects.get(id=request.user.id)
    if task.is_completed is False:
        task.is_completed = True
        employee.number_of_completed_tasks += 1
        task.save()
        employee.save()
    return HttpResponseRedirect(
        reverse_lazy("task_manager:task-detail", args=[pk])
    )
