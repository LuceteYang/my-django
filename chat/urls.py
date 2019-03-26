from django.urls import path

from . import views

app_name = 'chat'
urlpatterns = [
    # 순서에 따라 먼저 탐
    path('', views.room, name='room'),
]
