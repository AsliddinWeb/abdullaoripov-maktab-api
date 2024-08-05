from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Page
from .serializers import PageSerializer

class PageDetailView(generics.RetrieveAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    tags = ['Page']
