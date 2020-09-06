from rest_framework import serializers
from apps.models.models import Event, Ticket
from django.contrib.auth import get_user_model, authenticate

class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    ''' Produce the full details of a user '''
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email')


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    ''' Create New User and Generate a new User Card '''
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password' : {'write_only' : True}}
    
    def create(self, validated_data, *args, **kwargs):
        user = get_user_model().objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user


# Login Serializer
class LoginSerializer(serializers.Serializer):
    ''' Log a user in and Generate a JWT '''
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials. Try again.....")
