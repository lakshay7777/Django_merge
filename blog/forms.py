from django import forms
from .models import Tag, Category, Post
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'category', 'tag', 'feature_image','thumnail_image')

class UserSignUpForm(forms.ModelForm):
    
    username = forms.CharField(
        required=False, 
        widget=forms.TextInput(attrs={'placeholder': 'Username'}),
    )

        
    class Meta:
        model = User
        fields = ('username', 'password','phone_number','email','city','state','country','user_profile_image')
       

class userloginForm(forms.ModelForm):
    username = forms.CharField(
    required=False, 
    widget=forms.TextInput(attrs={'placeholder': 'Username'}),)
    class Meta:
        model = User
        fields = ('username', 'password')
    

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'username',
            'phone_number',
            'city',
            'state',
            'country',
            'email',
            'user_profile_image',
        )
        exclude = ('password',)





