from django.urls import path
from .views import register_user, list_users

urlpatterns = [
    path('api/register/', register_user, name='register_user'),
    path('api/users/', list_users, name='list_users'),
]