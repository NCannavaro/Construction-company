from django.contrib.auth.models import AbstractUser
from django.db import models


URGENCY_CHOICES = (
    (0, "minor"),
    (1, "medium",),
    (2, "major",),
    (3, "critical")
)


class Project(models.Model):
    name = models.CharField(max_length=255)
    registration_number = models.CharField(max_length=255)
    address = models.CharField(max_length=255)


class TypeOfWork(models.Model):
    name = models.CharField(max_length=255)


class Position(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


class Employee(AbstractUser):
    position = models.ForeignKey("Position", on_delete=models.CASCADE)
    number_of_completed_tasks = models.IntegerField()


class Task(models.Model):
    project = models.ForeignKey("Project", on_delete=models.CASCADE)
    type_of_work = models.ForeignKey("TypeOfWork", on_delete=models.CASCADE)
    description = models.TextField()
    urgency = models.IntegerField(max_length=1, choices=URGENCY_CHOICES, default=1)
    price = models.BooleanField()
    status = models.CharField(max_length=255)
    employees = models.ManyToManyField("Employee")
