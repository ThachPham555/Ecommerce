# Generated by Django 4.0.1 on 2024-04-25 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('des', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('publisher', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='image/mobiles/')),
                ('price', models.FloatField()),
                ('sale', models.FloatField()),
                ('type', models.CharField(default='mobile', max_length=50)),
                ('quantity', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('des', models.TextField(null=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mobiles.brand')),
            ],
        ),
    ]
