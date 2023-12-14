from django.shortcuts import render
from django.views import generic
from .models import List_item

# Create your views here.
class ShoppingList(generic.ListView):
    model = List_item
    queryset = List_item.objects.all
    ## queryset = List_item.objects.filter(bought=False).order_by('date_created')
    context_object_name = 'list_items'
    template_name = 'index.html'
