from django.urls import path
from .views import *


urlpatterns = [
    path('rockets/', RocketListView, name='rocket_list_url'),
    path('rocket/<int:rocket_id>', RocketDetailView, name='rocket_detail_url'),
    path('create_rocket', RocketCreateView, name='rocket_create_url'),
    path('rocket_update/<int:rocket_id>', RocketUpdateView, name='rocket_update_url'),
    path('rocket_delete/<int:rocket_id>', RocketDeleteView, name='rocket_delete_url')
]




