from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import User
from .serializers import UserSerializer
from base.models import Tickets
from .serializers import TicketSerializer
from base.models import Chatlogs
from .serializers import ChatLogsSerializer
from base.models import Role
from .serializers import RoleSerializer


@api_view(['GET'])
def get_User(request, pk):
    users = User.objects.get(user_id=pk)
    serializer = UserSerializer(users, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def get_all_Users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def set_User(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def get_Ticket(request, pk):
    tickets = Tickets.objects.get(ticket_id=pk)
    serializer = TicketSerializer(tickets, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def get_all_Tickets(request):
    tickets = Tickets.objects.all()
    serializer = TicketSerializer(tickets, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def set_Ticket(request):
    serializer = TicketSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def get_Chat_Log(request, pk):
    chatlogs = Chatlogs.objects.get(chat_id=pk)
    serializer = ChatLogsSerializer(chatlogs, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def get_all_Chat_Logs(request):
    chatlogs = Chatlogs.objects.all()
    serializer = ChatLogsSerializer(chatlogs, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def set_Chat_Log(request):
    serializer = ChatLogsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def get_Role(request, pk):
    roles = Role.objects.get(role_id=pk)
    serializer = RoleSerializer(roles, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def get_all_Roles(request):
    roles = Role.objects.all()
    serializer = RoleSerializer(roles, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def set_Role(request):
    serializer = RoleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
