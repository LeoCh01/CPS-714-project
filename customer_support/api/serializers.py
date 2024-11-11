from rest_framework import serializers
from base2.models import User
from base2.models import Tickets
from base2.models import Chatlogs
from base2.models import Role

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

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'