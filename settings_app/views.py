from rest_framework import generics, permissions, status
from rest_framework.authentication import TokenAuthentication

from rest_framework.response import Response

from .models import (
    SeoSettings,
    HeaderSettings,
    FooterSettings,
    SocialSettings,
    MoreTitles,
    ErrorTexts,
    FooterLinkCategory,
    FooterLink
)
from .serializers import (
    SeoSettingsSerializer,
    HeaderSettingsSerializer,
    FooterSettingsSerializer,
    SocialSettingsSerializer,
    MoreTitlesSerializer,
    ErrorTextsSerializer,
    FooterLinkCategorySerializer,
    FooterLinkSerializer
)

class LastObjectView(generics.GenericAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_last_object(self):
        return self.queryset.last() if self.queryset.exists() else None

    def get(self, request, *args, **kwargs):
        instance = self.get_last_object()
        if instance is None:
            return Response({'error': "Sozlamalar topilmadi!"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class SeoSettingsLastView(LastObjectView):
    queryset = SeoSettings.objects.all()
    serializer_class = SeoSettingsSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    tags = ['Settings']

class HeaderSettingsLastView(LastObjectView):
    queryset = HeaderSettings.objects.all()
    serializer_class = HeaderSettingsSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    tags = ['Settings']

class FooterSettingsLastView(LastObjectView):
    queryset = FooterSettings.objects.all()
    serializer_class = FooterSettingsSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    tags = ['Settings']

class MoreTitlesLastView(LastObjectView):
    queryset = MoreTitles.objects.all()
    serializer_class = MoreTitlesSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    tags = ['Settings']

class ErrorTextsLastView(LastObjectView):
    queryset = ErrorTexts.objects.all()
    serializer_class = ErrorTextsSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    tags = ['Settings']

class SocialSettingsLastView(generics.ListAPIView):
    queryset = SocialSettings.objects.all()
    serializer_class = SocialSettingsSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    tags = ['Settings']

class FooterLinkCategoryListView(generics.ListAPIView):
    queryset = FooterLinkCategory.objects.all()
    serializer_class = FooterLinkCategorySerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    tags = ['Settings']

class FooterLinkListView(generics.ListAPIView):
    queryset = FooterLink.objects.all()
    serializer_class = FooterLinkSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    tags = ['Settings']
