from django.test import TestCase
from tasks.models import Task
from django.contrib.auth import get_user_model

User = get_user_model()


class TaskModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        owner = User.objects.create()
        Task.objects.create(title="Important task",
                            owner=owner, priority=5)

    def test_title_label(self):
        task = Task.objects.get(id=1)
        field_label = task._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'Задача')
