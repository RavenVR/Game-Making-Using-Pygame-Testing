############################VARIABLES####################################
import pygame
import random
pygame.init()
dis=pygame.display.set_mode((600,600))
pygame.display.update()
pygame.display.set_caption('testing')
x1 = 0
y1 = 0
x1_b = 300
y1_b = 300
blue = (0,255,0)
clock = pygame.time.Clock()
game_over=False
#########################MAIN WINDOW################################################
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
########################MOVEMENT########################################SS
        
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                y1 = -15
            if event.key == pygame.K_s:
                y1 = 15
            if event.key == pygame K_a:
                x1 = -15
            if event.key == pygame.K_d:
                x1 = 15
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                y1 = 0
            if event.key == pygame.K_s:
                y1 = 0
            if event.key == pygame.K_a:
                x1 = 0
            if event.key == pygame.K_d:
                x1 = 0
        
            
            if y1_b > 600:
                y1_b = 0
            if y1_b < 0:
                y1_b = 600
            if x1_b > 600:
                x1_b = 0
            if x1_b < 0:
                x1_b = 600
        y1_b += y1
        x1_b += x1
        pygame.draw.rect(dis, blue, [x1_b, y1_b, 10, 10])
 
        pygame.display.update()
 
        clock.tick(30)
pygame.quit()
quit()
