from gtts import *
import os

print("Please Be patience it will took  few second  to open in your system")

Text = """जन गण मन अधिनायक जय हे
भारत भाग्य विधाता।

पंजाब सिन्ध गुजरात मराठा
द्रविड़ उत्कल बंग।
विंध्य हिमाचल यमुना गंगा
उच्छल जलधि तरंग।

तव शुभ नामे जागे
तव शुभ आशीष मागे।

गाहे तव जयगाथा।

जन गण मंगलदायक जय हे
भारत भाग्य विधाता।

जय हे, जय हे, जय हे
जय जय जय जय हे॥ 

Thank you for your Patience"""

language = 'hi'  # hindi

# gTTS() take few argument main is TEXT to read, language (by default=en),slow means slow thn True fast than make it
# false
speech = gTTS(text=Text, lang=language, slow=False)
speech.save("document\\Speech.mp3")  # .save() for save file
os.system("document\\Speech.mp3")  # os.system() to start play

# Language Code list link: https://developers.google.com/admin-sdk/directory/v1/languages
