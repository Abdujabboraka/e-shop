from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import MessageForm
from django.contrib.auth.models import User
from .models import UserMessage
from home.models import Profile

@login_required
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.creator = request.user
            message.sender = request.user
            receiver_id = request.POST.get('receiver_id')
            message.receiver = User.objects.get(id=receiver_id)
            message.save()
            return redirect('message_sent')
    else:
        form = MessageForm()

    context = {
        'form': form,
    }
    return render(request, 'messages/send_message.html', context)

@login_required
def notifications(request):
    user = request.user
    user_notifications = UserMessage.objects.filter(receiver=user).order_by('-timestamp')
    

    # Get all profiles in a dictionary to avoid repeated queries
    #profile_photos = {profile.user: profile.photo.url for profile in Profile.objects.filter(user__in=[msg.sender for msg in user_notifications])}
    # check if the profile photo is exsist or not
    profile_photos = {profile.user: profile.photo.url if profile.photo else None for profile in Profile.objects.filter(user__in=[msg.sender for msg in user_notifications])}
    # Attach sender profile photo to each notification
    notifications_with_photos = [
        {
            'message': message,
            'sender_photo': profile_photos.get(message.sender)
        }
        for message in user_notifications
    ]

    context = {
        'notifications': notifications_with_photos,

    }

    return render(request, 'messages/notifications.html', context)
