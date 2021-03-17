from django.contrib import admin
from django.urls import include, path
from django.conf.urls import handler403

handler403 = 'tasks.views.forbidden' # noqa

urlpatterns = [
    path('auth/', include('users.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('tasks.urls')),
]
