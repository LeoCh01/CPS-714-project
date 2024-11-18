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
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

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

@csrf_exempt
def get_gemini_response(request):
    if request.method == 'POST':
        user_message = request.POST.get('message')
        
        # Google Gemini API Set-Up
        api_key = 'AIzaSyDdiDCw-aHgOUTGEmmLKBFEROZyRP5eM8U'
        api_url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key=AIzaSyDdiDCw-aHgOUTGEmmLKBFEROZyRP5eM8U'
        
        headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json',
        }
        
        payload = {
            'prompt': user_message,
            'model': '1.5_flash',
        }
        
        response = requests.post(api_url, headers=headers, json=payload)
        data = response.json()
        
        if response.status_code == 200:
            return JsonResponse({'response': data.get('generated_text')})
        else:
            return JsonResponse({'response': "Having trouble responding right now. Please try again later"}, status=500)

