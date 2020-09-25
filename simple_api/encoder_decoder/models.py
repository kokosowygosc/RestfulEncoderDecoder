from django.db import models
from simple_api.encoder_decoder.app import Encoder, Decoder


class Encoding(models.Model):
    text_to_encode = models.CharField(max_length=200, blank=False)
    encoded_text = models.CharField(max_length=200, editable=False)

    def save(self, *args, **kwargs):
        encoder = Encoder()
        self.encoded_text = encoder.encode(
            text_to_encode=str(self).replace('\\n', '\n').rstrip()
        )
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.text_to_encode}\n {self.encoded_text}'


class Decoding(models.Model):
    text_to_decode = models.CharField(max_length=200, blank=False)
    decoded_text = models.CharField(max_length=200, editable=False)

    def save(self, *args, **kwargs):
        decoder = Decoder()
        self.decoded_text = decoder.decode(
            text_to_decode=str(self).replace('\\n', '\n').rstrip()
        )
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.text_to_decode}\n {self.decoded_text}'
