from rest_framework import serializers
from .models import NavType, OneNavbar, TwoNavbar, ThreeNavbar

class ThreeNavbarSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThreeNavbar
        fields = '__all__'

class TwoNavbarSerializer(serializers.ModelSerializer):
    three_navbars = ThreeNavbarSerializer(many=True, read_only=True)

    class Meta:
        model = TwoNavbar
        fields = '__all__'

class OneNavbarSerializer(serializers.ModelSerializer):
    two_navbars = TwoNavbarSerializer(many=True, read_only=True)

    class Meta:
        model = OneNavbar
        fields = '__all__'

class NavTypeSerializer(serializers.ModelSerializer):
    one_navbars = OneNavbarSerializer(many=True, read_only=True)

    class Meta:
        model = NavType
        fields = '__all__'
