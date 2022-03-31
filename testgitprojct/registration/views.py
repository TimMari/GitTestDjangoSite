from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .forms import RegUserForm


class RegUser(CreateView):
    form_class = RegUserForm
    template_name = 'registration/reg.html'
    success_url = reverse_lazy('prof')


class AuthUser(LoginView):
    form_class = RegUserForm
    template_name = 'registration/auth.html'


@login_required
def prof(request):
    return render(request, 'registration/prof.html')
