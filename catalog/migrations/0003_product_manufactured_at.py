# Generated by Django 5.0.2 on 2024-03-03 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_category_product_delete_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='manufactured_at',
            field=models.DateField(blank=True, null=True, verbose_name='Дата производства продукта'),
        ),
    ]