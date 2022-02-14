from rest_framework import serializers
from .models import Players,Teams

class PlayersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Players
        exclude=['pic']
