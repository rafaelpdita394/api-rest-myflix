from rest_framework import serializers
from myflix.models import user, stream, lista


class userSerializers(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ['id', 'nome', 'email', 'cpf', 'data_nascimento', 'celular']

class streamSerializers(serializers.ModelSerializer):
    class Meta:
        model = stream
        fields = ['id', 'codigo', 'descricao', 'categoria']

class listaSerializers(serializers.ModelSerializer):
    class Meta:
        model = lista
        exclude = []

class listaUserSerializer():
    stream = serializers.ReadOnlyField(source='stream.descricao')

    class Meta:
        model = lista
        fields = ['stream']
    
    def get_categoria(self, obj):
        return obj.stream.get_categoria_display()

class listaStreamSerializes():
    user_nome = serializers.ReadOnlyField(source='user.nome')

    class Meta:
        model = lista
        fields = ['user_nome']



