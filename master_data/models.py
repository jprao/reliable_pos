"""
Master data Models
"""
from django.db import models


class Country(models.Model):
    """Countries"""
    name = models.CharField(max_length=50, unique=True,
                            null=False, blank=False)
    active = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "countries"
        ordering = ["name"]
        verbose_name = "Country"
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.name
