from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from medfed import serializers
from core.models import UserDocumentUpload

class MedFed(viewsets.ModelViewSet):
    serializer_class = serializers.MedFedSerializer
    queryset = UserDocumentUpload.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def _parms_to_id(self,qs):
        return [int(str_id) for str_id in qs.split(',')]
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by('-id')
    def perform_create(self, serializer):
        return serializer.save(user = self.request.user)