from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.db import transaction
from .models import My_user, Invoices

class ModeratorSignUpForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = My_user
        fields = ['username']
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_moderator = True
        user.save()
        return user

class AdminSignUpForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = My_user
        fields = ['username']
    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_admin = True
        if commit:
            user.save()
        return user

class InvoicesCreationForm(forms.ModelForm):
    class Meta:
        model = Invoices
        fields = ['date', 'number', 'supply', 'comment']