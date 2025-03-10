from django import forms
from .models import Todo

# dev_3


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "description", "important"]
