from django.db.models import fields
from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name','comment']
    name = forms.CharField(max_length=120)
    comment = forms.CharField(max_length=255)