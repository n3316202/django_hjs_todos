from django import forms
from .models import Todo
from rest_framework import serializers
# dev_7
# class TodoForm(forms.ModelForm):
#     class Meta:
#         model = Todo
#         fields = ["title", "description", "important"]

class TodoDRFSerializer(serializers.ModelSerializer):
    class  Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'created', 'complete', 'important')
