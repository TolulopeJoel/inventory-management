from django.contrib.auth import get_user_model
from django.db import models


class Employee(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.user.username
