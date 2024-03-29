# Generated by Django 4.1 on 2023-08-01 00:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0002_rename_price_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('address2', models.CharField(max_length=200)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.cart')),
            ],
        ),
    ]
