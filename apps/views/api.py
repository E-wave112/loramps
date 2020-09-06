from django.shortcuts import HttpResponse
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from knox.models import AuthToken

from .serializers import (
    EventSerializer, TicketSerializer,
    RegisterSerializer, LoginSerializer, UserSerializer,
    Event, Ticket
)

def index(request):
    return HttpResponse('Hello From the Home Route')

# Create your views here

class EventsAPI(generics.ListCreateAPIView):
    name = 'All Events'
    serializer_class = EventSerializer
    queryset = Event.objects.all()



# Register API
class RegisterAPI(generics.GenericAPIView):
    ''' Register The User '''
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            'user' : RegisterSerializer(user, context=self.get_serializer_context()).data ,
            'token' : AuthToken.objects.create(user)[1]
        })


# Login API
class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            'user' : UserSerializer(user, context=self.get_serializer_context()).data,
            'token' : AuthToken.objects.create(user)[1]
        })


# User API
class UserAPI(generics.RetrieveAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user