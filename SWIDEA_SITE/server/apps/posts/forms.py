from django import forms
from .models import Post

class idForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','image','content','rate','devtool']