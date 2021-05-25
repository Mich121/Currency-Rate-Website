from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class':'form-control', 'value':'', 'placeholder':'User name...', 'id':'elder', 'type':'hidden'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
        } 

class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('post', 'author', 'name', 'body')

        widgets = {
            'post': forms.TextInput(attrs={'class':'form-control', 'value':'', 'placeholder':'Post id...', 'id':'elder', 'type':'hidden'}),
            'author': forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'userid', 'type':'hidden'}),
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
        }