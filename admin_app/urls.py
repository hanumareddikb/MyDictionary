from django.urls import path
from admin_app import views

urlpatterns = [
    path('user_messages/', views.user_messages, name='user_messages'),
]
