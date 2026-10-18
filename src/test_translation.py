
from deep_translator import MyMemoryTranslator

translator = MyMemoryTranslator(
    source="english",
    target="german",
)

text = "Your perfect pack for everyday use and walks in the forest."

try:
    result = translator.translate(text)
    print("Deutsch:", result)
except Exception as error:
    print("Übersetzungsfehler:", error)
