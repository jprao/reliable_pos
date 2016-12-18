from rest_framework import viewsets
from inventory.models import (ProductCategory, TaxCategory, Tax, Location,
                              Counter)
from inventory.serializers import (ProductCategorySerializer,
                                   TaxCategorySerializer,
                                   TaxSerializer, LocationSerializer,
                                   CounterSerializer)


class ProductCategoryViewSet(viewsets.ModelViewSet):
    """Product categories end point"""
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class TaxCategoryViewSet(viewsets.ModelViewSet):
    """Tax Product categories end point"""
    queryset = TaxCategory.objects.all().filter(deleted=False)
    serializer_class = TaxCategorySerializer


class TaxViewSet(viewsets.ModelViewSet):
    """Tax Product categories end point"""
    queryset = Tax.objects.all().filter(deleted=False)
    serializer_class = TaxSerializer


class LocationViewSet(viewsets.ModelViewSet):
    """Location end point"""
    queryset = Location.objects.all().filter(deleted=False)
    serializer_class = LocationSerializer


class CounterViewSet(viewsets.ModelViewSet):
    """Location end point"""
    queryset = Counter.objects.all().filter(deleted=False)
    serializer_class = CounterSerializer
