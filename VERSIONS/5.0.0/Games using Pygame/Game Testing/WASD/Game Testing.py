import pygame
import random as rand
pygame.init()
dis=pygame.display.set_mode((400,300))

pygame.display.set_caption('Game testing')
x = 200
y =150
red = (255,0,0)
BG = (0,0,0)
green = (0,255,0)
x_change = 0
y_change = 0
tree1x = rand.randint(0,400)
tree1y = rand.randint(0,300)

tree2x = rand.randint(0,400)
tree2y = rand.randint(0,300)

tree3x = rand.randint(0,400)
tree3y = rand.randint(0,300)

tree4x = rand.randint(0,400)
tree4y = rand.randint(0,300)

tree5x = rand.randint(0,400)
tree5y = rand.randint(0,300)


#--------------main program---------------#
game_over=False
#----------loop-----------
while not game_over:
    for event in pygame.event.get(): # if user did smth
        if event.type == pygame.QUIT: # if they exited the game i will close
            game_over = True
        
        
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                x_change -= 10
            if event.key == pygame.K_d:
                x_change += 10
            if event.key == pygame.K_w:
                y_change -= 10
            if event.key == pygame.K_s:
                y_change += 10
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                x_change = 0
            if event.key == pygame.K_d:
                x_change = 0
            if event.key == pygame.K_w:
                y_change = 0
            if event.key == pygame.K_s:
                y_change = 0

        x += x_change
        y += y_change

        dis.fill(BG)
        #player
        pygame.draw.rect(dis, red, (x, y, 10, 10))
        #trees
        pygame.draw.rect(dis, green, (tree1x, tree1y, 15, 15))
        pygame.draw.rect(dis, green, (tree2x, tree2y, 15, 15))
        pygame.draw.rect(dis, green, (tree3x, tree3y, 15, 15))
        pygame.draw.rect(dis, green, (tree4x, tree4y, 15, 15))
        pygame.draw.rect(dis, green, (tree5x, tree5y, 15, 15))
        
        
        pygame.display.update()

pygame.quit()
quit()
