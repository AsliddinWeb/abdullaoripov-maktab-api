from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from .models import Category, News, NewsDetailText
from .serializers import CategorySerializer, NewsSerializer, NewsDetailTextSerializer

# Pagination
from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 9
    page_size_query_param = 'page_size'
    max_page_size = 100

class LastObjectView(generics.GenericAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_last_object(self):
        return self.queryset.last() if self.queryset.exists() else None

    def get(self, request, *args, **kwargs):
        instance = self.get_last_object()
        if instance is None:
            return Response({'error': "Ma'lumot topilmadi!"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    tags = ['News']

class NewsListView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = StandardResultsSetPagination
    tags = ['News']

class NewsCategoryView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        news = News.objects.filter(category=category)

        paginator = StandardResultsSetPagination()
        paginated_news = paginator.paginate_queryset(news, request)

        serializer = NewsSerializer(paginated_news, many=True)

        return paginator.get_paginated_response(serializer.data)

class NewsDetailView(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    tags = ['News']


class NewsDetailTextView(LastObjectView):
    queryset = NewsDetailText.objects.all()
    serializer_class = NewsDetailTextSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    tags = ['News']
