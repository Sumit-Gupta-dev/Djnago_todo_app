# Generated by Django 4.1.2 on 2022-10-27 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0003_rename_task_name_task_task_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]