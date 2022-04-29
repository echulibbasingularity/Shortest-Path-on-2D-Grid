

import pygame

WIDTH,HEIGHT = 800,800
ROWS,COL = 8,8
SIZE = WIDTH//COL  # SIZE OF SQUARE

fps = 70

# RGB COORDINATES
'''wow'''
PINK = (253,87,231)
WHITE = (240,219,230)

image = pygame.image.load('chess.png')
image = pygame.transform.scale(image, (SIZE-10,SIZE-10))  # RESIZING IMAGE

pic_X, pic_Y = 0,0



screen = pygame.display.set_mode((WIDTH,HEIGHT))

def grid():
    screen.fill(WHITE)
    for row in range(ROWS):
        for col in range(row%2,ROWS,2):
            pygame.draw.rect(screen,PINK,(col*SIZE, row*SIZE, SIZE,SIZE))

def curr_pos(x, y):
    return (x,y)

def legal_move(x, y):
    if x<0 or y<0 or x>WIDTH or y>WIDTH:
        return False
    else:
        return True

def knight_move(pic_X, pic_Y):
    # x_co = curr_pos(x,y)[0]
    # y_co = curr_pos(x,y)[1]
    # dx = [-200,-200,100,200]
    # dy=[-100,100,200,100]
    # for i in range(2):
    #     new_X = pic_X + dx[i]
    #     new_Y = pic_Y + dy[i]  




    # else:


        screen.blit(image,(pic_X, pic_Y))
             
    



   
   





running = True
clock = pygame.time.Clock()
while running:
    clock.tick(fps)
    for event in pygame.event.get(): #list of all events in the game
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pic_X,pic_Y = pygame.mouse.get_pos()  # returns x,y position of the mouse when clicked
            print(pic_X,pic_Y)
            



    grid()
    #curr_pos((pic_X//SIZE)*SIZE + SIZE/2 - 48,(pic_Y//SIZE)*SIZE + SIZE/2 - 47)
    knight_move((pic_X//SIZE)*SIZE + SIZE/2 - 48,(pic_Y//SIZE)*SIZE + SIZE/2 - 47)
    
    pygame.display.update()
pygame.display.quit()

