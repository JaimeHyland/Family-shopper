from . import views
from django.urls import path

urlpatterns = [
    path('', views.ShoppingList.as_view(), name='home')
]