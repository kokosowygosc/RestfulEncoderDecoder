from rest_framework import serializers
from .models import Encoding, Decoding


class EncoderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Encoding
        fields = ('id', 'text_to_encode', 'encoded_text')


class DecoderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Decoding
        fields = ('id', 'text_to_decode', 'decoded_text')
