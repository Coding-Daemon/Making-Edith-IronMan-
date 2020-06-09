import playsound
from gtts import gTTS

#speech to text

text_string="your script for edith here "
tts=gTTS(text=text_string)
tts.save('edith1234.mp3')
playsound.playsound('edith1234.mp3')
print(text_string)
