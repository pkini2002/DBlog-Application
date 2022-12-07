from django import forms
from .models import Post,Category,Comment
from django.contrib.auth.models import User

choices=Category.objects.all().values_list('name','name')
choice_list=[]

for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','author','category','body','snippet','header_image')

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Title'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title tag'}),
            'author':forms.Select(attrs={'class':'form-control','placeholder':'username','id':'elder','value':''}),
            'category':forms.Select(choices=choice_list,attrs={ 'class' : 'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Content'}),
            'snippet':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Content'})
        }
       
    
class EditForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','title_tag','body','snippet')

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
            'snippet':forms.Textarea(attrs={'class':'form-control'})
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('name','body')

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=('name',)

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'})
        }

         