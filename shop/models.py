from django.db import models
from django.core.validators import MinValueValidator

class Category(models.Model):
    """Модель Категория товара"""
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")

    def __str__(self):
        return self.name

class Manufacturer(models.Model):
    """Модель Производитель"""
    name = models.CharField(max_length=100, verbose_name="Название")
    country = models.CharField(max_length=100, verbose_name="Страна")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")

    def __str__(self):
        return self.name

class Product(models.Model):
    """Модель Товар"""
    name = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    product_image = models.ImageField(upload_to='products/', verbose_name="Фото товара")
    
    # Валидация: цена не может быть меньше 0
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        validators=[MinValueValidator(0)],
        verbose_name="Цена"
    )
    
    # Валидация: количество не может быть меньше 0
    stock_quantity = models.IntegerField(
        validators=[MinValueValidator(0)],
        verbose_name="Количество на складе"
    )

    # Связи ForeignKey с каскадным удалением
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE, 
        verbose_name="Категория"
    )
    manufacturer = models.ForeignKey(
        Manufacturer, 
        on_delete=models.CASCADE, 
        verbose_name="Производитель"
    )

    def __str__(self):
        return self.name
