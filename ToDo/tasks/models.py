import datetime

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

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
        models.SET_NULL,
        null=True,
        blank=True,
        related_name='tasks',
        verbose_name='Категория',
        help_text='Укажите категорию',
    )

    class Meta:
        ordering = ('deadline', 'priority', 'category')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'view-task',
            kwargs={'owner': self.owner.username, 'pk': self.id}
        )


class Comment(models.Model):
    task = models.ForeignKey(
        Task, on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='пост'
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='автор'
    )
    text = models.TextField(
        'Текст комментария',
        help_text='Здесь текст комментария'
    )
    created = models.DateTimeField(
        'Дата создания',
        auto_now_add=True
    )

    def __str__(self):
        return f'{self.task} - {self.text}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
