# Generated by Django 5.1.2 on 2024-11-09 04:44

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_order_last_update_by_alter_order_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='invoice_number',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), editable=False, max_digits=10),
        ),
    ]
