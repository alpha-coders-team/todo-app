from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Task(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    url = models.SlugField(unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='posts', verbose_name='автор')
    text = models.TextField('Текст задачи')
