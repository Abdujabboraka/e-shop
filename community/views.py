from django.shortcuts import render, redirect
from .models import Opinion, Support
from .forms import OpinionForm, SupportForm
from django.views.generic import ListView, CreateView

def CommunityView(request):
    opinions = Opinion.objects.all()
    supports = Support.objects.all()
    form = OpinionForm()

    if request.method == 'POST':
        form = OpinionForm(request.POST)
        if form.is_valid():
            opinion = form.save(commit=False)
            opinion.user = request.user
            opinion.save()
            return redirect('community')
        else:
            form_errors = form.errors

    context = {
        'opinions': opinions,
        'supports': supports,
        'form': form,
    }
    return render(request, 'community/lobby.html', context)


class SupportListView(ListView):
    model = Support
    template_name = 'community/support.html'
    context_object_name = 'supports'

    def get_queryset(self):
        return Support.objects.filter(user=self.request.user)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SupportForm()
        return context

    def post(self, request, *args, **kwargs):
        form = SupportForm(request.POST, request.FILES)
        if form.is_valid():
            support = form.save(commit=False)
            support.user = request.user
            support.save()
            return redirect('supporturl')
        else:
            return render(request, 'community/support.html', {'form': form})