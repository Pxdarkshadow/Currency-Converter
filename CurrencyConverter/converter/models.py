from django.db import models
class ExchangeRate(models.Model):
    currency_code = models.CharField(max_length=3, unique=True)
    currency_name = models.CharField(max_length=50)
    rate_to_usd = models.FloatField(help_text="Exchange rate to 1 USD")
    last_updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.currency_code} - {self.currency_name}"

