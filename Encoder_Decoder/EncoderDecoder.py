import re
import random


class Encoder:
    """
    Class to encode words from given sentence.
    Returns
    -------
    string
        Encoded text and original words which have been shuffled separated
        using '---weird---'.
    """
    def __init__(self):
        self.tokenize = re.compile(r'(\w+)', re.U)

    def shuffler(self, word):
        # shuffle given string until it differ from original one
        # first check if string consist of differ letters
        if len(set(word)) == 1:
            return word
        shuffled = ''.join(random.sample(word, len(word)))
        if shuffled != word:
            return shuffled
        else:
            return self.shuffler(word)

    def encode(self, text_to_encode):
        words = self.tokenize.split(text_to_encode)
        original_words = []
        shuffled_sentence = ""
        for word in words:
            if len(word) > 3 and len(set(word[1:-1])) != 1:
                shuffled_sentence += \
                    word[0] + self.shuffler(word[1:-1]) + word[-1]
                original_words.append(word)
            else:
                shuffled_sentence += word
        # sort words (to lower) before returning them
        original_words = sorted(original_words, key=str.lower)

        return "\n---weird---\n{}\n---weird---\n{}".format(
            shuffled_sentence, ' '.join(original_words)
        )


class Decoder:
    """
    Class to decode given encoded sentence.
    Returns
    -------
    string
        Decoded string.
    """
    def __init__(self):
        self.tokenize = re.compile(r'(\w+)', re.U)

    def decode(self, text_to_decode):
        # safe check if given parameter is encoded
        if text_to_decode.count('---weird---') != 2:
            raise ValueError("Given text is not encoded by Encoder class.")
        # divide input to encoded_text and original list of words
        encoded_text, original_words = \
            filter(None, text_to_decode.split('\n---weird---\n'))
        encoded_text = self.tokenize.split(encoded_text)
        original_words = original_words.split(' ')
        decoded_sentence = ""
        for word in encoded_text:
            # searching for encoded words
            if len(word) > 3 and len(set(word[1:-1])) != 1 and \
                    re.match(r'(\w+)', word):
                for original_word in original_words:
                    if sorted(original_word[1:-1]) == sorted(word[1:-1]):
                        decoded_sentence += original_word
                        original_words.remove(original_word)
            else:
                decoded_sentence += word
        return decoded_sentence


if __name__ == '__main__':
    stringGivenByUser = 'This is a long looong test sentence,\n' \
                        'with some big (biiiiig) words!'

    encoder = Encoder()
    decoder = Decoder()
    encoded = encoder.encode(text_to_encode=stringGivenByUser)
    decoded = decoder.decode(text_to_decode=encoded)
    print(encoded+'\n')
    print(decoded)
