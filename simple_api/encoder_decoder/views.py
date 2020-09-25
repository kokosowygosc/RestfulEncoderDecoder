from rest_framework import viewsets
from .models import Encoding, Decoding
from .serializers import EncoderSerializer, DecoderSerializer


class EncoderViewSet(viewsets.ModelViewSet):
    serializer_class = EncoderSerializer
    queryset = Encoding.objects.all()


class DecoderViewSet(viewsets.ModelViewSet):
    serializer_class = DecoderSerializer
    queryset = Decoding.objects.all()
