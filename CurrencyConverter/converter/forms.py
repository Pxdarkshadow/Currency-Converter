from django import forms
class CurrencyConverterForm(forms.Form):
    CURRENCY_CHOICES = [
        ('USD', 'US Dollar (USD)'),
        ('EUR', 'Euro (EUR)'),
        ('JPY', 'Japanese Yen (JPY)'),
        ('INR', 'Indian Rupee (INR)'),
        ('MXN', 'Mexican Peso (MXN)'),
        ('GBP', 'British Pound (GBP)'),
    ]
    amount = forms.DecimalField(
        min_value=0.01, 
        max_digits=15, 
        decimal_places=2,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter amount',
        })
    )
    from_currency = forms.ChoiceField(
        choices=CURRENCY_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    to_currency = forms.ChoiceField(
        choices=CURRENCY_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
