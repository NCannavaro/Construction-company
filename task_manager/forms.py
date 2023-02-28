from django.contrib.auth.forms import UserCreationForm

from task_manager.models import Employee


class EmployeeCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Employee
        fields = UserCreationForm.Meta.fields + (
            "email",
            "first_name",
            "last_name",
            "position"
        )
