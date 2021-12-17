from rest_framework import serializers
from .models import DealershipRest, ReviewRest

class DealershipRestSerializer(serializers.ModelSerializer):
    class Meta:
        model = DealershipRest
        fields = "__all__"

class ReviewRestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewRest
        fields = "__all__"
