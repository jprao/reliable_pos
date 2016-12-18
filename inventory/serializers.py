from django.utils.datastructures import MultiValueDictKeyError

from rest_framework import serializers
from rest_framework.pagination import _get_count
from rest_framework.pagination import _positive_int
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.settings import api_settings

from inventory.models import (ProductCategory, TaxCategory, Tax, Location,
                              Counter)


class ProductCategorySerializer(serializers.HyperlinkedModelSerializer):
    """Category serializer"""
    class Meta:
        model = ProductCategory
        fields = ('url', 'id', 'name', 'active', 'created_at', 'updated_at')


class TaxCategorySerializer(serializers.HyperlinkedModelSerializer):
    """Tax Category serializer"""
    class Meta:
        model = TaxCategory
        fields = ('url', 'id', 'name', 'active', 'created_at', 'updated_at')


class TaxSerializer(serializers.HyperlinkedModelSerializer):
    """Tax Category serializer"""
    category = serializers.StringRelatedField(many=False)

    class Meta:
        model = Tax
        fields = ('url', 'id', 'name', 'category', 'rate', 'rate_order',
                  'active', 'created_at', 'updated_at')
        # depth = 1


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    """Location serializer"""
    class Meta:
        model = Location
        fields = ('url', 'id', 'name', 'address', 'latitude', 'longitude',
                  'active', 'created_at', 'updated_at')


class CounterSerializer(serializers.HyperlinkedModelSerializer):
    """Tax Category serializer"""
    location = serializers.StringRelatedField(many=False)

    class Meta:
        model = Counter
        fields = ('url', 'id', 'name', 'location', 'active', 'created_at',
                  'updated_at')


###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################


class DataTablesPagination(LimitOffsetPagination):
    """
    TODO: Comments based on Datatables
    A limit/offset based style. For example:

    http://api.example.org/accounts/?limit=100
    http://api.example.org/accounts/?offset=400&limit=100
    """
    default_limit = api_settings.PAGE_SIZE
    limit_query_param = 'length'
    offset_query_param = 'start'
    draw_param = 'draw'
    max_limit = None
    template = 'rest_framework/pagination/numbers.html'

    def paginate_queryset(self, queryset, request, view=None):
        self.limit = self.get_limit(request)
        if self.limit is None:
            return None

        self.offset = self.get_offset(request)
        self.count = _get_count(queryset)
        self.request = request
        if self.count > self.limit and self.template is not None:
            self.display_page_controls = True
        return list(queryset[self.offset:self.offset + self.limit])

    def get_paginated_response(self, data):
        draw = self.__get_draw_string()
        od = {}
        if draw != 0:
            od['draw'] = draw
        od['recordsTotal'] = self.count
        od['recordsFiltered'] = self.count
        od['data'] = data
        return Response(od)

    def __get_draw_string(self):
        """
        Get 'draw' param value
        """
        try:
            draw_str = self.request.query_params[self.draw_param]
        except MultiValueDictKeyError:
            return 0

        if draw_str is None:
            return 0

        return _positive_int(draw_str, strict=True, cutoff=None)
