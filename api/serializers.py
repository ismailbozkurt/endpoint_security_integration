from rest_framework import serializers
from core.models import Product


class ProductSerializer(serializers.ModelSerializer):
    fields = serializers.JSONField()
    keys = serializers.JSONField()

    class Meta:
        model = Product
        exclude = ['id']
