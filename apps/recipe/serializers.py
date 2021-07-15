from rest_framework import serializers
from apps.core.models import Tag, Ingredient


class TagSerializer(serializers.ModelSerializer):
    """Serializer for tag serializer"""

    class Meta:
        model = Tag
        fields = ('id', 'name')
        read_only_fields = ('id',)


class IngredientSerializer(serializers.ModelSerializer):
    """Serializer for ingredient serializer"""

    class Meta:
        model = Ingredient
        fields = ('id', 'name')
        read_only_fields = ('id',)
