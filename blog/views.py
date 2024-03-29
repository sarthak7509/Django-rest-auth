from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from blog import serializers
from core.models import  Blog


class BlogViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BlogSerializer
    queryset = Blog.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def _parms_to_id(self,qs):
        return [int(str_id) for str_id in qs.split(',')]
    def get_queryset(self):
        query_set = self.queryset
        return query_set.filter(user=self.request.user).order_by('-id')
    def get_serializer_class(self):
        if self.action=='list':
            return serializers.BlogSerializer
        return self.serializer_class
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
