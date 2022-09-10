import pygame
import random as rand
from time import sleep
pygame.init()
dis=pygame.display.set_mode((600,600))

pygame.display.set_caption('Game testing')
x = 300
y = 300
red = (255,0,0)
BG = (0,200,0)
black = (0,0,0)
tree = (0,100,0)
home = (165,42,42)
x_change = 0
y_change = 0
wood = 0
white = (255, 255, 255)

font = pygame.font.SysFont("comicsansms", 25)
def Your_score(score):
    value = font.render("Wood Collected: " + str(wood), True, white)
    dis.blit(value, [0, 0])
def redraw():
        tree1x = rand.randint(0,600)
        tree1y = rand.randint(0,600)

        tree2x = rand.randint(0,600)
        tree2y = rand.randint(0,600)

        tree3x = rand.randint(0,600)
        tree3y = rand.randint(0,600)

        tree4x = rand.randint(0,600)
        tree4y = rand.randint(0,600)

        tree5x = rand.randint(0,600)
        tree5y = rand.randint(0,600)

        tree6x = rand.randint(0,600)
        tree6y = rand.randint(0,600)

        tree7x = rand.randint(0,600)
        tree7y = rand.randint(0,600)

        tree8x = rand.randint(0,600)
        tree8y = rand.randint(0,600)

        tree9x = rand.randint(0,600)
        tree9y = rand.randint(0,600)

        pygame.draw.rect(dis, tree, tree1)
        pygame.draw.rect(dis, tree, tree2)       
        pygame.draw.rect(dis, tree, tree3)       
        pygame.draw.rect(dis, tree, tree4)       
        pygame.draw.rect(dis, tree, tree5)       
        pygame.draw.rect(dis, tree, tree6)       
        pygame.draw.rect(dis, tree, tree7)       
        pygame.draw.rect(dis, tree, tree8)       
        pygame.draw.rect(dis, tree, tree9)



tree1x = rand.randint(0,600)
tree1y = rand.randint(0,600)

tree2x = rand.randint(0,600)
tree2y = rand.randint(0,600)

tree3x = rand.randint(0,600)
tree3y = rand.randint(0,600)

tree4x = rand.randint(0,600)
tree4y = rand.randint(0,600)

tree5x = rand.randint(0,600)
tree5y = rand.randint(0,600)

tree6x = rand.randint(0,600)
tree6y = rand.randint(0,600)

tree7x = rand.randint(0,600)
tree7y = rand.randint(0,600)

tree8x = rand.randint(0,600)
tree8y = rand.randint(0,600)

tree9x = rand.randint(0,600)
tree9y = rand.randint(0,600)



tree1x = round(tree1x)
tree1y = round(tree1y)

tree2x = round(tree2x)
tree2y = round(tree2y)

tree3x = round(tree3x)
tree3y = round(tree3y)

tree4x = round(tree4x)
tree4y = round(tree4y)

tree5x = round(tree5x)
tree5y = round(tree5y)

tree6x = round(tree6x)
tree6y = round(tree6y)

tree7x = round(tree7x)
tree7y = round(tree7y)

tree8x = round(tree8x)
tree8y = round(tree8y)

tree9x = round(tree9x)
tree9y = round(tree9y)


homex = rand.randint(0, 400)
homey = rand.randint(0, 400)
hsizex = rand.randint(50,75)
hsizey = rand.randint(50,75)


houseLocation = (homex, homey)
houseSize = (hsizex, hsizey)
playerLocation = (x, y)
#--------------main program---------------#
game_over=False
#----------loop-----------
while not game_over:
    for event in pygame.event.get(): # if user did smth
        if event.type == pygame.QUIT: # if they exited the game it will close
            game_over = True
        
        
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change -= 10
            if event.key == pygame.K_RIGHT:
                x_change += 10
            if event.key == pygame.K_UP:
                y_change -= 10
            if event.key == pygame.K_DOWN:
                y_change += 10
            
                
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x_change = 0
            if event.key == pygame.K_RIGHT:
                x_change = 0
            if event.key == pygame.K_UP:
                y_change = 0
            if event.key == pygame.K_DOWN:
                y_change = 0

        x += x_change
        y += y_change
        player = pygame.Rect(x, y, 15, 15)
        tree1 = pygame.Rect(tree1x, tree1y, 25, 25)
        tree2 = pygame.Rect(tree2x, tree2y, 25, 25)
        tree3 = pygame.Rect(tree3x, tree3y, 25, 25)
        tree4 = pygame.Rect(tree4x, tree4y, 25, 25)
        tree5 = pygame.Rect(tree5x, tree5y, 25, 25)
        tree6 = pygame.Rect(tree6x, tree6y, 25, 25)
        tree7 = pygame.Rect(tree7x, tree7y, 25, 25)
        tree8 = pygame.Rect(tree8x, tree8y, 25, 25)
        tree9 = pygame.Rect(tree9x, tree9y, 25, 25)
        house = pygame.Rect(homex, homey, hsizex, hsizey)

        dis.fill(BG)
        #player
        pygame.draw.rect(dis, red, player)
        #Home/house
        pygame.draw.rect(dis, home, house)
        #check colision
        if player.colliderect(house):
                redraw()
        if player.colliderect(tree1):
                wood += 1
                tree1x = -50
                tree1y= -50
        if player.colliderect(tree2):
                wood += 1
                tree2x = -50
                tree2y= -50
        if player.colliderect(tree3):
                wood += 1
                tree3x = -50
                tree3y= -50
        if player.colliderect(tree4):
                wood += 1
                tree4x = -50
                tree4y= -50
        if player.colliderect(tree5):
                wood += 1
                tree5x = -50
                tree5y= -50
        if player.colliderect(tree6):
                wood += 1
                tree6x = -50
                tree6y= -50
        if player.colliderect(tree7):
                wood += 1
                tree7x = -50
                tree7y= -50
        if player.colliderect(tree8):
                wood += 1
                tree8x = -50
                tree8y= -50
        if player.colliderect(tree9):
                wood += 1
                tree9x = -50
                tree9y= -50
        #trees
        pygame.draw.rect(dis, tree, tree1)
        pygame.draw.rect(dis, tree, tree2)       
        pygame.draw.rect(dis, tree, tree3)       
        pygame.draw.rect(dis, tree, tree4)       
        pygame.draw.rect(dis, tree, tree5)       
        pygame.draw.rect(dis, tree, tree6)       
        pygame.draw.rect(dis, tree, tree7)       
        pygame.draw.rect(dis, tree, tree8)       
        pygame.draw.rect(dis, tree, tree9)

        Your_score(wood)
        
        pygame.display.update()


        
        
        
        

pygame.quit()
quit()
