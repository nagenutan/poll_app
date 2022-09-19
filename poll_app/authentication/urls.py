from django.contrib import admin
from django.urls import path, include
from.import views

urlpatterns = [
    path('signup', views.signup),
    path('login', views.login),
    path('create_poll', views.create_poll),
    path('get_polls_by_user', views.get_polls_by_user),
    path('get_polls_created_by_others', views.get_polls_created_by_others),
    path('get_profile', views.get_profile_data), 
    path('delete_data_24',views.data_24) 
]
