from rest_framework import serializers
from consolas.models import Consola
from Rol.models import Juego
from django.utils import timezone
from django.core.validators import RegexValidator
from django.contrib.auth.password_validation import validate_password
import re

# ------------------ USER SERIALIZER ------------------
class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        min_length=3,
        max_length=150,
        validators=[RegexValidator(
            regex=r'^[\w.@+-]+$',
            message="El username solo puede contener letras, números y @/./+/-/_"
        )]
    )
    password = serializers.CharField(
        write_only=True,
        min_length=8,
        error_messages={'min_length': 'La contraseña debe tener al menos 8 caracteres.'}
    )

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

    def validate_password(self, value):
        validate_password(value)  # reglas de Django
        if not re.search(r'[A-Z]', value):
            raise serializers.ValidationError("La contraseña debe tener al menos una letra mayúscula.")
        if not re.search(r'\d', value):
            raise serializers.ValidationError("La contraseña debe tener al menos un número.")
        return value

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


# ------------------ CONSOLA SERIALIZER ------------------
class ConsolaSerializer(serializers.ModelSerializer):
    anio_salida = serializers.IntegerField(min_value=1950, max_value=timezone.now().year, required=True)
    ventas_totales = serializers.IntegerField(min_value=0)
    juegos_vendidos = serializers.IntegerField(min_value=0, required=False)

    class Meta:
        model = Consola
        fields = '__all__'

    def validate_nombre(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("El nombre no puede estar vacío o solo con espacios.")
        if self.instance is None:
            if Consola.objects.filter(nombre=value).exists():
                raise serializers.ValidationError("Ya existe una consola con este nombre.")
        elif Consola.objects.filter(nombre=value).exclude(pk=self.instance.pk).exists():
            raise serializers.ValidationError("Ya existe otra consola con este nombre.")
        return value

    def validate_descripcion(self, value):
        if value.strip() and len(value.strip()) < 20:
            raise serializers.ValidationError("La descripción de la consola debe tener al menos 20 caracteres.")
        return value

    def validate_anio_salida(self, value):
        if value > timezone.now().year:
            raise serializers.ValidationError("El año de salida no puede ser mayor al actual.")
        return value

    def validate(self, data):
        ventas = data.get('ventas_totales', 0)
        juegos = data.get('juegos_vendidos', 0)
        if juegos > ventas:
            raise serializers.ValidationError("Juegos vendidos no puede ser mayor que ventas totales.")
        return data


# ------------------ JUEGO SERIALIZER ------------------
class JuegoSerializer(serializers.ModelSerializer):
    plataforma_nombre = serializers.CharField(source='plataforma.nombre', read_only=True)

    class Meta:
        model = Juego
        fields = ['id', 'nombre', 'imagen', 'descripcion', 'plataforma', 'plataforma_nombre']

    def validate_nombre(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("El nombre del juego no puede estar vacío.")
        if self.instance is None:
            if Juego.objects.filter(nombre=value).exists():
                raise serializers.ValidationError("Ya existe un juego con este nombre.")
        elif Juego.objects.filter(nombre=value).exclude(pk=self.instance.pk).exists():
            raise serializers.ValidationError("Ya existe otro juego con este nombre.")
        return value

    def validate_descripcion(self, value):
        if value.strip() and len(value.strip()) < 20:
            raise serializers.ValidationError("La descripción del juego debe tener al menos 20 caracteres.")
        return value

    def validate_imagen(self, value):
        if value:
            ext = value.name.split('.')[-1].lower()
            if ext not in ['jpg', 'jpeg', 'png']:
                raise serializers.ValidationError("Solo se permiten imágenes JPG o PNG.")
            if value.size > 2*1024*1024:  # 2MB máximo
                raise serializers.ValidationError("La imagen no puede superar 2MB.")
        return value
