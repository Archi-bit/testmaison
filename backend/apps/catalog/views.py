from rest_framework import viewsets
from .models import Catalog
from .serializers import CatalogSerializer



class CatalogViewset(viewsets.ModelViewSet):
    model = Catalog
    serializer_class = CatalogSerializer