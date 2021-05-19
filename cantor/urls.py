from cantor.forms import SellCurrencyForm
from os import name
from django.urls import path
from .views import Account, BuyCurrency, Home, Statistic, Account, SellCurrency  #, Country
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Home, name='home'),
    #path('info/<str:ticker>/', Country, name='country'),
    path('info/<str:ticker>/', BuyCurrency.as_view(), name='country'),
    path('statistic/<int:pk>/', Statistic.as_view(), name='stats'),
    path('account/<int:pk>/', Account.as_view(), name='account'),
    path('sell_currency/<int:pk>/', SellCurrency.as_view(), name='sell_currency'),

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)