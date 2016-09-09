from django import forms
from .models import *

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['name', 'alias','email', 'password', 'confirm_password']

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.password = self.cleaned_data['password']
        if commit:
            user.save()
        return user

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'author']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'rating']
# class RegisterForm(forms.Form):
#     first_name = forms.CharField(max_length=45)
#     last_name = forms.CharField(max_length=45)
#     email = forms.EmailField()
#     password = forms.CharField(max_length=100, widget=forms.PasswordInput)
#     confirm_password = forms.CharField(max_length=100, widget=forms.PasswordInput)
