from rest_framework.response import Response
from rest_framework.decorators import api_view , permission_classes
from django.contrib.auth.models import User

@api_view(['POST'])
def create(request):
    email = request.data['email']
    password = request.data['password']
    username = request.data['username']

    print(email ,  password , username)

    if not User.objects.filter(username = username).exists():
        User.objects.create_user(
            username=username,
            password=password,
            email=email
        )

        responce_data = {
            "status_code":400,
            "message" : "successfully created account"
        }
        print(User.username)
        return Response(responce_data)
    else:
        responce_data = {
            "status_code":4001,
            "message" : "this  account already exists"
        }

        return Response(responce_data)
