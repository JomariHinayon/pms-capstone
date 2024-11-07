# Generated by Django 5.1.2 on 2024-11-07 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_order_product_payment_order_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='position',
            field=models.CharField(blank=True, choices=[('dean', 'Dean'), ('head', 'Head')], default='supplier', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='user_type',
            field=models.CharField(choices=[('procurement_admin', 'Procurement Admin'), ('supplier', 'Supplier'), ('user', 'User'), ('municipal_admin', 'Municipal Admin')], default='user', max_length=20),
        ),
    ]
