from rest_framework import serializers
from .models import Catalog



class CatalogSerializer(serializers.ModelSerializer):
    model = Catalog
    fields = ('title',)