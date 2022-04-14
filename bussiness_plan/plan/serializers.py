from rest_framework import serializers
from .models import BussinessPlan , Section , Question 
from django.contrib.auth.models import User

class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model=Question
        fields=["id","question","section"]

class BussinessPlanSerializer(serializers.Serializer):
    question_id=serializers.IntegerField()
    answer=serializers.CharField();
    def validate(self, attrs):
    
        if attrs['question_id'] <= 0:
            raise serializers.ValidationError("question id  must be greather than 0");
        return attrs

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=User;
        fields=["username","password"]
    