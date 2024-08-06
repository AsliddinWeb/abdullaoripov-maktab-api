from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import HomeWelcome, HomeAbout, Counter, HomeLeaders, HomePartners
from .serializers import (HomeWelcomeSerializer, HomeAboutSerializer, CounterSerializer, HomeLeadersSerializer,
                          HomePartnersSerializer)

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

class HomeWelcomeView(LastObjectView):
    queryset = HomeWelcome.objects.all()
    serializer_class = HomeWelcomeSerializer
    tags = ['Home']

class HomeAboutView(LastObjectView):
    queryset = HomeAbout.objects.all()
    serializer_class = HomeAboutSerializer
    tags = ['Home']

class CounterView(LastObjectView):
    queryset = Counter.objects.all()
    serializer_class = CounterSerializer
    tags = ['Home']

class HomeLeadersListView(ListAPIView):
    queryset = HomeLeaders.objects.all()
    serializer_class = HomeLeadersSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    tags = ['Home']

class HomeLeadersDetailView(RetrieveAPIView):
    queryset = HomeLeaders.objects.all()
    serializer_class = HomeLeadersSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    tags = ['Home']

class HomePartnersListView(ListAPIView):
    queryset = HomePartners.objects.all()
    serializer_class = HomePartnersSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    tags = ['Home']
