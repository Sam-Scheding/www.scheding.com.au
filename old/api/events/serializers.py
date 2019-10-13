import pickle
from rest_framework import serializers
from api.events.models import Tag



class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'
