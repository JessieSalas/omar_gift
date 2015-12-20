import RPi.GPIO as GPIO
import time
import pygame
import random

#set up the buttons
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#set up audio playback
pygame.mixer.init()

def playAudio(filename):
    '''
    Play audio recordings on stuffed animal
    '''
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue

jojo = './media/jojo_french.mp3'
jaja = './media/jaja_spanish.mp3'
male_bark = './media/male_bark.mp3'
female_bark = './media/female_bark.mp3'
ach = './media/ach.mp3'
nooo = './media/nooo.mp3'

mario = './media/mario.mp3'
design = './media/design.mp3'
dear_darla = './media/dear_darla.mp3'
wine_bot = './media/wine_bot.mp3'
pavlov = './media/pavlov.mp3'
got = './media/got.mp3'
boss = './media/boss.mp3'
rap = './media/rap.mp3'

print('ready!')
while True:
    top_list = [jojo,jaja,male_bark,female_bark,ach,nooo] 
    bottom_list = [mario,design,dear_darla,wine_bot,pavlov,got,boss,rap]

    top_button = GPIO.input(18)
    if top_button == False:
        print('top Button Pressed')
        to_play = random.choice(top_list)
        print to_play
        playAudio(to_play)
        time.sleep(0.2)
        
    bottom_button = GPIO.input(21)
    if bottom_button == False:
        print('Bottom Button Pressed')
        to_play = random.choice(bottom_list)
        playAudio(to_play)
        time.sleep(0.2)
