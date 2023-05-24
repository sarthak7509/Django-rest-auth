from django.shortcuts import render
from rest_framework import generics,authentication,permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
# Create your views here.
from user.serializers import UserSerializer,AuthTokenSerialzer

class CreateUserView(generics.CreateAPIView):
    '''create a view for new user'''
    serializer_class=UserSerializer

class CreateTokenView(ObtainAuthToken):
    serializer_class=AuthTokenSerialzer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class ManageUserViews(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get_object(self):
        return self.request.user
