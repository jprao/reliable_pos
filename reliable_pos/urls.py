"""reliable_pos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from inventory.views import (ProductCategoryViewSet, TaxCategoryViewSet,
                             TaxViewSet, LocationViewSet, CounterViewSet)

from crm.views import CountryViewSet
# REST Framework URLs


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'product-categories', ProductCategoryViewSet)
router.register(r'taxcategories', TaxCategoryViewSet)
router.register(r'taxes', TaxViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'counters', CounterViewSet)

router.register(r'countries', CountryViewSet)


urlpatterns = [
    # API urls
    url(r'^api/', include(router.urls)),

    # application urls
    url(r'^inventory/', include('inventory.urls')),

    # rest frame work authentcation
    url(r'^api-auth/', include('rest_framework.urls')),

    # admin app urls
    url(r'^admin/', admin.site.urls),
]