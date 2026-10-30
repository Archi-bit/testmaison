from django.urls import path
from .views import CategoryListView, DishListView, DishDetailView

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('dishes/', DishListView.as_view(), name='dish-list'),
    path('dishes/<slug:slug>/', DishDetailView.as_view(), name='dish-detail'),
]