from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import NavType, OneNavbar, TwoNavbar, ThreeNavbar
from .serializers import NavTypeSerializer, OneNavbarSerializer, TwoNavbarSerializer, ThreeNavbarSerializer

class NavTypeListView(ListAPIView):
    queryset = NavType.objects.all()
    serializer_class = NavTypeSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class NavTypeDetailView(RetrieveAPIView):
    queryset = NavType.objects.all()
    serializer_class = NavTypeSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class OneNavbarListView(ListAPIView):
    queryset = OneNavbar.objects.all()
    serializer_class = OneNavbarSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class OneNavbarDetailView(RetrieveAPIView):
    queryset = OneNavbar.objects.all()
    serializer_class = OneNavbarSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class TwoNavbarListView(ListAPIView):
    queryset = TwoNavbar.objects.all()
    serializer_class = TwoNavbarSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class TwoNavbarDetailView(RetrieveAPIView):
    queryset = TwoNavbar.objects.all()
    serializer_class = TwoNavbarSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class ThreeNavbarListView(ListAPIView):
    queryset = ThreeNavbar.objects.all()
    serializer_class = ThreeNavbarSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class ThreeNavbarDetailView(RetrieveAPIView):
    queryset = ThreeNavbar.objects.all()
    serializer_class = ThreeNavbarSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
