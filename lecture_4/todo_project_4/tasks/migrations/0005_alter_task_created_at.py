# Generated by Django 4.2.6 on 2023-10-18 06:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_alter_task_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 18, 6, 43, 7, 203890, tzinfo=datetime.timezone.utc)),
        ),
    ]
