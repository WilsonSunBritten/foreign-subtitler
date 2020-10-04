import os
from translator import Translator

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials.json"
translator = Translator()
print(translator.translate_phrase('ご機嫌はいかがですか？'))