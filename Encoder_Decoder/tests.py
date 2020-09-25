import unittest
from EncoderDecoder import Encoder, Decoder


class TestEncoder(unittest.TestCase):
    def setUp(self):
        self.encoder = Encoder()

    def test_shuffler_if_word_has_same_characters(self):
        """
        Test that shuffler is returning same string if it consist with same characters
        """
        result = self.encoder.shuffler('iiiii')
        self.assertEqual(result, 'iiiii')

    def test_shuffler_if_word_has_differ_characters(self):
        """
        Test that shuffler is returning differ string
        """
        result = self.encoder.shuffler('sentence')
        self.assertNotEqual(result, 'sentence')

    def test_shuffler_if_word_has_2_characters(self):
        """
        Test that shuffler is returning differ string
        """
        result = self.encoder.shuffler('is')
        self.assertEqual(result, 'si')

    def test_encoder_is_returning_encoded_value(self):
        """
        Test that encoder is giving 'magic' word inside returned value
        """
        result = self.encoder.encode(text_to_encode='Sentence without punctuation marks')
        self.assertIn('---weird---', result)

    def test_bad_type_returned(self):
        """
        Test that method encode return TypeError when they get wrong type of parameter
        """
        value = ['Simple sentence']
        with self.assertRaises(TypeError):
            self.encoder.encode(text_to_encode=value)


class TestDecoder(unittest.TestCase):
    def setUp(self):
        self.decoder = Decoder()

    def test_decoder_returning_valid_values(self):
        """
        Test that decoder is returning valid decoded sentences
        """
        result = self.decoder.decode(text_to_decode='\n---weird---\nSenetcne wtih nrbmeus 0 23 2 and spciael '
                                                    'cterahacrs []*# $\n---weird---\ncharacters numbers Sentence '
                                                    'special with')
        self.assertEqual(result, 'Sentence with numbers 0 23 2 and special characters []*# $')

    def test_decoder_returning_valid_values_for_single_word(self):
        """
        Test that decoder is returning valid decoded sentences
        """
        result = self.decoder.decode(text_to_decode='\n---weird---\nTihs\n---weird---\nThis')
        self.assertEqual(result, 'This')

    def test_bad_type_returned(self):
        """
        Test that method decode return ValueError when they get magic '---weird---' symbol
        """
        value = 'Tihs is a lnog loonog tset sectenne'
        with self.assertRaises(ValueError):
            self.decoder.decode(text_to_decode=value)


class TestEncoderWorkingWithDecoder(unittest.TestCase):
    def setUp(self):
        self.encoder = Encoder()
        self.decoder = Decoder()

    def test_decoder_returning_valid_values(self):
        """
        Test that values given to encoder and returned by decoder are the same
        """
        value = 'This is a long looong test sentence,\nwith some big (biiiiig) words!'
        encoding_result = self.encoder.encode(text_to_encode=value)
        decoding_result = self.decoder.decode(text_to_decode=encoding_result)
        self.assertEqual(value, decoding_result)

    def test_pipeline_decoder_coder(self):
        """
        Test pipeline encoder->decoder->encoder->decoder and check value
        """
        value = 'This is a long looong test sentence,\nwith some big (biiiiig) words!'
        encoding_result = self.encoder.encode(text_to_encode=value)
        decoding_result = self.decoder.decode(text_to_decode=encoding_result)
        encoding_result = self.encoder.encode(text_to_encode=decoding_result)
        decoding_result = self.decoder.decode(text_to_decode=encoding_result)
        self.assertEqual(value, decoding_result)


if __name__ == '__main__':
    unittest.main()
