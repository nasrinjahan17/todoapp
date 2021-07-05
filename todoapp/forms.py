from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django import forms
from django.forms import ModelForm

status_choices = [
    ("Completed", "Completed"),
    ("Pending", "Pending"),
]


class SignupForm(UserCreationForm):
    username = forms.CharField(
        error_messages={"required": "Enter Username"},
        widget=forms.TextInput(attrs={"placeholder": "Username"}),
    )
    email = forms.EmailField(
        error_messages={"required": "Enter Email"},
        widget=forms.EmailInput(attrs={"placeholder": "Email"}),
    )
    password1 = forms.CharField(
        error_messages={"required": "Enter Password"},
        widget=forms.PasswordInput(attrs={"placeholder": "Password"}),
    )
    password2 = forms.CharField(
        error_messages={"required": "Enter Re-type password "},
        widget=forms.PasswordInput(attrs={"placeholder": "Re-Type Password"}),
    )

    # def __init__(self, *args, **kwargs):
    #     super(SignupForm, self).__init__(*args, **kwargs)

    #     for fieldname in ["username", "password1", "password2"]:
    #         self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )


class TodoForm(ModelForm):
    status = forms.ChoiceField(choices=status_choices, widget=forms.RadioSelect)

    class Meta:
        model = To_Do
        fields = ["title", "status", "priority"]
