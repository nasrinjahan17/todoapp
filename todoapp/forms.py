from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django import forms 
from django.forms import ModelForm 

status_choices = [
        ('Completed','Completed'),
        ('Pending','Pending'),
    ]

class SignupForm(UserCreationForm):
    username = forms.CharField(error_messages={'required':'Enter Username'},widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password1 = forms.CharField(error_messages={'required':'Enter Password'},widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    password2 = forms.CharField(error_messages={'required':'Enter Re-type password '},widget=forms.PasswordInput(attrs={'placeholder':'Re-Type Password'}))
    email = forms.EmailField(error_messages={'required':'Enter Email'},widget=forms.EmailInput(attrs={'placeholder':'Email'}))
    
    class Meta:
        model = User
        fields = ('username','password1','password2','email')
        

class TodoForm(ModelForm):
    status = forms.ChoiceField(choices=status_choices, widget=forms.RadioSelect)
    class Meta:
        model= To_Do
        fields = ['title','status','priority']
    
    
