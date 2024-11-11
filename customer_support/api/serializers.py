from rest_framework import serializers
from base.models import User
from base.models import Tickets
from base.models import Chatlogs

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tickets
        fields = '__all__'

class ChatLogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chatlogs
        fields = '__all__'