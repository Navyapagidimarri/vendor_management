# Generated by Django 5.0.4 on 2024-05-06 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendorapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PO_number', models.CharField(max_length=50)),
                ('vendor_reference', models.CharField(max_length=100)),
                ('order_date', models.DateField()),
                ('items', models.TextField()),
                ('quantity', models.IntegerField()),
                ('status', models.CharField(max_length=20)),
            ],
        ),
    ]
