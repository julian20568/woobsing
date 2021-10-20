from django.urls import path
from PalabrasClaves import views

urlpatterns=[
    path('palabras',views.MetPalabras),
]