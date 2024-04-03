from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record



class Signupform(UserCreationForm):
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder': 'Email Address'
    })) 
    
    first_name = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder': 'Enter First Name'
    }))
    
    last_name = forms.CharField(label='',max_length=100, widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder': 'Enter Last Name'
    }))
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        
        
    def __init__(self, *args, **kwargs):
        super(Signupform, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label=''
        self.fields['username'].help_text = '<span class="form-text text-info"><small>Required. 150 character or fewer. Letter, digit and @/./+/-/_ only</small></span>'
        
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-info "><small>Enter the same password as before, for verification.</small></span>'
        
        
class AddRecord(forms.ModelForm):
    firstname = forms.CharField( required=True, label='', widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder': 'Enter First Name'
    }))
    lastname = forms.CharField( required=True, label='', widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder': 'Enter Last Name'
    }))
    email = forms.EmailField( required=True, label='', widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder': 'Enter Email'
    }))
    phone = forms.IntegerField( required=True, label='', widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder': 'Enter Phone no...'
    }))
    address = forms.CharField( required=True, label='', widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder': 'Enter Address'
    }))
    city = forms.CharField( required=True, label='', widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder': 'Enter City'
    }))
    state = forms.CharField( required=True, label='', widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder': 'Enter State'
    }))
    zipcode = forms.IntegerField( required=True, label='', widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder': 'Enter Zipcode'
    }))
    
    class Meta:
        model = Record
        exclude = ('user',)