from rest_framework import serializers
from core.models import UserDocumentUpload


class MedFedSerializer(serializers.ModelSerializer):
    class Meta:
        model= UserDocumentUpload
        fields = ('name','age','dr_name','prescription','report')
