from django import forms
from .models import Post,Category
from django.contrib.auth.models import User

choices=Category.objects.all().values_list('name','name')
choice_list=[]

for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
        title =forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder':'Title'}))
        title_tag =forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder':'Title tag'}))
        author =forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control','placeholder':'username','id':'elder','type':'hidden','value':''}))
        category =forms.CharField(widget=forms.Select(choices=choice_list,attrs={ 'class' : 'form-control'}))
        body =forms.CharField(widget=forms.Textarea(attrs={ 'class' : 'form-control', 'placeholder':'Content'}))
       
    
        class Meta:
            model = Post
            fields = ['title','title_tag','author','category','body'] 

class EditForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','title_tag','body')

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'})
        }

         