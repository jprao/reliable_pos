from rest_framework import viewsets

from crm.models import Country
from crm.serializers import CountrySerializer


class CountryViewSet(viewsets.ModelViewSet):
    """Product categories end point"""
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
