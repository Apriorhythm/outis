#coding=utf-8

from django import forms

from .models import OutisPost

class PostForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = OutisPost
        fields = ['category_id', 'title', 'link', 'description', 'tag', 'attraction']


