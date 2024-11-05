from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='nomi')
    slug = models.SlugField(max_length=100, unique=True)
    photo = models.ImageField(upload_to='Category-photos/', null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, verbose_name='sub-category')

    def __str__(self):
        if self.parent:
            return f"Sub: {self.name}"
        return self.name

    class Meta:
        verbose_name = 'Toifa'
        verbose_name_plural = 'Toifalar'



class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='nomi')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='narxi')
    is_available = models.BooleanField(verbose_name='bormi')
    size = models.PositiveIntegerField(verbose_name='olchami')
    description = models.TextField(verbose_name='xaqida')
    card_details = models.TextField(verbose_name='card-details')
    shipping = models.TextField(verbose_name='shipping')

    def get_image(self):
        first_image = self.image_set.first()
        return first_image.image.url if first_image else None

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Maxsulot'
        verbose_name_plural = 'Maxsulotlar'


class Image(models.Model):
    image = models.ImageField(upload_to='Product-images/', verbose_name='Rasmi')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Mahsulot')

    def __str__(self):
        return f"{self.product.name} | {self.image.name}"

    class Meta:
        verbose_name = 'Rasm'
        verbose_name_plural = 'Rasmlar'



class Review(models.Model):
    rate = models.IntegerField(validators=[
        MinValueValidator(1, "eng kam baho 1"),
        MaxValueValidator(5, "eng ko'p baho 5")
    ])
    content = models.CharField(max_length=200, verbose_name='Matn')
    author = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='avtor')
    address = models.CharField(max_length=200, verbose_name='manzil', null=True, blank=True)
    author_photo = models.ImageField(upload_to='user-avatar/', null=True, blank=True, verbose_name='avatar')


    def __str__(self):
        return f"{self.author}'s review "


    class Meta:
        verbose_name = 'Sharx'
        verbose_name_plural = 'Sharxlar'







