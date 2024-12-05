from django import forms
from .models import ToDo

class ToDoEditForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ['title']