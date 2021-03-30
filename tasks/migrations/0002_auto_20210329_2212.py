# Generated by Django 2.2 on 2021-03-29 18:12

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ('deadline', 'priority')},
        ),
        migrations.RemoveField(
            model_name='task',
            name='finish_date',
        ),
        migrations.AddField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 29, 22, 12, 57, 336217), help_text='Срок выполнения задачи', verbose_name='Дедлайн'),
        ),
        migrations.AddField(
            model_name='task',
            name='priority',
            field=models.SmallIntegerField(default=10, help_text='Приоритет выполнения задачи', verbose_name='Приоритет'),
        ),
        migrations.AlterField(
            model_name='task',
            name='owner',
            field=models.ForeignKey(help_text='Укажите имя', on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to=settings.AUTH_USER_MODEL, verbose_name='Владелец задачи'),
        ),
    ]