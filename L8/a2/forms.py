from django import forms

class FeedbackForm(forms.Form):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    
    COURSE_CHOICES = [
        ('asp-xml', 'ASP-XML'),
        ('dotnet', 'DotNET'),
        ('javapro', 'JavaPro'),
        ('unix', 'Unix'),
        ('c', 'C'),
        ('cpp', 'C++'),
    ]
    
    student_name = forms.CharField(max_length=100, label='Student Name',
                                  widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Enter your name'}))
    gender = forms.ChoiceField(choices=GENDER_CHOICES, label='Gender',
                              widget=forms.Select(attrs={'class': 'form-input'}))
    course = forms.ChoiceField(choices=COURSE_CHOICES, label='Select Course',
                              widget=forms.Select(attrs={'class': 'form-input'}))
    suggestion = forms.CharField(label='Suggestion', required=False,
                                widget=forms.Textarea(attrs={'class': 'form-input', 'rows': 5, 'placeholder': 'Enter your suggestion'}))
