from django import forms
from .models import Tag, Category, Post
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User
# from django.forms import ModelForm
# from .models import MyModel



class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'category', 'tag', 'feature_image','thumnail_image')

class UserSignUpForm(forms.ModelForm):
    # email = forms.EmailField(required=True)
    username = forms.CharField(
        required=False,  # Make the username field optional
        widget=forms.TextInput(attrs={'placeholder': 'Username'}),
        # help_text='Enter your username (optional).',
        # error_messages={
        #     'required': 'Username is optional.'
        # }
    )

        
    class Meta:
        model = User
        fields = ('username', 'password','phone_number','email','city','state','country','user_profile_image')
        # fields = '__all__'

class userloginForm(forms.ModelForm):
    username = forms.CharField(
    required=False,  # Make the username field optional
    widget=forms.TextInput(attrs={'placeholder': 'Username'}),)
    class Meta:
        model = User
        fields = ('username', 'password')
    
        
        # class MyModelForm(ModelForm):
        #     class Meta:
        #         model = MyModel  # Connect the form to the 'MyModel'
        #         fields = '__all__'

    #  class meta:
    #      model = User
    #      fields = ('username', 'password','phone_number','email','city','state','country','user_profile_image')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'username',
            'phone_number',
            'city',
            'state',
            'country',
        ) 
        exclude = ('password',)


#################################################################







