# Generated by Django 4.0.1 on 2024-05-08 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(null=True, upload_to='C:/Users/DELL/Downloads/Ecom/Product/image/books/'),
        ),
    ]
