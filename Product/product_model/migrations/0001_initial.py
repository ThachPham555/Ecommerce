# Generated by Django 4.1.13 on 2024-04-12 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=10)),
                ('product_category', models.CharField(max_length=50)),
                ('product_name', models.CharField(max_length=100)),
                ('availability', models.CharField(max_length=15)),
                ('price', models.CharField(max_length=10)),
            ],
        ),
    ]
