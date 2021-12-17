from rest_framework import serializers
from .models import DealershipRest

class DealershipRestSerializer(serializers.ModelSerializer):
    class Meta:
        model = DealershipRest
        fields = "__all__"
