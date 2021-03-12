from django.contrib.auth import get_user_model
from django.db import models

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
    finish_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата',
        help_text='Дата и время выполнения задачи',
    )

    class Meta:
        ordering = ('finish_date',)

    def __str__(self):
        return self.title
