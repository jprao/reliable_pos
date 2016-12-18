"""
welcome

Author: Jaya Prasad Rao. E (rao@rbtsb.com)
"""
from django.db import models


class ProductCategory(models.Model):
    """Product category"""
    name = models.CharField(max_length=50, unique=True,
                            null=False, blank=False)
    active = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "prodcut_categories"
        ordering = ["name"]
        verbose_name = "Product categories"
        verbose_name_plural = "Product Categories"

    def __str__(self):
        return self.name


class TaxCategory(models.Model):
    """Tax category"""
    name = models.CharField(max_length=50, unique=True,
                            null=False, blank=False)
    active = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "tax_categories"
        ordering = ["name"]
        verbose_name = "Tax categories"
        verbose_name_plural = "Tax Categories"

    def __str__(self):
        return self.name


class Tax(models.Model):
    """Tax category"""
    name = models.CharField(max_length=50, unique=True,
                            null=False, blank=False)
    category = models.ForeignKey(TaxCategory, on_delete=models.PROTECT,
                                 related_name='category')
    rate = models.FloatField(default=0.0)
    rate_order = models.IntegerField(default=1)
    active = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "taxes"
        ordering = ["name"]
        verbose_name = "Tax"
        verbose_name_plural = "Taxes"

    def __str__(self):
        return self.name


class Location(models.Model):
    """POS Location"""
    name = models.CharField(max_length=50, unique=True,
                            null=False, blank=False)
    address = models.TextField(max_length=1000)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    active = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "locations"
        ordering = ["name"]
        verbose_name = "Location"
        verbose_name_plural = "Locations"

    def __str__(self):
        return self.name + "-" + self.address


class Counter(models.Model):
    """POS Counter locaiton details"""
    name = models.CharField(max_length=50, unique=True,
                            null=False, blank=False)
    location = models.ForeignKey(Location, on_delete=models.PROTECT,
                                 related_name='location')
    active = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "counters"
        ordering = ["name"]
        verbose_name = "Counter"
        verbose_name_plural = "Counters"

    def __str__(self):
        return self.name

