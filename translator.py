import googletrans

class Translator:
    def __init__(self):
        self.translator = googletrans.Translator()

    def translate_phrase(self, phrase_to_translate: str) -> str:
        return self.translator.translate(phrase_to_translate).text
