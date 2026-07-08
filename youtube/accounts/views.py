from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic import CreateView
from django.urls import reverse_lazy
from accounts.forms import CustomUserCreationForm

# Create your views here.

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('accounts:login')
    template_name = "accounts/register.html"

    # to check the form where it is authenticated or not 
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super().dispatch(request, *args, **kwargs)
    
    # to valid the form and login the details
    def form_vaid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return redirect('/')
    