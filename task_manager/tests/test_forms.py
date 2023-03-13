from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from task_manager.forms import EmployeeCreationForm
from task_manager.models import Position


class FormsTests(TestCase):
    def test_employee_creating_form(self):
        position = Position.objects.create(name="Test")
        form_data = {
            "username": "new_user",
            "password1": "test123456789",
            "password2": "test123456789",
            "email": "test@test.com",
            "first_name": "first",
            "last_name": "last",
            "position": position
        }

        form = EmployeeCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)


class PrivateDriverTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="admin",
            password="admin123",
            first_name="first1",
            last_name="last1",
            email="admin@admin.com",
        )
        self.client.force_login(self.user)

    def test_update_employee(self):
        form_data = {
            "email": "admin@ad.com",
            "first_name": "first2",
            "last_name": "last2",
            "phone_number": "+380677999213"
        }
        self.client.post(reverse("task_manager:employee-update", args=(self.user.id,)), data=form_data)
        updated_user = get_user_model().objects.get(username="admin")

        self.assertEqual(updated_user.email, form_data["email"])
        self.assertEqual(updated_user.first_name, form_data["first_name"])
        self.assertEqual(updated_user.last_name, form_data["last_name"])
        self.assertEqual(updated_user.phone_number, form_data["phone_number"])

    def test_update_employees_phone_number(self):
        form_data = {
            "email": "admin@ad.com",
            "first_name": "first2",
            "last_name": "last2",
            "phone_number": "+3806779992"
        }

        self.client.post(reverse("task_manager:employee-update", args=(self.user.id,)), data=form_data)
        updated_user = get_user_model().objects.get(username="admin")

        self.assertNotEqual(updated_user.phone_number, form_data["phone_number"])
