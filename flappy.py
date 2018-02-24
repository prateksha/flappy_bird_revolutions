import pygame,sys
from pygame.locals import *
from bird import Bird
from pipe import Pipe
import math

FPS = 60
SCREENW = 1280
SCREENH = 720
BG = pygame.image.load('images/background.png')
WS = pygame.image.load('images/start_screen.png')

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS',100)
myfont2 = pygame.font.SysFont('AngryBirds',75)

score = 0

def welcomeScreen():
    WSCREEN = pygame.display.set_mode((SCREENW,SCREENH))
    pygame.display.set_caption('Flappy Bird: Revolutions')
    while True:
        pygame.init()
        WSCREEN.blit(WS,(0,0))
        start_button = pygame.draw.rect(WSCREEN,(255,255,200),(600,250,300,100),0)
        start = myfont2.render("START",True,(0,0,0))
        WSCREEN.blit(start,(650,265))
        mpos = pygame.mouse.get_pos()
        if 600 < mpos[0] < 600 + 300 and 250 < mpos[1] < 250 + 100:
            pygame.draw.rect(WSCREEN,(0,250,154),(600,250,300,100))
            WSCREEN.blit(start,(650,265))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if 600 <mpos[0] < 600 + 300 and 250 < mpos[1] < 250 + 100:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    WSCREEN.blit(BG,(0,0))
                    pygame.display.update()
                    pygame.time.wait(400)
                    main()
        pygame.display.update()

def gameOver():
    ESCREEN  = pygame.display.set_mode((SCREENW,SCREENH))
    pygame.display.set_caption("Flappy Bird: Revolutions")
    while True:
        pygame.init()
        ESCREEN.blit(BG,(0,0))
        end = myfont2.render("GAME OVER!",True,(7,54,66))
        ESCREEN.blit(end,(440,200))
        message = myfont.render(str(score),True,(255,255,255))
        if score > 9:
            ESCREEN.blit(message,(610,330))
        else:
            ESCREEN.blit(message,(622.5,330))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            keyspressed = pygame.key.get_pressed()
            if keyspressed[pygame.K_r]:
                pygame.time.wait(1000)
                main()

        pygame.display.update()

def main():
    global SCREEN, FPSCLOCK
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    SCREEN = pygame.display.set_mode((SCREENW,SCREENH))
    pygame.display.set_caption('Flappy Bird: Revolutions')
    angle_pipe = 20
    angle_bird = 0
    bird_radius = 192
    bird = Bird()
    pipe_1 = Pipe()
    pipe_2 = Pipe()
    count = 0

    while True:
        SCREEN.blit(BG,(0,0))
        SCREEN.blit(pipe_1.rotate(angle_pipe)[0],pipe_1.rotate(angle_pipe)[1])
        SCREEN.blit(pipe_2.rotate(angle_pipe+90)[0],pipe_2.rotate(angle_pipe+90)[1])
        w,h = bird.image.get_size()
        large_rect = pygame.Surface((w,2*bird_radius + h),pygame.SRCALPHA)
        large_rect.blit(bird.image,(0,0))
        birdImg = pygame.transform.rotozoom(large_rect,angle_bird,1)
        w_1,h_1 = birdImg.get_size()
        new_pos =  (640 - w_1/2,360 - h_1/2)

        count += 1
        if count >= 240 and count%240 == 0:
            global score
            score += 1
        message = myfont.render(str(score),True,(255,255,255))
        if score > 9:
            SCREEN.blit(message,(600,330))
        else:
            SCREEN.blit(message,(622.5,330))
        SCREEN.blit(birdImg,new_pos)
        
        angle_pipe += 0.75
        angle_bird -= 1.5

        if(bird_radius >= 290):
            bird_radius = 290
        elif(bird_radius <= 79):
            bird_radius = 79
        bird_radius -= 3

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                bird_radius += 25
            
            keyspressed = pygame.key.get_pressed()
            if keyspressed[pygame.K_DOWN]:
                gameOver()
        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__ == "__main__":
    welcomeScreen()
