from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100, label='Username', 
                              widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Enter username'}))
    password = forms.CharField(max_length=100, label='Password', required=False,
                              widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Enter password'}))
    email = forms.EmailField(label='Email', required=False,
                            widget=forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Enter email'}))
    contact = forms.CharField(max_length=20, label='Contact Number', required=False,
                             widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Enter contact number'}))
