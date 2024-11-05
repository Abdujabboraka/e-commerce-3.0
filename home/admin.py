from django.contrib import admin
from .models import Product, Category, Image, Review
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    list_editable = ['name',]
    prepopulated_fields = {'slug' : ('name',)}



class ImageInline(admin.StackedInline):
    model = Image
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'is_available', 'size']
    list_editable = ['name', 'price', 'is_available', 'size']
    inlines = [
        ImageInline
    ]

admin.site.register(Review)

