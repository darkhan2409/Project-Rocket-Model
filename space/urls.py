from django.urls import path
from .views import *
from django.views.generic import TemplateView


urlpatterns = [
    path('rockets/', RocketListView, name='rocket_list_url'),
    path('rocket/<int:rocket_id>', RocketDetailView, name='rocket_detail_url'),
    path('create_rocket', RocketCreateView, name='rocket_create_url'),
    path('rocket_update/<int:rocket_id>', RocketUpdateView, name='rocket_update_url'),
    path('rocket_delete/<int:rocket_id>', RocketDeleteView, name='rocket_delete_url'),

    path('about_us/', TemplateView.as_view(template_name='about_us.html'), name='about_us_url'),
    path('sign_in/', signIn, name='sign_in_url'),
    path('sign_out/', signOut, name='sign_out_url'),
    path('sign_up/', signUp, name='sign_up_url'),
]




