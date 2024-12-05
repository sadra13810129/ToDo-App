from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomSignupForm
from django.urls import reverse_lazy

class CustomSignUpView(CreateView):
    template_name = 'accounts/signup.html'
    form_class = CustomSignupForm
    success_url = '/accounts/login/'


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("todo:task-list")


class CustomLogoutView(LogoutView):
    template_name = 'accounts/logout.html'

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        return redirect('accounts:login')
    
