from django.urls import path
from .views import earning
urlpatterns = [
    path('tasks/', earning, name='earning'),
]