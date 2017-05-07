from rest_framework import serializers

from .models import OutisPost


class OutisPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = OutisPost
        fields = ('id', 'category_id', 'title', 'link', 'description', 'tag', 'attraction')
