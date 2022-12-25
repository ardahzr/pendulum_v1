import pygame
import math
from pygame import mixer

mixer.init()
sound1 = pygame.mixer.Sound('sound1.wav')
sound1.set_volume(0.5)
sound2 = pygame.mixer.Sound('sound2.wav')
sound2.set_volume(0.5)
sound3 = pygame.mixer.Sound('sound3.wav')
sound3.set_volume(0.5)
sound4 = pygame.mixer.Sound('sound4.wav')
sound4.set_volume(0.5)
sound5 = pygame.mixer.Sound('sound5.wav')
sound5.set_volume(0.5)
sound6 = pygame.mixer.Sound('sound6.wav')
sound6.set_volume(0.5)
sound7 = pygame.mixer.Sound('sound7.wav')
sound7.set_volume(0.5)
channel1 = pygame.mixer.Channel(1)
channel2 = pygame.mixer.Channel(2)
channel3 = pygame.mixer.Channel(3)
channel4 = pygame.mixer.Channel(4)
channel5 = pygame.mixer.Channel(5)
channel6 = pygame.mixer.Channel(6)
channel7 = pygame.mixer.Channel(7)

pygame.init()
dis = pygame.display.set_mode((960,960))
pygame.display.set_caption("Animation by Libuntu")
black = (0,0,0)
white = (255,255,255)
r1=250
g1=0
b1=125
r_change = 1
g_change = 1
b_change = 1

omega = 0.1
omega2 = 0.11
omega3 = 0.12
omega4 = 0.13
omega5 = 0.14
omega6 = 0.15
omega7 = 0.16
angle = 0
angle2 = 0
angle3 = 0
angle4 = 0
angle5 = 0
angle6 = 0
angle7 = 0
radius = 370
dt = 0.05

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT: 
            pygame.quit() 
            quit()
    dis.fill(black)

    angle += omega * dt
    angle2 += omega2 * dt
    angle3 += omega3 * dt
    angle4 += omega4 * dt
    angle5 += omega5 * dt
    angle6 += omega6 * dt
    angle7 += omega7 * dt

    x1 = radius * math.cos(angle) + 480
    y1 = radius * math.sin(angle) + 480
    x2 = 320 * math.cos(angle2) + 480
    y2 = 320 * math.sin(angle2) + 480
    x3 = 270 * math.cos(angle3) + 480
    y3 = 270 * math.sin(angle3) + 480
    x4 = 220 * math.cos(angle4) + 480
    y4 = 220 * math.sin(angle4) + 480
    x5 = 170 * math.cos(angle5) + 480
    y5 = 170 * math.sin(angle5) + 480
    x6 = 120 * math.cos(angle6) + 480
    y6 = 120 * math.sin(angle6) + 480
    x7 = 70 * math.cos(angle7) + 480
    y7 = 70 * math.sin(angle7) + 480
    if 450 <= x1 <= 455:
        if 0 <= y1 <= 480:
            omega = -0.1 
            channel7.play(sound7) 
    if 505 <= x1 <= 510:
        if 0 <= y1 <= 480:
            omega = 0.1 
            channel7.play(sound7)
    if 450 <= x2 <= 455:
        if 0 <= y2 <= 480:
            omega2 = -0.11
            channel6.play(sound6) 
    if 505 <= x2 <= 510:
        if 0 <= y2 <= 480:
            omega2 = 0.11 
            channel6.play(sound6)
    if 505 <= x3 <= 510:
        if 0 <= y3 <= 480:
            omega3 = 0.12 
            channel5.play(sound5)
    if 450 <= x3 <= 455:
        if 0 <= y3 <= 480:
            omega3 = -0.12 
            channel5.play(sound5)
    if 450 <= x4 <= 455:
        if 0 <= y4 <= 480:
            omega4 = -0.13
            channel4.play(sound4)
    if 505 <= x4 <= 510:
        if 0 <= y4 <= 480:
            omega4 = 0.13
            channel4.play(sound4)
    if 450 <= x5 <= 455:
        if 0 <= y5 <= 480:
            omega5 = -0.14
            channel3.play(sound3)
    if 505 <= x5 <= 510:
        if 0 <= y5 <= 480:
            omega5 = 0.14
            channel3.play(sound3)
    if 450 <= x6 <= 455:
        if 0 <= y6 <= 480:
            omega6 = -0.15
            channel2.play(sound2)
    if 505 <= x6 <= 510:
        if 0 <= y6 <= 480:
            omega6 = 0.15
            channel2.play(sound2)
    if 450 <= x7 <= 455:
        if 0 <= y7 <= 480:
            omega7 = -0.16
            channel1.play(sound1)
    if 505 <= x7 <= 510:
        if 0 <= y7 <= 480:
            omega7 = 0.16
            channel1.play(sound1)
            
    pygame.draw.line(dis,white,[480,80],[480,480],5)        
    pygame.draw.circle(dis,(255,255,255),[480,480], 400, 4)
    pygame.draw.circle(dis,(r1,g1,b1),[x1,y1], 25, 0)
    pygame.draw.circle(dis,(r1,g1,b1),[x2,y2], 25, 0)
    pygame.draw.circle(dis,(r1,g1,b1),[x3,y3], 25, 0)
    pygame.draw.circle(dis,(r1,g1,b1),[x4,y4], 25, 0)
    pygame.draw.circle(dis,(r1,g1,b1),[x5,y5], 25, 0)
    pygame.draw.circle(dis,(r1,g1,b1),[x6,y6], 25, 0)
    pygame.draw.circle(dis,(r1,g1,b1),[x7,y7], 25, 0)
    pygame.draw.line(dis,(r1,g1,b1),[x1,y1],[480,480],3)
    pygame.draw.line(dis,(r1,g1,b1),[x2,y2],[480,480],3)
    pygame.draw.line(dis,(r1,g1,b1),[x3,y3],[480,480],3)
    pygame.draw.line(dis,(r1,g1,b1),[x4,y4],[480,480],3)
    pygame.draw.line(dis,(r1,g1,b1),[x5,y5],[480,480],3)
    pygame.draw.line(dis,(r1,g1,b1),[x6,y6],[480,480],3)
    pygame.draw.line(dis,(r1,g1,b1),[x7,y7],[480,480],3)

    r1 = r1 + r_change
    g1 = g1 + g_change
    b1 = b1 + b_change
    if r1 == 254:
        r_change = -1
    if g1 == 254:
        g_change = -1
    if b1 == 254:
        b_change = -1
    if r1 == 0:
        r_change = 1
    if g1 == 0:
        g_change = 1
    if b1 == 0:
        b_change = 1

    pygame.time.Clock().tick(200)
    pygame.display.update()
    
