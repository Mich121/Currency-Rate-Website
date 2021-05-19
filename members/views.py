from django.shortcuts import render
from django.views import generic
from .forms import RegisterForm, ProfilePageForm
from django.urls import reverse_lazy
from cantor.models import Profile

# Create your views here.
class UserRegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('home')

class CreateProfile(generic.CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/create_profile_page.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class UpdateProfile(generic.UpdateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/update_profile_page.html'
    success_url = reverse_lazy('home')