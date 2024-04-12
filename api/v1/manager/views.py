from rest_framework.response import Response
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import AllowAny , IsAuthenticated
from manager.models import Passwords
from django.contrib.auth.models import User
from .serializers import DisplaySerializers
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def show(request):
    instance = Passwords.objects.filter(user = request.user)
    print(request.user)
    context = {
        "request" : request
    }
    serializer = DisplaySerializers(instance=instance , many=True , context = context)
    responce_data = {
        "status_code" : 4000,
        "data" : serializer.data
    }
    return Response(responce_data)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create(request):
    account = request.data['account']
    username = request.data['username']
    password = request.data['password']

    Passwords.objects.create(
        Account_Name = account,
        password = password,
        username = username,
        user = request.user,
    )

    print(username, password , account)
    responce_data = {
        "status_code" : 4001,
        "message" : "successfully saved password"
    }
    return Response(responce_data)



@api_view(['POST'])
@permission_classes([AllowAny])
def delete(request , pk):
    if Passwords.objects.filter(pk=pk).exists():

        instance = Passwords.objects.filter(pk = pk)
        instance.delete()
        
        responce_data = {
            "status_code" : 4000,
            "message" : "successfully deleted password"
        }
        return Response(responce_data)
    else:
        responce_data = {
            "status_code" : 4001,
            "message" : "cant deleted password"
        }
        return Response(responce_data)
