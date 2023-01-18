from django import forms
from .models import Post

class idForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['name','image','content','rate','devtool']