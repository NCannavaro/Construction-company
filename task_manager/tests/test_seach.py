from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from task_manager.models import Task, Project, TypeOfWork

TASK_URL = reverse("task_manager:task-list")
PROJECT_URL = reverse("task_manager:project-list")
EMPLOYEES_URL = reverse("task_manager:employee-list")


class ModelsTests(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            last_name="admin",
            password="admin12345"
        )
        self.client.force_login(self.admin_user)

        self.user = get_user_model().objects.create_user(
            username="Taras",
            password="Shevchenko123456",
            last_name="Shevchenko",
        )

        project1 = Project.objects.create(
            name="House",
            registration_number="1",
            address="address1"
        )
        project2 = Project.objects.create(
            name="Hotel",
            registration_number="2",
            address="address2"
        )
        type_of_work = TypeOfWork.objects.create(name="Test")
        Task.objects.create(
            project=project1,
            type_of_work=type_of_work,
            price=5,
        )
        Task.objects.create(
            project=project2,
            type_of_work=type_of_work,
            price=12,
        )

    def test_project_search_by_name(self):
        response = self.client.get(PROJECT_URL, data={"name": "t"})
        queryset = Project.objects.filter(name__icontains="t")

        self.assertEqual(response.context["project_list"][0], queryset[0])

    def test_task_search_by_project(self):

        response = self.client.get(TASK_URL, data={"project": "house"})
        queryset = Task.objects.filter(project__name__icontains="house")

        self.assertEqual(response.context["task_list"][0], queryset[0])

    def test_employee_search_by_last_name(self):

        response = self.client.get(EMPLOYEES_URL, data={"last_name": "shev"})
        queryset = get_user_model().objects.filter(last_name__icontains="shev")

        self.assertEqual(
            response.context["employee_list"][0].last_name, queryset[0].last_name
        )
