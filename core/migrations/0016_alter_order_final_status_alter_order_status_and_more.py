# Generated by Django 5.1.2 on 2025-01-07 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_merge_0012_alter_order_status_0014_product_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='final_status',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected'), ('dispatch', 'Dispatch')], default='pending', max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected'), ('dispatch', 'Dispatch')], default='approved', max_length=20),
        ),
        migrations.AlterField(
            model_name='orderrefund',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected'), ('dispatch', 'Dispatch')], default='pending', max_length=20),
        ),
    ]
