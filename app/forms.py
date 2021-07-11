from django.forms import ModelForm
from django import forms
from django.forms.widgets import PasswordInput
from app.models import TODO, Blocklist


class TODOForm(ModelForm):
    class Meta:
        model = TODO
        fields = ['title', 'status', 'priority']


class CreateBlocklist(ModelForm):
    class Meta:
        model = Blocklist
        fields = ['name']