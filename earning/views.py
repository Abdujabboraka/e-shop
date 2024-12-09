from django.shortcuts import render
from django.contrib import messages
from home.models import Profile
# Create your views here.

def earning(request):
    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)

    user_profile = Profile.objects.get(user=request.user)
    user_bonus = not user_profile.first_bonus

    if request.method == 'POST':
        reward = int(request.POST.get('reward', 0))

        if reward == 600 and user_profile.first_bonus == False:
            user_profile.balance += 600
            user_profile.first_bonus = True
            user_profile.save()
            messages.success(request, "You have claimed your first bonus of 600 cp!")

    context = {
        'user_bonus': user_bonus,
        'user': user,
        'profile': profile
    }
    return render(request, 'Earning/index.html', context)