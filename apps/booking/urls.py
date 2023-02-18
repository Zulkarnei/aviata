from django.contrib import admin
from django.urls import path

from apps.booking.views import ProviderAView, ProviderBView

urlpatterns = [
    path('provider-a/search/', ProviderAView.as_view()),
    path('provider-b/search/', ProviderBView.as_view()),
]
