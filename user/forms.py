from django import forms
from django.contrib.auth.models import User
from django.forms import widgets


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = {'username', 'password'}
        labels = {'username':'用户名1', 'password':'密码1'}
        widgets = {'password':widgets.PasswordInput}
        help_texts = {'username':''}
