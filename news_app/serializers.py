from rest_framework import serializers

from .models import Category, News, NewsImage, NewsDetailText

class NewsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsImage
        fields = '__all__'

class NewsSerializer(serializers.ModelSerializer):
    images = NewsImageSerializer(many=True, read_only=True)

    class Meta:
        model = News
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    news = NewsSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = '__all__'

class NewsDetailTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsDetailText
        fields = '__all__'
