from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import SignUpForm


# Create your views here.
class SignUpView(CreateView, SuccessMessageMixin):
    template_name = 'signup.html'
    success_url = reverse_lazy('account:signin')
    form_class = SignUpForm
    success_message = 'Your have been created an account successfully.🎊'


class SignInView(LoginView, SuccessMessageMixin):
    template_name = 'signin.html'
    success_message = 'Welcome~😍'
    success_url = reverse_lazy('display:home')
