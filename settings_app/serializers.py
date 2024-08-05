from rest_framework import serializers
from .models import (
    SeoSettings,
    HeaderSettings,
    FooterSettings,
    FooterLinkCategory,
    FooterLink,
    SocialSettings,
    MoreTitles,
    ErrorTexts
)

class SeoSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeoSettings
        fields = '__all__'

class HeaderSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeaderSettings
        fields = '__all__'

class FooterSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterSettings
        fields = '__all__'

class FooterLinkCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterLinkCategory
        fields = '__all__'

class FooterLinkSerializer(serializers.ModelSerializer):
    category = FooterLinkCategorySerializer()  # Nested serializer

    class Meta:
        model = FooterLink
        fields = '__all__'

class SocialSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialSettings
        fields = '__all__'

class MoreTitlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoreTitles
        fields = '__all__'

class ErrorTextsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ErrorTexts
        fields = '__all__'
