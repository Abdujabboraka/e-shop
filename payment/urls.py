from django.urls import path
from .views import payment_view


urlpatterns = [
    path('buy-coin', payment_view, name='payment')
]