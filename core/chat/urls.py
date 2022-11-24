from django.urls import path

from .views import index, chat_room

urlpatterns = [
    path('', index, name='main'),
    path('<str:chat_name>/', chat_room, name='room')

]