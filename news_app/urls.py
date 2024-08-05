from django.urls import path

from .views import CategoryListView, NewsListView, NewsDetailView, NewsDetailTextView, NewsCategoryView

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', NewsCategoryView.as_view(), name='news-category-list'),
    path('all/', NewsListView.as_view(), name='news-list'),
    path('detail/<int:pk>/', NewsDetailView.as_view(), name='news-detail'),
    path('detail-text/', NewsDetailTextView.as_view(), name='news-detail-text-last'),
]
