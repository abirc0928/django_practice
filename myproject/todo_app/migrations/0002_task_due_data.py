# Generated by Django 5.1 on 2024-08-25 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='due_data',
            field=models.DateField(blank=True, null=True),
        ),
    ]
