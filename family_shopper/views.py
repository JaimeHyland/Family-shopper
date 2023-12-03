from django.shortcuts import render
from .models import List_item

# Create your views here.
def get_shopping_list(request):
    list_items = List_item.objects.all()
    context = {
        'list_items': list_items
    }
    return render(request, 'family_shopper/shopping_list.html', context)

def add_item_to_list(request):
    return render(request, 'family_shopper/add_item_to_list.html')
