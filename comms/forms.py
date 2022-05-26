from django import forms
from .models import *

choices = Category.objects.all().values_list('name','name')
choice_list = []
for item in choices:
    choice_list.append(item) 
yr = {('1st Year','1st Year'),('2nd Year','2nd Year'),('3rd Year','3rd Year'),('4th Year','4th Year'),('5th Year','5th Year')}

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('title','body', 'category','year')

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Some relevant topic of your question'}),
            'body':forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Type your Question here'}),
            'category': forms.Select(choices=choice_list, attrs={'class':'form-control'}),
            'year': forms.Select(choices=yr, attrs={'class':'form-control'}),
        }

class CommentcreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

        widgets = {
            'body':forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Type your answer here'}),
        }

class RatingForm(forms.ModelForm):

    class Meta:
        model = Rating
        fields=['rating']

