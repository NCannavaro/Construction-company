from django.contrib.auth import get_user_model
from django.test import TestCase

from task_manager.models import Project, TypeOfWork, Position, Task


class ModelsTests(TestCase):
    def test_project_str(self):
        project = Project.objects.create(
            name="Test",
            registration_number="1",
            address="Test"
        )
        self.assertEqual(
            str(project), f"{project.name}"
        )

    def test_typeofwork_str(self):
        type_of_work = TypeOfWork.objects.create(
            name="Test",
        )
        self.assertEqual(
            str(type_of_work), f"{type_of_work.name}"
        )

    def test_position_str(self):
        position = Position.objects.create(
            name="Test",
        )
        self.assertEqual(
            str(position), f"{position.name}"
        )

    def test_employee_full_name_str(self):
        position = Position.objects.create(name="Test")
        employee = get_user_model().objects.create(
            username="Test",
            email="test@test.com",
            first_name="Jon",
            last_name="Wick",
            phone_number="+380677999213",
            position=position,
        )
        self.assertEqual(
            employee.full_name, "Jon Wick"
        )

    def test_task_str(self):
        project = Project.objects.create(
            name="Test",
            registration_number="1",
            address="Test"
        )
        type_of_work = TypeOfWork.objects.create(
            name="Test",
        )
        task = Task.objects.create(
            project=project,
            type_of_work=type_of_work,
            price=5,
        )

        self.assertEqual(
            str(task), f"Project: {task.project}, {task.type_of_work}"
        )
