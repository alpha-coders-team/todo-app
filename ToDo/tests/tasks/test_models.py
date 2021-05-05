from django.test import TestCase
from tasks.models import Task, Category, Comment
from django.contrib.auth import get_user_model

User = get_user_model()


class TaskModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.owner = User.objects.create(username='testuser')
        cls.category = Category.objects.create(title='testcategory',
                                               owner=cls.owner)
        cls.task = Task.objects.create(
            title="Important task",
            owner=cls.owner,
            priority=5,
            category=cls.category)

    def test_task_title_label(self):
        task = TaskModelTest.task
        fields_verboses = {
            'owner': 'Владелец задачи',
            'title': 'Задача',
            'deadline': 'Дедлайн',
            'priority': 'Приоритет',
            'category': 'Категория',
        }
        for value, expected in fields_verboses.items():
            with self.subTest(value=value):
                self.assertEqual(
                    task._meta.get_field(value).verbose_name, expected)

    def test_task_help_text(self):
        task = TaskModelTest.task
        fields_help_texts = {
            'owner': 'Укажите имя владельца',
            'title': 'Быстрое добавление задачи',
            'deadline': 'Срок выполнения задачи',
            'priority': 'Приоритет выполнения задачи',
            'category': 'Укажите категорию',
        }
        for value, expected in fields_help_texts.items():
            with self.subTest(value=value):
                self.assertEqual(
                    task._meta.get_field(value).help_text, expected)

    def test_task_str(self):
        task = TaskModelTest.task
        self.assertEquals(str(task), task.title)


class CommentModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.author = User.objects.create(username='testuser')
        cls.task = Task.objects.create(title='testtitle',
                                       owner=cls.author)
        cls.comment = Comment.objects.create(
            task=cls.task,
            author=cls.author,
            text='testtext',
        )

    def test_comment_title_label(self):
        comment = CommentModelTest.comment
        fields_verboses = {
            'task': 'пост',
            'author': 'автор',
            'text': 'Текст комментария',
            'created': 'Дата создания',
        }
        for value, expected in fields_verboses.items():
            with self.subTest(value=value):
                self.assertEqual(
                    comment._meta.get_field(value).verbose_name, expected)

    def test_comment_help_text(self):
        comment = CommentModelTest.comment
        fields_help_texts = {
            'text': 'Здесь текст комментария',
        }
        for value, expected in fields_help_texts.items():
            with self.subTest(value=value):
                self.assertEqual(
                    comment._meta.get_field(value).help_text, expected)

    def test_comment_str(self):
        comment = CommentModelTest.comment
        self.assertEquals(str(comment), f'{comment.task} - {comment.text}')


class CategoryModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.owner = User.objects.create(username='testuser')
        cls.category = Category.objects.create(
            owner=cls.owner,
            title='testtitle',
        )

    def test_category_title_label(self):
        category = CategoryModelTest.category
        fields_verboses = {
            'title': 'Категория',
            'owner': 'Владелец категории',
        }
        for value, expected in fields_verboses.items():
            with self.subTest(value=value):
                self.assertEqual(
                    category._meta.get_field(value).verbose_name, expected)

    def test_category_help_text(self):
        category = CategoryModelTest.category
        fields_help_texts = {
            'title': 'Категория задачи',
            'owner': 'Укажите категорию',
        }
        for value, expected in fields_help_texts.items():
            with self.subTest(value=value):
                self.assertEqual(
                    category._meta.get_field(value).help_text, expected)

    def test_category_str(self):
        category = CategoryModelTest.category
        self.assertEquals(str(category), category.title)
