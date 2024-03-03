from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.CharField(max_length=500, verbose_name='описание')

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'категории'
        verbose_name_plural = 'категорий'
        ordering = ('name',)


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.CharField(max_length=500, verbose_name='описание')
    image = models.ImageField(upload_to='students/', verbose_name='превью', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена за покупку')
    created_at = models.DateField(max_length=100, verbose_name='дата создания записи в БД')
    updated_at = models.DateField(max_length=100, verbose_name='дата последнего изменения записи в БД')

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'продукты'
        verbose_name_plural = 'продукт'
        ordering = ('name',)
