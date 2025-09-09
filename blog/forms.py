from django import forms
from .models import Comment

class EmailPostForm(forms.Form):   #Normal Form
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,
                               widget=forms.Textarea)
    
class CommentForm(forms.ModelForm): #Model Form
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')