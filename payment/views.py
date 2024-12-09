from django.shortcuts import render
from home.models import Profile
# Create your views here.
def payment_view(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    context = {
        'user': user,
        'profile': profile
    }
    return  render(request, 'payment/index.html', context)