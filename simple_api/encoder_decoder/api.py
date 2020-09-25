from rest_framework.routers import DefaultRouter
from simple_api.encoder_decoder.views import EncoderViewSet, DecoderViewSet

encoder_router = DefaultRouter()
decoder_router = DefaultRouter()

encoder_router.register(r'encode', EncoderViewSet)
decoder_router.register(r'decode', DecoderViewSet)
