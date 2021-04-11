from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('api/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('users/', include('users.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('tasks.urls')),
    path('', include('contacts.urls')),
]
