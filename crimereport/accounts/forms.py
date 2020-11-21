from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].required = True
        self.fields['district'].required = True
        

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username','password','city','district'] # input elements