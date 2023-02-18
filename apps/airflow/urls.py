from django.contrib import admin
from django.urls import path

from apps.airflow.views import AirflowSearchView, get_results
urlpatterns = [
    path('search/', AirflowSearchView.as_view()),
    path('results/<str:search_id>/<str:currency>/', get_results),
]
