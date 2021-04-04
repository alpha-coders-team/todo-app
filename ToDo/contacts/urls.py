from django.urls import path

from . import views

urlpatterns = [
    path('contact_us/', views.ContactView.as_view(), name='contact_us'),
    path('email_sent/', views.EmailSent.as_view(), name='email_sent')
]