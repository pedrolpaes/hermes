from rest_framework import serializers
from users.models import Usuario


class CriarUsuarioSerializer(serializers.ModelSerializer):
    """
    Currently unused in preference of the below.
    """
    #email = serializers.EmailField(required=True)
    #user_name = serializers.CharField(required=True)
    #password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = Usuario
        fields = ('email', 'user_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # as long as the fields are the same, we can just use this
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class ListUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['email', 'user_name', 'nome', 'sobrenome', 'bio', 'genero', 'cpf', 'data_nascimento', 'cep', 'cidade', 'estado', 'is_staff', 'is_active', 'date_joined', 'last_login']
