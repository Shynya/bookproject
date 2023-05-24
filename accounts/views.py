from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.conf import settings

#from .forms import SignupForm
from .forms import CustomUserCreationForm

class SignupView(CreateView):
    #model = User
    model = settings.AUTH_USER_MODEL
    #form_class = SignupForm
    form_class = CustomUserCreationForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('index')

