from django.urls import path, include
from .views import CatalogViewset
from rest_framework.routers import SimpleRouter


router = SimpleRouter
router.register('catalog', CatalogViewset, basename='catalog')

urlpatterns = [
    path('', include(router.urls)),
]
