from dataclasses import field
from django.contrib.auth.forms import UserCreationForm

from accounts.models import MyUser

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ('f_name','l_name','mobileno','password1','password2','address')

class MyAdminCreationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ('f_name','l_name','mobileno','role','password1','password2','address')