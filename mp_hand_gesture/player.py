import pygame
import threading
import time

def play(mp3):
    pygame.mixer.init()
    pygame.mixer.music.load(mp3)
    pygame.mixer.music.play()
    time.sleep(2)
    pygame.mixer.music.stop()



def go(a):
    thread = threading.Thread(target= play , args=(a,))
    thread.start()


