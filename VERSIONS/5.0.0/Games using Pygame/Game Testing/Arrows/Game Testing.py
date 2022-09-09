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
def player():
    pygame.draw.rect(dis, red, (x, y, 15, 15))
def drawHome():
    pygame.draw.rect(dis, home, (homex, homey, hsizex, hsizey))



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

tree1ax = rand.randint(0,600)
tree1ay = rand.randint(0,600)

tree2ax = rand.randint(0,600)
tree2ay = rand.randint(0,600)

tree3ax = rand.randint(0,600)
tree3ay = rand.randint(0,600)

tree4ax = rand.randint(0,600)
tree4ay = rand.randint(0,600)

homex = rand.randint(0, 400)
homey = rand.randint(0, 400)
hsizex = rand.randint(50,75)
hsizey = rand.randint(50,75)

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

tree1ax = round(tree1ax)
tree1ay = round(tree1ay)

tree2ax = round(tree2ax)
tree2ay = round(tree2ay)

tree3ax = round(tree3ax)
tree3ay = round(tree3ay)

tree4ax = round(tree4ax)
tree4ay = round(tree4ay)


houseLocation = (homex, homey)
houseSize = (hsizex, hsizey)
playerLocation = (x, y)
#--------------main program---------------#
game_over=False
#----------loop-----------
while not game_over:
    for event in pygame.event.get(): # if user did smth
        if event.type == pygame.QUIT: # if they exited the game i will close
            game_over = True
        
        
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change -= 15
            if event.key == pygame.K_RIGHT:
                x_change += 15
            if event.key == pygame.K_UP:
                y_change -= 15
            if event.key == pygame.K_DOWN:
                y_change += 15
            
                
            
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
        if x == tree1x:
            wood += 1
            tree1x = -50
            tree1y = -50
        if x == tree2x:
            wood += 1
            tree1x = -50
            tree1y = -50
        if x == tree3x:
            wood += 1
            tree1x = -50
            tree1y = -50
        if x == tree4x:
            wood += 1
            tree1x = -50
            tree1y = -50
        print(x, y)
        dis.fill(BG)
        #player
        player()
        #trees
        pygame.draw.rect(dis, tree, (tree1x, tree1y, 20, 20))
        pygame.draw.rect(dis, tree, (tree2x, tree2y, 20, 20))
        pygame.draw.rect(dis, tree, (tree3x, tree3y, 20, 20))
        pygame.draw.rect(dis, tree, (tree4x, tree4y, 20, 20))
        pygame.draw.rect(dis, tree, (tree5x, tree5y, 20, 20))
        pygame.draw.rect(dis, tree, (tree6x, tree6y, 20, 20))
        pygame.draw.rect(dis, tree, (tree7x, tree7y, 20, 20))
        pygame.draw.rect(dis, tree, (tree8x, tree8y, 20, 20))
        pygame.draw.rect(dis, tree, (tree9x, tree4y, 20, 20))
        pygame.draw.rect(dis, tree, (tree1ax, tree1ay, 20, 20))
        pygame.draw.rect(dis, tree, (tree2ax, tree2ay, 20, 20))
        pygame.draw.rect(dis, tree, (tree3ax, tree3ay, 20, 20))
        pygame.draw.rect(dis, tree, (tree4ax, tree4ay, 20, 20))        
        #Home/house
        drawHome()
        pygame.display.update()

pygame.quit()
quit()
