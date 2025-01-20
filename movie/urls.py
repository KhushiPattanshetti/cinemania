from django.contrib import admin
from django.urls import path
from .views import home_view, thriller_view, comedy_view, action_view, east_asian_view, family_view, horror_view, romance_view, teen_view

urlpatterns = [
    path('', home_view, name='home'),  # Root URL
    path('home/', home_view, name='home_page'),  # URL for /home
    path('thriller/', thriller_view, name='thriller'),
    path('comedy/', comedy_view, name='comedy'),
    path('action/', action_view, name='action'),
    path('east_asian/', east_asian_view, name='east_asian'),
    path('family/', family_view, name='family'),
    path('horror/', horror_view, name='horror'),
    path('romance/', romance_view, name='romance'),
    path('teen/', teen_view, name='teen'),
]
