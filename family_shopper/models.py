from django.db import models


# Create your models here.
class List_item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    on_list = models.BooleanField()
    bought = models.BooleanField()

    def __str__(self):
        return self.name
