from rest_framework import serializers
from core.models import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id','title','likes','description']
        read_only_fields = ('id',)