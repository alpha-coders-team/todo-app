# Generated by Django 2.2 on 2021-04-07 13:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_task_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(1970, 1, 1, 0, 0), help_text='Срок выполнения задачи', verbose_name='Дедлайн'),
        ),
    ]
