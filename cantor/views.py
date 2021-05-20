from cantor.models import Currency, Profile
from django.shortcuts import render, get_object_or_404
import requests
import json
from django.views import generic
from .forms import BuyCurrencyForm, SellCurrencyForm
from django.db.models import Sum
#generate graph
import matplotlib.pyplot as plt
import base64
from io import BytesIO

# Create your views here.
def Home(request):
   return render(request, "map.html")

#first option to show currency rate in 'country.html'
# def country(request, ticker):
#    context = {}
#    context['ticker'] = ticker
#    #get data from api
#    url = 'https://api.frankfurter.app/latest?from=usd'
#    response = requests.get(url)
#    #get all currencies data, based on usd
#    currencies_data = response.json()
#    #get currency rate
#    currency_rate = currencies_data['rates'][ticker]
#    currency_rate = round(currency_rate, 2)
#    context['currency_rate'] = currency_rate
#    return render(request, "country.html", context)


class BuyCurrency(generic.CreateView):
   model = Currency
   form_class = BuyCurrencyForm
   template_name = "country.html"

   def get_context_data(self, *args, **kwargs):
      context = super(BuyCurrency, self).get_context_data(*args, **kwargs)
      ticker = self.kwargs['ticker']
      context['ticker'] = ticker
      #get data from API
      url = 'https://api.frankfurter.app/latest?from=USD'
      response = requests.get(url)
      #get all currencies data, based on USD
      currencies_data = response.json()
      #get currency rate
      currency_rate = currencies_data['rates'][ticker]
      currency_rate = round(currency_rate, 2)
      context['currency_rate'] = currency_rate
      return context

   #inicialize 'currency' field in form with currency ticker
   def get_initial(self, *args, **kwargs):
        initial = super(BuyCurrency, self).get_initial(**kwargs)
        initial['currency'] = self.kwargs['ticker']
        return initial

   
class Account(generic.ListView):
   model = Currency
   template_name = 'account.html'

   def get_context_data(self, *args, **kwargs):
      context = super(Account, self).get_context_data(*args, **kwargs)
      #get 'pk' from url
      pk = self.kwargs['pk']
      context['pk'] = pk

      #get data from API
      url_rates = 'https://api.frankfurter.app/latest?from=USD'
      response = requests.get(url_rates)
      #get all currencies data, based on USD
      currencies_data = response.json()

      #create ticker table
      tickers = ['BGN','CHF','CZK','DKK','EUR','GBP','HUF','ISK','NOK','PLN','RON','RUB','SEK']
      context['tickers'] = tickers
      #create dictonaries with value for current account
      user_currency = {'BGN': 0.00,'CHF': 0.00,'CZK': 0.00,'DKK': 0.00,'EUR': 0.00,'GBP': 0.00,'HUF': 0.00,'ISK': 0.00,'NOK': 0.00,'PLN': 0.00,'RON': 0.00,'RUB': 0.00,'SEK': 0.00}
      total_amount_currency = 0
      currency_values_in_dollars = []

      #choose correct user and add to context to use in 'account.html'
      appropriate_user = get_object_or_404(Profile, id=self.kwargs['pk'])
      context['appropriate_user'] = appropriate_user
      #pass for all ticker
      for ticker in tickers:
         if Currency.objects.filter(owner=appropriate_user.user, currency=ticker).exists():
            #sum all object from account with the same ticker, get all amount of some currency
            sum_currency = Currency.objects.filter(owner=appropriate_user.user, currency=ticker).aggregate(Sum('price'))
            #get values from dictonaries
            for total in sum_currency.values():
               #add to list values in dollars before changing to currency
               currency_values_in_dollars.append(total)
               total_amount_currency = total
            
            #delete objects, because we must have one object from user connected with one currency
            for i in Currency.objects.filter(owner=appropriate_user.user, currency=ticker):
               i.delete()
            #and create new with sum of price deleted objects
            obj_sum_currency = Currency.objects.create(owner=appropriate_user.user, currency=ticker, price=total_amount_currency)
            #change value in 'user_currency' to appriopriate for different current
            user_currency[ticker] = round(total_amount_currency * currencies_data['rates'][ticker], 2)

      #get sum of our currencies
      total_currencies_values = sum(currency_values_in_dollars)
      context['total_currencies_values'] = total_currencies_values
      #dictonaries with ticker and values
      context['user_currency'] = user_currency
      
      return context

class Statistic(generic.ListView):
   model = Currency
   template_name = 'statistic.html'

   def get_context_data(self, *args, **kwargs):
      context = super(Statistic, self).get_context_data(*args, **kwargs)
      #get 'pk' from url
      pk = self.kwargs['pk']
      context['pk'] = pk

      #choose correct user
      appropriate_user = get_object_or_404(Profile, id=self.kwargs['pk'])

      #choose currency of user
      currencies = Currency.objects.filter(owner=appropriate_user.user)
      context['currencies'] = currencies

      user_currency = {}
      ownerpk = 0

      for currency in currencies:
         user_currency[currency.currency] = currency.price
         ownerpk = currency.owner.id

      context['ownerpk'] = ownerpk

      #generate figure using matplotlib
      chart = self.get_plot(user_currency)
      context['chart'] = chart

      return context

   def get_graph(self):
      buffer = BytesIO()
      plt.savefig(buffer, format='png')
      buffer.seek(0)
      image_png = buffer.getvalue()
      graph = base64.b64encode(image_png)
      graph = graph.decode('utf-8')
      buffer.close()
      return graph

   def get_plot(self, currencies):
      plt.switch_backend('AGG')
      plt.figure(figsize=(10,10))
      plt.title('Currencies')
      courses = list(currencies.keys())
      values = list(currencies.values())
      plt.bar(courses, values)
      graph = self.get_graph()
      return graph

class SellCurrency(generic.UpdateView):
    model = Currency
    form_class = SellCurrencyForm
    template_name = 'sell_currency.html'