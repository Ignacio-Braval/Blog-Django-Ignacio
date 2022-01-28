from rest_framework import serializers
from users.models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        # Estos son los campos que se pediran para crear a un usuario
        model = User
        fields = ['id', 'email', 'username', 'password']

    def create(self, validated_data):
        # Estas lineas de codigo ayudan a encriptar la password
        # que el usuario crea.
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    # Esta clase ayuda a obtener los datos del mismo usuario
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'first_name', 'last_name']

class UserUpdateSerializer(serializers.ModelSerializer):
    # Esta ayuda a actualizar los datos del usuario solo (first_name y last_name)
    class Meta:
        model = User
        fields = ['first_name', 'last_name']
