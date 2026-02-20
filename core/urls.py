from django.urls import path
from core.views import *

app_name = 'core'

urlpatterns = [
    path('', home, name = 'home'),
    path('mac/', mac, name = 'mac'),
    path('ipad/', ipad, name = 'ipad'),
    path('iphone/', iphone, name = 'iphone'),
    path('watch/', watch, name = 'watch'),
    path('airpods/', airpods, name = 'airpods'),
    path('tv_home/', tv_home, name = 'tv_home'),
    path('accessories/', accessories, name = 'accessories'),
    path('trade_in/', trade_in, name = 'trade_in'),
    path('list/', list, name = 'list'),
    path('pay/<str:model>/<int:id>/', pay, name = 'pay'),
    path('offers/', offers, name = 'offers'),
    path('services/', services, name = 'services'),
    path('financing/', financing, name = 'financing'),
    path('warranty/', warranty, name = 'warranty'),
    path('giftcards/', giftcards, name = 'giftcards'),
    path('stores/', stores, name = 'stores'),
    path('brands/', brands, name = 'brands'),
]
