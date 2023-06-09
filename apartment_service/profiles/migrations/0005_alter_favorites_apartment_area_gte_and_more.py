# Generated by Django 4.2 on 2023-04-08 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_remove_serviceuser_favorites_favorites_service_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorites',
            name='apartment_area_gte',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='favorites',
            name='apartment_area_lte',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='favorites',
            name='price_gte',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='favorites',
            name='price_lte',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
