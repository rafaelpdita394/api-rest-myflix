from rest_framework import viewsets, generics
from myflix.models import user, stream, lista
from myflix.serializers import userSerializers, streamSerializers, listaSerializers

class userViewSet(viewsets.ModelViewSet):
    queryset = user.objects.all()
    serializer_class = userSerializers

class streamViewSet(viewsets.ModelViewSet):
    queryset = stream.objects.all()
    serializer_class = streamSerializers

class listaViewSet(viewsets.ModelViewSet):
    queryset = lista.objects.all()
    serializer_class = listaSerializers

class listaUser(generics.ListAPIView):
    def get_queryset(self):
        queryset = lista.objects.filter(user_id=self.kwargs['pk'])
        return queryset
    serializer_class = listaSerializers

class listaStream(generics.ListAPIView):
    def get_queryset(self):
        queryset = lista.objects.filter(stream_id=self.kwargs['pk'])
        return queryset
    
    serializer_class = listaSerializers



