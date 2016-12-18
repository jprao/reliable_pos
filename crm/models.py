"""
CRM Models
"""
from django.db import models
from master_data.models import Country


class LoyaltyCard(models.Model):
    """Loyalty Cards"""
    number = models.CharField(max_length=20, unique=True,
                              null=False, blank=False)
    active = models.BooleanField(default=True)
    issue_date = models.DateField()
    valid_to = models.DateField()
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "loyalty_cards"
        verbose_name = "LoyaltyCard"
        verbose_name_plural = "LoyaltyCards"

    def __str__(self):
        return self.number


class Customer(models.Model):
    """ Customers """
    firstname = models.CharField(max_length=80)
    lastname = models.CharField(max_length=80, null=False, blank=False)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)
    fax = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    address1 = models.CharField(max_length=80)
    address2 = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=12, null=False, blank=False)
    city = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    coutry = models.ForeignKey(Country, on_delete=models.PROTECT,
                               related_name='country')
    notes = models.TextField()
    maxdebt = models.FloatField(default=0.0)
    current_debt = models.FloatField(default=0.0)
    image = models.BinaryField()
    loyalty_card = models.ForeignKey(LoyaltyCard, on_delete=models.PROTECT,
                                     related_name='loyalty_card')

    class Meta:
        db_table = 'customers'
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def __str__(self):
        return self.name

