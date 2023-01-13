from django.urls import path
from .views import show_user_list
from .views import create_user

urlpatterns = [
    path('show-user/',show_user_list),
    path('create-user/',create_user),
]
