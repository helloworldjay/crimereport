from django import forms
from django.forms.widgets import PasswordInput, Widget
from .models import User
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].required = True
        self.fields['district'].required = True
    username = forms.RegexField(max_length=30,regex=r'^[\w.@+-]+$', help_text="abc",
    widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder' : 'ID 입력',
            'required' : 'True',
        })
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder' : '비번 입력',
            'required' : 'True',
        })
    )
    password2 = forms.CharField(help_text='bbc',
        widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder' : '비번 확인 입력',
            'required' : 'True',
        })
    )
    age = forms.DecimalField(max_value=100,
    widget=forms.NumberInput(
        attrs={
            'class':'form-control',
            'placeholder' : '나이 입력',
            'required' : 'True',
        })
    )
    class Meta(UserCreationForm.Meta):
        
        model = User
        fields = ['username','password1','password2','age', 'city','district'] # input elements