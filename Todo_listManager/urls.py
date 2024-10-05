from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('task_list/', views.task_list, name='task_list'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]