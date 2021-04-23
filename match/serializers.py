from rest_framework import serializers
from .models import Match
from human.serializers import HumanSerializer


class MatchSerializer(serializers.ModelSerializer):
    human = HumanSerializer(read_only=True)
    
    class Meta:
        model = Match
        fields = ['id', 'first_name', 'second_name', 'age', 'gender', 'human']


class MatchDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Match
        fields = ['id', 'first_name', 'second_name', 'age', 'gender']