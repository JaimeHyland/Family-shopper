from django.shortcuts import render

# Create your views here.
def get_shopping_list(request):
    return render(request, 'family_shopper/shopping_list.html')