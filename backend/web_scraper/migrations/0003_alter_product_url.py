# Generated by Django 5.0.6 on 2024-06-06 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_scraper', '0002_rename_user_product_favorited_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='url',
            field=models.URLField(max_length=2000),
        ),
    ]