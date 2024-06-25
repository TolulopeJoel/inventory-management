# Generated by Django 5.0.6 on 2024-06-25 07:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="employee",
            name="employee_id",
        ),
        migrations.AddField(
            model_name="employee",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default="2024-06-25 07:13:38.000840+00:00"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="employee",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
