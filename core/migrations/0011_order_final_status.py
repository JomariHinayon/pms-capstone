# Generated by Django 5.1.2 on 2024-11-09 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_order_invoice_number_order_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='final_status',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=20),
        ),
    ]
