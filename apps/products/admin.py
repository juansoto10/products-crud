"""Admin"""
from django.contrib import admin
from .models import Product, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'thumbnail', 'added', 'was_added_recently')
    search_fields = ('name',)
    date_hierarchy = 'added'


class ProductAdmin(admin.ModelAdmin):

    list_display = ('name', 'slug', 'thumbnail', 'category', 'units',
                    'price', 'product_uuid', 'added', 'was_added_recently')
    list_filter = ('category',)
    search_fields = ('name', 'category__name')
    date_hierarchy = 'added'


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
