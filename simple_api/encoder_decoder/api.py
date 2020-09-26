from rest_framework.routers import DefaultRouter
from simple_api.encoder_decoder.views import EncoderViewSet, DecoderViewSet

router = DefaultRouter()

router.register(r'encode', EncoderViewSet)
router.register(r'decode', DecoderViewSet)
