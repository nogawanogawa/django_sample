from django import forms
from .models import Person

class UserForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'mail', 'age']
    