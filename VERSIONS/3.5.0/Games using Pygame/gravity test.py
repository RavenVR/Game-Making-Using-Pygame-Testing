import pygame

pygame.init()
dis=pygame.display.set_mode((400,300))
 
pygame.display.set_caption('test')

clock = pygame.time.Clock()
fps = 25

velocity = 0
y = 150
 
blue=(0,0,255)
red=(255,0,0)
 
game_over=False
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
    velocity += 0.2
    if velocity > 2.7:
        velocity = 2.7
    y += velocity
    if y > 300:
        y = 150
        velocity = 0
    dis.fill((0, 0, 0))
    pygame.draw.rect(dis,blue,[200,int(y),10,10])
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()
quit()
