# Generated by Django 3.2.23 on 2023-12-14 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('family_shopper', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list_item',
            name='buyer_notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='list_item',
            name='creator_notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='list_item',
            name='shop_bought',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shop_where_item_bought', to='family_shopper.shop'),
        ),
    ]
