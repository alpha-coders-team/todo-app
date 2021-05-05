from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from tasks.models import Task

User = get_user_model()

OWNER = 'owner'
OTHER = 'other'
TITLE = 'test_title'
CONTACT_US = reverse('contact_us')
EMAIL_SENT = reverse('email_sent')
INDEX_URL = reverse('index')
ADD_TASK = reverse('add-task')
ADD_CATEGORY = reverse('add-category')
USER_DELETE = reverse('user_delete')
CUSTOM_LOGOUT = reverse('customlogout')
SIGNIN = reverse('signin')
SIGNUP = reverse('signup')
PASSWORD_CHANGE = reverse('custom_password_change')
PASSWORD_CHANGE_DONE = reverse('custom_password_change_done_view')

INDEX_REDIRECT = f'{SIGNIN}?next={INDEX_URL}'
CONTACT_US_REDIRECT = f'{SIGNIN}?next={CONTACT_US}'
EMAIL_SENT_REDIRECT = f'{SIGNIN}?next={EMAIL_SENT}'
ADD_TASK_REDIRECT = f'{SIGNIN}?next={ADD_TASK}'
ADD_CATEGORY_REDIRECT = f'{SIGNIN}?next={ADD_CATEGORY}'
USER_DELETE_REDIRECT = f'{SIGNIN}?next={USER_DELETE}'
CUSTOM_LOGOUT_REDIRECT = f'{SIGNIN}?next={CUSTOM_LOGOUT}'
PASSWORD_CHANGE_REDIRECT = f'{SIGNIN}?next={PASSWORD_CHANGE}'
PASSWORD_CHANGE_DONE_REDIRECT = f'{SIGNIN}?next={PASSWORD_CHANGE_DONE}'


class TaskURLTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.author = User.objects.create_user(
            username=OWNER)
        cls.other = User.objects.create_user(
            username=OTHER)
        cls.task = Task.objects.create(
            owner=cls.author,
            title=TITLE,
        )
        cls.DETAIL_VIEW = reverse(
            'view-task', args=[OWNER, cls.task.id])
        cls.DETAIL_VIEW_REDIRECT = f'{SIGNIN}?next={cls.DETAIL_VIEW}'
        cls.UPDATE_TASK = reverse(
            'update-task', args=[OWNER, cls.task.id])
        cls.UPDATE_TASK_REDIRECT = (
            f'{SIGNIN}?next={cls.UPDATE_TASK}')
        cls.ADD_COMMENT = reverse(
            'add_comment', args=[OWNER, cls.task.id])
        cls.ADD_COMMENT_REDIRECT = (
            f'{SIGNIN}?next={cls.ADD_COMMENT}')
        cls.guest_client = Client()
        cls.authorized_client_author = Client()
        cls.authorized_client_author.force_login(cls.author)

    def test_url_status_code(self):
        url_list = (
            (CONTACT_US, self.authorized_client_author, 200),
            (EMAIL_SENT, self.guest_client, 200),
            (INDEX_URL, self.authorized_client_author, 200),
            (ADD_TASK, self.authorized_client_author, 200),
            (self.DETAIL_VIEW, self.authorized_client_author, 200),
            (self.UPDATE_TASK, self.authorized_client_author, 200),
            (ADD_CATEGORY, self.authorized_client_author, 200),
            (USER_DELETE, self.authorized_client_author, 200),
            (SIGNIN, self.authorized_client_author, 200),
            (SIGNUP, self.authorized_client_author, 200),
            (PASSWORD_CHANGE, self.authorized_client_author, 200),
            (PASSWORD_CHANGE_DONE, self.authorized_client_author, 200),
        )
        for url, client, status_code in url_list:
            with self.subTest(value=url):
                self.assertEqual(
                    client.get(url).status_code, status_code)

    def test_url_uses_correct_template(self):
        url_list = (
            (CONTACT_US, self.authorized_client_author,
             'contacts/contact_us.html'),
            (EMAIL_SENT, self.authorized_client_author,
             'contacts/email_sent_confirm.html'),
            (INDEX_URL, self.authorized_client_author, 'tasks/index.html'),
            (ADD_TASK, self.authorized_client_author, 'tasks/add-task.html'),
            (self.DETAIL_VIEW, self.authorized_client_author,
             'tasks/task_detail.html'),
            (self.UPDATE_TASK, self.authorized_client_author,
             'tasks/add-task.html'),
            (ADD_CATEGORY, self.authorized_client_author,
             'tasks/add-category.html'),
            (USER_DELETE, self.authorized_client_author,
             'users/account_delete_confirm.html'),
            (SIGNIN, self.authorized_client_author, 'users/signin.html'),
            (SIGNUP, self.authorized_client_author, 'users/signup.html'),
            (PASSWORD_CHANGE, self.authorized_client_author,
             'registration/password_change_form.html'),
            (PASSWORD_CHANGE_DONE, self.authorized_client_author,
             'registration/password_change_done.html'),
        )
        for url, client, template in url_list:
            with self.subTest(value=url):
                self.assertTemplateUsed(client.get(url), template)

    def test_urls_correct_redirect(self):
        url_list = (
            (INDEX_URL, self.guest_client, INDEX_REDIRECT),
            (CONTACT_US, self.guest_client, CONTACT_US_REDIRECT),
            (ADD_TASK, self.guest_client, ADD_TASK_REDIRECT),
            (ADD_CATEGORY, self.guest_client, ADD_CATEGORY_REDIRECT),
            (PASSWORD_CHANGE, self.guest_client,
             PASSWORD_CHANGE_REDIRECT),
            (PASSWORD_CHANGE_DONE, self.guest_client,
             PASSWORD_CHANGE_DONE_REDIRECT),
            (self.UPDATE_TASK, self.guest_client, self.UPDATE_TASK_REDIRECT),
            (self.DETAIL_VIEW, self.guest_client, self.DETAIL_VIEW_REDIRECT),
            (self.ADD_COMMENT, self.guest_client, self.ADD_COMMENT_REDIRECT),
        )
        for reverse_name, client, redirect in url_list:
            with self.subTest(value=reverse_name):
                self.assertRedirects(client.get(reverse_name), redirect)
