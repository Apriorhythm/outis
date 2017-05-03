from rest_framework import serializers

from .models import OutisPost


class OutisPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = OutisPost
        fields = ('category_id', 'title', 'link', 'description', 'tag', 'attraction')