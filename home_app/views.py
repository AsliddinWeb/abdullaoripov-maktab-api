from rest_framework import generics, status
from rest_framework.authentication import TokenAuthentication

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import HomeWelcome, HomeAbout, Counter, HomeLeaders, HomePartners
from .serializers import (HomeWelcomeSerializer, HomeAboutSerializer, CounterSerializer, HomeLeadersSerializer,
                          HomePartnersSerializer)

class LastObjectView(generics.GenericAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_last_object(self):
        return self.queryset.last() if self.queryset.exists() else None

    def get(self, request, *args, **kwargs):
        instance = self.get_last_object()
        if instance is None:
            return Response({'error': "Ma'lumot topilmadi!"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class HomeWelcomeView(LastObjectView):
    queryset = HomeWelcome.objects.all()
    serializer_class = HomeWelcomeSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    tags = ['Home']

class HomeAboutView(LastObjectView):
    queryset = HomeAbout.objects.all()
    serializer_class = HomeAboutSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    tags = ['Home']

class CounterView(LastObjectView):
    queryset = Counter.objects.all()
    serializer_class = CounterSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    tags = ['Home']

class HomeLeadersListView(generics.ListAPIView):
    queryset = HomeLeaders.objects.all()
    serializer_class = HomeLeadersSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    tags = ['Home']

class HomeLeadersDetailView(generics.RetrieveAPIView):
    queryset = HomeLeaders.objects.all()
    serializer_class = HomeLeadersSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    tags = ['Home']

class HomePartnersListView(generics.ListAPIView):
    queryset = HomePartners.objects.all()
    serializer_class = HomePartnersSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    tags = ['Home']
