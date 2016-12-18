from rest_framework import serializers

from crm.models import Country


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    """Countries serializer"""
    class Meta:
        model = Country
        fields = ('url', 'id', 'name', 'active', 'created_at', 'updated_at')
