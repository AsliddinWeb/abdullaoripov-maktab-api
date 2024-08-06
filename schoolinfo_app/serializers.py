from rest_framework import serializers

from .models import InfoImages, SchoolInfo, SchoolLeaders, Teachers, EducationSystem, Gallery, ApplyInfo

class InfoImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoImages
        fields = '__all__'

class SchoolInfoSerializer(serializers.ModelSerializer):
    images = InfoImagesSerializer(many=True, read_only=True)

    class Meta:
        model = SchoolInfo
        fields = '__all__'

class SchoolLeadersSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolLeaders
        fields = '__all__'

class TeachersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teachers
        fields = '__all__'

class EducationSystemSerializer(serializers.ModelSerializer):
    images = InfoImagesSerializer(many=True, read_only=True)

    class Meta:
        model = EducationSystem
        fields = '__all__'

class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'

class ApplyInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplyInfo
        fields = '__all__'
