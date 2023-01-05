from django.contrib import admin
from django.urls import path, include
from Todo import views

urlpatterns = [
    path('', views.index, name='home'),
    path('create_todo', views.create_todo, name='create_todo'),
    path('update_todo', views.update_todo, name='update_todo'),
    path('delete_todo', views.delete_todo, name='delete_todo'),
    

]