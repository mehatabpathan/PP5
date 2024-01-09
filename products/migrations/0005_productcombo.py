# Generated by Django 4.2 on 2024-01-09 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_remove_order_customer_remove_order_products_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCombo',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='products.product')),
                ('product_list', models.ManyToManyField(related_name='product_list', to='products.product')),
            ],
            bases=('products.product',),
        ),
    ]