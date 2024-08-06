from rest_framework import generics, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.response import Response

from .models import SchoolInfo, SchoolLeaders, Teachers, EducationSystem, Gallery, ApplyInfo
from .serializers import (SchoolInfoSerializer, SchoolLeadersSerializer, TeachersSerializer,
                          EducationSystemSerializer, GallerySerializer, ApplyInfoSerializer)

class LastObjectView(GenericAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_last_object(self):
        return self.queryset.last() if self.queryset.exists() else None

    def get(self, request, *args, **kwargs):
        instance = self.get_last_object()
        if instance is None:
            return Response({'error': "Ma'lumot topilmadi!"}, status=HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class SchoolInfoView(LastObjectView):
    queryset = SchoolInfo.objects.all()
    serializer_class = SchoolInfoSerializer

class SchoolLeadersListView(ListAPIView):
    queryset = SchoolLeaders.objects.all()
    serializer_class = SchoolLeadersSerializer

    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

class TeachersListView(ListAPIView):
    queryset = Teachers.objects.all()
    serializer_class = TeachersSerializer

    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

class EducationSystemView(LastObjectView):
    queryset = EducationSystem.objects.all()
    serializer_class = EducationSystemSerializer

class GalleryListView(ListAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer

    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

class ApplyInfoView(LastObjectView):
    queryset = ApplyInfo.objects.all()
    serializer_class = ApplyInfoSerializer
