from rest_framework import serializers

from .models import HomeWelcome, HomeAbout, Counter, HomeLeaders, HomePartners

class HomeWelcomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeWelcome
        fields = '__all__'

class HomeAboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeAbout
        fields = '__all__'

class CounterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Counter
        fields = '__all__'

class HomeLeadersSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeLeaders
        fields = '__all__'

class HomePartnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomePartners
        fields = '__all__'
