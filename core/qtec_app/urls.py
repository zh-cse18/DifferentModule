from django.urls import path
from .views import search, search_result

urlpatterns = [
    path('search/', search, name="search"),
    path('search_result/', search_result, name="search_result"),


]
