from django.urls import path
from .views import CommunityView, SupportListView
urlpatterns = [
    path('lobby', CommunityView, name='community'),
    path('support', SupportListView.as_view(), name='supporturl')
]