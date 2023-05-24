from django.contrib import admin

#from .models import CustomUser

#class CustomUserAdmin(admin.ModelAdmin):

    #list_display = ('id', 'username')

    #list_display_links = ('id','username')

from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm
CustomUser = get_user_model()

class CustomUserAdmin(UserAdmin):

    add_form = CustomUserCreationForm
    model = CustomUser
    list_display = ('id', 'username')

admin.site.register(CustomUser, CustomUserAdmin)