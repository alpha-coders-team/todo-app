from django.urls import include, path
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'tasks', views.TaskViewSet, basename='tasks')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='accounts_api'))
]
