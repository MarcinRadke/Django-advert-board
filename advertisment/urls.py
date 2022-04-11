from unicodedata import name
from django.urls import path
from advertisment.views import *

urlpatterns = [
    path('', apiOverwiew, name="apiOverwiew"),
    
    path('offers/', offer_list, name="offers"),
    path('offers/<str:pk>/', offer_detail, name="offer_detail"),
    path('offers_create/', offer_create, name="offer_create"),
    path('offers_update/<str:pk>/', offer_update, name="offer_update"),
    path('offers_delete/<str:pk>/', offer_delete, name="offer_delete"),

    path('category/', category_list, name="category"),
    path('category_create/', category_create, name="category_create"),
    path('category_update/<str:pk>/', category_update, name="category_update"),
    path('category_delete/<str:pk>/', category_delete, name="category_delete"),
]