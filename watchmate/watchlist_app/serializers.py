from .models import Watchlist
from .views import *
from rest_framework import serializers
from .models import Watchlist, Streamplatform, Review


# class movieserializers(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     description = serializers.CharField()
#     active = serializers.BooleanField()
#
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
#
#     def validate_name(self, value):
#         if len(value) < 2:
#             raise serializers.ValidationError("Name is too short")
#
#         return value
#
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Name and description cannot be same")
#         else:
#             return data


class Watchlistserializers(serializers.ModelSerializer):
    class Meta:
        model = Watchlist
        fields = '__all__'
        # fields = ["name", 'active']
        # exclude = ['name','active']


class PlatformSerializers(serializers.ModelSerializer):
    watchlist = Watchlistserializers(many=True, read_only=True)

    class Meta:
        model = Streamplatform
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Review