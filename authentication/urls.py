from django.urls import path
from authentication import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.authlogin, name='login'),
    path('logout/', views.authlogout, name='logout'),
]
