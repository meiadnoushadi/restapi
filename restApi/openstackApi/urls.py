from django.urls import path
from .views import openstack_list_user
from .views import openstack_user_details
from .views import openstack_create_user
from .views import openstack_update_user
from .views import openstack_delete_user


urlpatterns = [
    path('openstack_list_user/',openstack_list_user),
    path('openstack_user_details/<pk>',openstack_user_details),
    path('openstack_create_user/',openstack_create_user),
    path('openstack_update_user/<pk>',openstack_update_user),
    path('openstack_delete_user/<pk>',openstack_delete_user),
]
