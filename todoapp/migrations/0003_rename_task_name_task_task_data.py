# Generated by Django 4.1.2 on 2022-10-20 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_rename_data_task_rename_name_task_task_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='task_name',
            new_name='task_data',
        ),
    ]