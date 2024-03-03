# Generated by Django 5.0.2 on 2024-03-03 20:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='наименование')),
                ('description', models.CharField(max_length=500, verbose_name='описание')),
            ],
            options={
                'verbose_name': 'наименование',
                'verbose_name_plural': 'наименования',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='наименование')),
                ('description', models.CharField(max_length=500, verbose_name='описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='students/', verbose_name='превью')),
                ('price', models.IntegerField(verbose_name='цена за покупку')),
                ('created_at', models.DateField(max_length=100, verbose_name='дата создания записи в БД')),
                ('updated_at', models.DateField(max_length=100, verbose_name='дата последнего изменения записи в БД')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.category')),
            ],
            options={
                'verbose_name': 'наименование',
                'verbose_name_plural': 'наименования',
                'ordering': ('name',),
            },
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
