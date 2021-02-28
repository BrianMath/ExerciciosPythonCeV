# Ex. 021

from pygame import mixer

# Créditos da música
print("""Contains music ©2021 Joshua McLean (https://joshua-mclean.itch.io)
Licensed under Creative Commons Attribution 4.0 International""")

# Tocador da música
mixer.init()
mixer.music.load("dancing-with-the-lion.mp3")
mixer.music.play()
while mixer.music.get_busy():
    pass
