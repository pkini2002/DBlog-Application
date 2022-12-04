from django import forms
from .models import Post
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
        title =forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder':'Title'}))
        title_tag =forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder':'Title tag'}))
        author =forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder':'Title tag'}))
        body =forms.CharField(widget=forms.Textarea(attrs={ 'class' : 'form-control', 'placeholder':'Content'}))
    
        class Meta:
            model = Post
            fields = ['title','title_tag','author','body'] 

class EditForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','title_tag','body')

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'})
        }

         