# Generated by Django 3.2.8 on 2021-10-13 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(default=None, null=True)),
                ('deleted_at', models.DateTimeField(default=None, null=True)),
                ('quantity', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'baskets',
            },
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(default=None, null=True)),
                ('deleted_at', models.DateTimeField(default=None, null=True)),
            ],
            options={
                'db_table': 'wishlists',
            },
        ),
    ]
