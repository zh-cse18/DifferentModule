from rest_framework import serializers
from .models import MobileInfo


class MobileInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobileInfo
        fields = '__all__'



