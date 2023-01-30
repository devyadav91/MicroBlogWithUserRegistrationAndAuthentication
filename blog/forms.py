from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from django import forms
from django.views.generic.edit import CreateView
from .models import article

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {'email':'Email ',
                    'username':'User Name ',
                    'first_name':'First Name ',
                    'last_name':'Last Name '
                    }
        widgets = {
                   'username':forms.TextInput(attrs={'class':'form-control'}) ,
                   'first_name':forms.TextInput(attrs={'class':'form-control'}),
                   'last_name':forms.TextInput(attrs={'class':'form-control'}) ,
                   'email':forms.EmailInput(attrs={'class':'form-control'}) ,
        }


class LogInForm(AuthenticationForm):
    username = UsernameField(label='User Name',widget=forms.TextInput(attrs={'class':'form-control','autofocus': True}))
    password = forms.CharField(label=_('Password'),strip=False,
                            widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))

class AddPostForm(forms.ModelForm):
    class Meta:
        model = article
        fields = ['title','content']
        labels ={'title':"Topic",'content':'Description' }
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'content':forms.Textarea(attrs={'class':'form-control'}),
        }
    
 