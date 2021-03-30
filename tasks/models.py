import datetime

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

User = get_user_model()


class Task(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tasks',
        verbose_name='Владелец задачи',
        help_text='Укажите имя',
    )
    title = models.CharField(
        max_length=280,
        verbose_name='Задача',
        help_text='Быстрое добавление задачи',
    )
    deadline = models.DateTimeField(
        default=datetime.datetime.now(),
        verbose_name='Дедлайн',
        help_text='Срок выполнения задачи',
    )
    priority = models.SmallIntegerField(
        default=10,
        verbose_name='Приоритет',
        help_text='Приоритет выполнения задачи',
    )

    class Meta:
        ordering = ('deadline', 'priority',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'view-task',
            kwargs={'owner': self.owner.username, 'pk': self.id}
        )
