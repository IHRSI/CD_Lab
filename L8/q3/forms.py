from django import forms

class CGPAForm(forms.Form):
    name = forms.CharField(max_length=100, label='Student Name',
                          widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Enter name'}))
    marks = forms.DecimalField(max_digits=5, decimal_places=2, label='Total Marks',
                              widget=forms.NumberInput(attrs={'class': 'form-input', 'placeholder': 'Enter marks', 'step': '0.01'}))
