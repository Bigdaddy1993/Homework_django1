from django.db import models

from users.models import User

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
    image = models.ImageField(upload_to='product/', verbose_name='превью', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена за покупку')
    created_at = models.DateField(max_length=100, verbose_name='дата создания записи в БД')
    updated_at = models.DateField(max_length=100, verbose_name='дата последнего изменения записи в БД')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='владелец', **NULLABLE)
    is_published = models.BooleanField(default=False, verbose_name='статус публикации')

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'продукты'
        verbose_name_plural = 'продукт'
        ordering = ('name',)

        permissions = [
            ('set_published',
             'Can publish posts'),
            ('set_description',
             'Can change description'),
            ('set_category',
             'Can change category')
        ]


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    version_number = models.CharField(max_length=50, verbose_name='номер версии')
    version_name = models.CharField(max_length=50, verbose_name='название версии')
    is_active = models.BooleanField(default=True, verbose_name='Текущая версия')

    def __str__(self):
        return f'{self.product} {self.version_number}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
