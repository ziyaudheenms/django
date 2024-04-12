from rest_framework.serializers import ModelSerializer
from manager.models import Passwords
from rest_framework import serializers

class DisplaySerializers(ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        fields = ('id' , 'Account_Name' , 'password' , 'username', 'user' , 'created_on')
        model = Passwords


    def get_user(self , instance):
        return instance.user.username