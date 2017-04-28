from django import forms

from .models import OutisPost

class PostForm(forms.ModelForm):
    class Meta:
        model = OutisPost
        fields = ['category_id', 'title', 'link', 'description', 'tag', 'attraction']


