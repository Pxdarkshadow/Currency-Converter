from django.shortcuts import render
from .forms import CurrencyConverterForm
import requests
import json
from decimal import Decimal
def index(request):
    result = None
    converted_amounts = {}
    form = CurrencyConverterForm()
    currencies = {
        'USD': 'US Dollar',
        'EUR': 'Euro',
        'JPY': 'Japanese Yen',
        'INR': 'Indian Rupee',
        'MXN': 'Mexican Peso',
        'GBP': 'British Pound'
    }
    exchange_rates = {
        'USD': 1.0,
        'EUR': 0.92,
        'JPY': 153.24,
        'INR': 83.42,
        'MXN': 16.78,
        'GBP': 0.79
    }
    if request.method == 'POST':
        form = CurrencyConverterForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            from_currency = form.cleaned_data['from_currency']
            to_currency = form.cleaned_data['to_currency']
            amount_in_usd = float(amount) / exchange_rates[from_currency]
            converted_amount = amount_in_usd * exchange_rates[to_currency]
            result = {
                'amount': amount,
                'from_currency': from_currency,
                'from_currency_name': currencies[from_currency],
                'to_currency': to_currency,
                'to_currency_name': currencies[to_currency],
                'converted_amount': round(converted_amount, 2)
            }
            for code, rate in exchange_rates.items():
                converted = amount_in_usd * rate
                converted_amounts[code] = {
                    'code': code,
                    'name': currencies[code],
                    'amount': round(converted, 2)
                }
    context = {
        'form': form,
        'result': result,
        'converted_amounts': converted_amounts,
        'currencies': currencies
    }
    return render(request, 'converter/index.html', context)