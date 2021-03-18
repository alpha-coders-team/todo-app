from django.contrib.auth import get_user_model
from django.db import models
import datetime

User = get_user_model()


class Category(models.Model):
    title = models.CharField(
        max_length=200,
        unique=True,
        verbose_name='Категория',
        help_text='Категория задачи',
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='category',
        verbose_name='Владелец категории',
        help_text='Укажите категорию',
    )

    def __str__(self):
        return self.title


class Task(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tasks',
        verbose_name='Владелец задачи',
        help_text='Укажите имя владельца',
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
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='task_category',
        verbose_name='Категория',
        help_text='Укажите категорию',
    )

    class Meta:
        ordering = ('deadline', 'priority',)

    def __str__(self):
        return self.title
