"""Models"""
import datetime
import uuid

from django.db import models
from django.utils import timezone
from django.contrib import admin


class Category(models.Model):

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=50,
                            unique=True)
    thumbnail = models.CharField(max_length=100)
    added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    @admin.display(
        boolean=True,
        ordering='added',
        description='Added recently?',
    )
    def was_added_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.added <= now


class Product(models.Model):

    product_uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    thumbnail = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    units = models.PositiveIntegerField()
    price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    @admin.display(
        boolean=True,
        ordering='added',
        description='Added recently?',
    )
    def was_added_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.added <= now
