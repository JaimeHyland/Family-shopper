from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Shop(models.Model):
    shop_name = models.CharField(max_length=50, null=False, blank=False)
    creator_id = models.ForeignKey(User, on_delete=models.PROTECT, related_name = "user_who_created_shop")
    featured_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.shop_name

class Category(models.Model):
    category_name = models.CharField(max_length=50, null=False, blank=False)
    creator_id = models.ForeignKey(User, on_delete=models.PROTECT, related_name="user_who_created_category")
    featured_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_name = models.CharField(max_length=50, null=False, blank=False)
    default_quantity = models.IntegerField()
    default_unit = models.CharField(max_length=10)
    default_shop = models.ForeignKey(Shop, on_delete=models.PROTECT, related_name="default_where_to_buy")
    creator_id = models.ForeignKey(User, on_delete=models.PROTECT, related_name="user_who_created_product")

    def __str__(self):
        return self.product_name


class List_item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    product_id = models.ForeignKey(Product, on_delete=models.PROTECT, related_name="product_of_list_item")
    date_created = models.DateTimeField(auto_now=True)
    bought = models.BooleanField(default=False)
    date_bought = models.DateTimeField(default=None, blank=True, null=True)
    shopper_id = models.ForeignKey(Product, on_delete=models.PROTECT, related_name="user_who_bought_item")
    quantity_required = models.IntegerField(default=1)
    quantity_bought = models.IntegerField(default=1)
    shop_bought = models.ForeignKey(Shop, on_delete=models.PROTECT, related_name="shop_where_item_bought")
    creator_notes = models.TextField(default='Notes added by creator')
    buyer_notes = models.TextField(default='Notes added by buyer')

    class Meta:
        ordering = ['date_created']

    def __str__(self):
        return self.name




