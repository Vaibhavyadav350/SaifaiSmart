from rest_framework import serializers

class DocumentSerializer(serializers.Serializer):
    _id = serializers.CharField(required=False)
    name = serializers.CharField(required=False, allow_blank=True, default="")
    category = serializers.CharField(required=False, allow_blank=True, default="")
    price = serializers.CharField(required=False, allow_blank=True, default="")
    description = serializers.CharField(required=False, allow_blank=True, default="")