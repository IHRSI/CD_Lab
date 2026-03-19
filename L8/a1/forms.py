from django import forms

class BillForm(forms.Form):
    BRAND_CHOICES = [
        ('hp', 'HP'),
        ('nokia', 'Nokia'),
        ('samsung', 'Samsung'),
        ('motorola', 'Motorola'),
        ('apple', 'Apple'),
    ]
    
    DEVICE_CHOICES = [
        ('mobile', 'Mobile'),
        ('laptop', 'Laptop'),
    ]
    
    brand = forms.ChoiceField(choices=BRAND_CHOICES, widget=forms.RadioSelect, label='Select Brand')
    devices = forms.MultipleChoiceField(choices=DEVICE_CHOICES, widget=forms.CheckboxSelectMultiple, label='Select Device(s)')
    quantity = forms.IntegerField(min_value=1, label='Quantity', 
                                 widget=forms.NumberInput(attrs={'class': 'form-input', 'placeholder': 'Enter quantity'}))
