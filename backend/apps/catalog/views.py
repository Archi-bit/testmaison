from rest_framework import generics
from django.shortcuts import get_object_or_404
from .models import Category, Dish
from .serializers import CategorySerializer, DishListSerializer, DishDetailSerializer
from .pagination import DishPagination
from rest_framework.exceptions import ValidationError


class CategoryListView(generics.ListAPIView):
    serializer_class = CategorySerializer
    pagination_class = None

    def get_queryset(self):
        return Category.objects.filter(is_active=True).order_by("sort_order", "id")


class DishListView(generics.ListAPIView):
    serializer_class = DishListSerializer
    pagination_class = DishPagination

    def get_queryset(self):
        queryset = Dish.objects.filter(
            is_active=True, 
            category__is_active=True
        ).select_related('category').order_by('sort_order', 'id')

        # Фильтр по поиску (name__icontains)
        search_query = self.request.query_params.get('search')
        if search_query:
            queryset = queryset.filter(name__icontains=search_query)

        # Фильтр по категории (category__slug)
        category_slug = self.request.query_params.get('category')
        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)

        # Фильтр по рекомендациям (featured)
        featured_param = self.request.query_params.get('featured')
        if featured_param is not None:
            if featured_param.lower() == 'true':
                queryset = queryset.filter(is_featured=True)
            elif featured_param.lower() == 'false':
                queryset = queryset.filter(is_featured=False)
            else:
                raise ValidationError({'detail': 'Некорректное значение параметра featured. Ожидается true или false.'})

        return queryset


class DishDetailView(generics.RetrieveAPIView):
    serializer_class = DishDetailSerializer
    lookup_field = 'slug'

    def get_object(self):
        queryset = Dish.objects.filter(is_active=True, category__is_active=True).select_related('category')
        slug = self.kwargs.get(self.lookup_field)
        return get_object_or_404(queryset, slug=slug)