# Generated by Django 5.1.2 on 2024-11-07 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_account_address_alter_account_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='business_permit',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
