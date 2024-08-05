from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import NavType, OneNavbar, TwoNavbar, ThreeNavbar
from .serializers import NavTypeSerializer, OneNavbarSerializer, TwoNavbarSerializer, ThreeNavbarSerializer

class NavTypeListView(generics.ListAPIView):
    queryset = NavType.objects.all()
    serializer_class = NavTypeSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class NavTypeDetailView(generics.RetrieveAPIView):
    queryset = NavType.objects.all()
    serializer_class = NavTypeSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class OneNavbarListView(generics.ListAPIView):
    queryset = OneNavbar.objects.all()
    serializer_class = OneNavbarSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class OneNavbarDetailView(generics.RetrieveAPIView):
    queryset = OneNavbar.objects.all()
    serializer_class = OneNavbarSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class TwoNavbarListView(generics.ListAPIView):
    queryset = TwoNavbar.objects.all()
    serializer_class = TwoNavbarSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class TwoNavbarDetailView(generics.RetrieveAPIView):
    queryset = TwoNavbar.objects.all()
    serializer_class = TwoNavbarSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class ThreeNavbarListView(generics.ListAPIView):
    queryset = ThreeNavbar.objects.all()
    serializer_class = ThreeNavbarSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class ThreeNavbarDetailView(generics.RetrieveAPIView):
    queryset = ThreeNavbar.objects.all()
    serializer_class = ThreeNavbarSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
