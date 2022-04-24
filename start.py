
import pygame

WIDTH,HEIGHT = 800,800
ROWS,COL = 8,8
SIZE = WIDTH//COL  # SIZE OF SQUARE

fps = 100

PINK = (253,87,231)   #RGB COORDINATES
WHITE = (240,219,230)

image = pygame.image.load('chess.png')
image = pygame.transform.scale(image, (SIZE-10,SIZE-10))  #RESIZING IMAGE

pic_X, pic_Y = 0,0



screen = pygame.display.set_mode((WIDTH,HEIGHT))

def grid():
    screen.fill(WHITE)
    for row in range(ROWS):
        for col in range(row%2,ROWS,2):
            pygame.draw.rect(screen,PINK,(col*SIZE, row*SIZE, SIZE,SIZE))
    
def knight_move(pic_X, pic_Y):
    if pic_X==0 and pic_Y==0:
        # draws the image on the surface at (x,y)
        screen.blit(image,(pic_X, pic_Y))
    else:
        screen.blit(image,(pic_X-48, pic_Y-47))
             
    



   
   





running = True
clock = pygame.time.Clock()
while running:
    clock.tick(fps)
    for event in pygame.event.get(): #list of all events in the game
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pic_X,pic_Y = pygame.mouse.get_pos()  # returns x,y position of the mouse when clicked
            



    grid()
    knight_move(pic_X,pic_Y)
    pygame.display.update()
pygame.display.quit()
