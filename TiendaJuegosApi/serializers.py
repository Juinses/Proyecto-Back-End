from rest_framework import serializers
from django.contrib.auth.models import User
from consolas.models import Consola
from Rol.models import Juego 
from django.utils import timezone


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8, 
                                     error_messages={'min_length': 'La contraseña debe tener al menos 8 caracteres.'})
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True}
        } 

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Este email ya está registrado.")
        return value

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class ConsolaSerializer(serializers.ModelSerializer):
    anio_salida = serializers.IntegerField(min_value=1950, max_value=timezone.now().year, required=True)
    ventas_totales = serializers.IntegerField(min_value=0)
    
    class Meta:
        model = Consola
        fields = '__all__'
        
    def validate_nombre(self, value):
        if self.instance is None:
            if Consola.objects.filter(nombre=value).exists():
                raise serializers.ValidationError("Ya existe una consola con este nombre.")
        elif Consola.objects.filter(nombre=value).exclude(pk=self.instance.pk).exists():
            raise serializers.ValidationError("Ya existe otra consola con este nombre.")
        return value

    def validate(self, data):
        if 'descripcion' in data and len(data['descripcion']) < 20:
            raise serializers.ValidationError("La descripción de la consola debe tener al menos 20 caracteres.")
        return data


class JuegoSerializer(serializers.ModelSerializer):
    plataforma_nombre = serializers.CharField(source='plataforma.nombre', read_only=True)
    
    class Meta:
        model = Juego
        fields = ['id', 'nombre', 'imagen', 'descripcion', 'plataforma', 'plataforma_nombre'] 

    def validate_nombre(self, value):
        if self.instance is None:
            if Juego.objects.filter(nombre=value).exists():
                raise serializers.ValidationError("Ya existe un juego con este nombre.")
        elif Juego.objects.filter(nombre=value).exclude(pk=self.instance.pk).exists():
            raise serializers.ValidationError("Ya existe otro juego con este nombre.")
        return value

    def validate(self, data):
        if 'descripcion' in data and len(data['descripcion']) < 20:
            raise serializers.ValidationError("La descripción del juego debe tener al menos 20 caracteres.")
        return data
