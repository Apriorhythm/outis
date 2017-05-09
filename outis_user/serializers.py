from rest_framework import serializers

from .models import OutisUser


class OutisUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = OutisUser
        fields = ('id', 'username', 'logo', 'signature')
