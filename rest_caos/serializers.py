from rest_framework import serializers
from caosnews.models import *

class cortaSerializers(serializers.ModelSerializer):
    class Meta:
        model = corta
        fields = '__all__'
class caosSerializers(serializers.ModelSerializer):
    class Meta:
        model = caosnews
        fields = ('nombre_caosnews','apellido_caosnews','correo_caosnews','rut')