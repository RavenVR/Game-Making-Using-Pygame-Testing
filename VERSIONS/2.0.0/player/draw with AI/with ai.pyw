############################VARIABLES####################################
import pygame
import random
from time import sleep
pygame.init()
dis=pygame.display.set_mode((600,600))
pygame.display.update()
pygame.display.set_caption('testing')
x1 = 0
y1 = 0
x1_b = random.randint(0,600)
y1_b = random.randint(0,600)

x1_a = 0
y1_a = 0
x_ai = random.randint(0,600)
y_ai = random.randint(0,600)
blue = (0,255,0)
red = (255,0,0)
clock = pygame.time.Clock()
game_over=False
ai_tick=0
ai_wait_time=20
#########################MAIN WINDOW################################################
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
########################MOVEMENT########################################SS
        ai_tick += 1
        ai_tick = ai_tick % ai_wait_time
        if ai_tick == 0:
            y1_a=random.randint(-10,10)
            x1_a=random.randint(-10,10) 
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y1 = -10
            if event.key == pygame.K_DOWN:
                y1 = 10
            if event.key == pygame.K_LEFT:
                x1 = -10
            if event.key == pygame.K_RIGHT:
                x1 = 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                y1 = 0
            if event.key == pygame.K_DOWN:
                y1 = 0
            if event.key == pygame.K_LEFT:
                x1 = 0
            if event.key == pygame.K_RIGHT:
                x1 = 0
        
            
            if y1_b > 600:
                y1_b = 0
                y1 = 0
            if y1_b < 0:
                y1_b = 600
                y1 = 0
            if x1_b > 600:
                x1_b = 0
                x1 = 0
            if x1_b < 0:
                x1_b = 600
                x1 = 0
                
            if y_ai > 600:
                y_ai = 0
                y1_a = 0
            if y_ai < 0:
                y_ai = 600
                y1_a = 0
            if x_ai > 600:
                x_ai = 0
                x1_a = 0
            if x_ai < 0:
                x_ai = 600
                x1_a = 0
        y1_b += y1
        x1_b += x1
        x_ai += x1_a
        y_ai += y1_a
        pygame.draw.rect(dis, blue, [x1_b, y1_b, 10, 10])
        pygame.draw.rect(dis, red, [x_ai, y_ai, 10, 10])
        pygame.display.update()
 
        clock.tick(30)
pygame.quit()
quit()
