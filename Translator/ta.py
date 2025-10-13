'''
Python Language Translator
'''
from googletrans import Translator

userinput = input("Enter: ")
Atranslator = Translator()
out = Atranslator.translate(userinput, dest="ar")

print(f"Translated: {out.text}")