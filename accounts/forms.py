from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

#from .models import CustomUser

#from django.contrib.auth.models import User

#class SignupForm(UserCreationForm):
    #class Meta(UserCreationForm.Meta):
        #model = CustomUser
        #fields = ('username',)

#class UserCreationForm(form.ModelForm):
    #class Meta:
        #model = User
        #fields = ('username',)

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        #model = CustomUser
        model = get_user_model()

        fields = ('username','password1','password2',)
