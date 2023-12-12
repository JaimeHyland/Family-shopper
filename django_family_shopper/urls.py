from django.contrib import admin
from django.urls import path, include
# Import ShoppingList if you need it, but it's not used in the urlpatterns below.

urlpatterns = [
    path('admin/', admin.site.urls),
    # Use the correct import path for the family_shopper URLs.
    path('', include('family_shopper.urls'), name='shopper.urls')
]
