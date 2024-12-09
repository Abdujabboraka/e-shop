from django.urls import path
from .views import send_message, notifications
urlpatterns = [
    path('', send_message, name='message'),
    path('notifications/', notifications, name='notifications')
]