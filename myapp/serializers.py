# myapp/serializers.py
from rest_framework import serializers

class DocumentSerializer(serializers.Serializer):
    _id = serializers.CharField(required=False)
    name = serializers.CharField(required=False, allow_blank=True, default="")
    category = serializers.CharField(required=False, allow_blank=True, default="")
    price = serializers.CharField(required=False, allow_blank=True, default="")
    description = serializers.CharField(required=False, allow_blank=True, default="")
    image = serializers.ImageField(max_length=None, allow_empty_file=False, use_url=True)