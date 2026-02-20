from django.urls import path
from accounts.views import *
from django.contrib.auth.views import LogoutView
app_name = 'accounts'

urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('profile/', profile, name = 'profile'),

    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]