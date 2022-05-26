from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length = 50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Type ypur first name here'}))
    last_name = forms.CharField(max_length = 50, widget=forms.TextInput(attrs={'class':'form-control',  'placeholder':'Type ypur first name here'}))

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')

    def __init__(self, *args,**kwargs):
        super(SignUpForm, self).__init__(*args,**kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image','BITS_ID','hostel_name','room','mob']

class InitialUpdate(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['BITS_ID','hostel_name','room','mob']











