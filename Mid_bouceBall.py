import pygame
import numpy as np

WINDOW_WIDTH = 1300
WINDOW_HEIGHT = 700

BLACK = (0, 0, 0)
RED = (255, 0,0)
PINK = (255, 200, 210)

BALL_RADIUS = 15
BALL_COLOR = BLACK
FLOOR_HEIGHT = 50
FLOOR_COLOR = BLACK

pygame.init()
pygame.display.set_caption("20191235 김시리")
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial", 36)
font_color = RED

xinit = WINDOW_WIDTH * 6 / 7. + 50 # np.random.uniform(0, WINDOW_WIDTH) # uniform probability distribution
yinit = 0
vx_init = 0.
vy_init = 13.

txy = np.array([xinit, yinit]) # translation of the polygon
vxy = np.array([vx_init, vy_init])
axy = np.array([0, .421])

floor_rect = pygame.Rect(0, WINDOW_HEIGHT - FLOOR_HEIGHT, WINDOW_WIDTH, FLOOR_HEIGHT)

block_w = 100
block_h = 20.
block1_rect = pygame.Rect(WINDOW_WIDTH * 6 / 7., WINDOW_HEIGHT * 7 / 8., block_w ,block_h)
block2_rect = pygame.Rect(WINDOW_WIDTH * 5 / 7., WINDOW_HEIGHT * 6 / 8., block_w ,block_h)
block3_rect = pygame.Rect(WINDOW_WIDTH * 4 / 7., WINDOW_HEIGHT * 5 / 8., block_w ,block_h)
block4_rect = pygame.Rect(WINDOW_WIDTH * 3 / 7., WINDOW_HEIGHT * 4 / 8., block_w ,block_h)
block5_rect = pygame.Rect(WINDOW_WIDTH * 2 / 7., WINDOW_HEIGHT * 3 / 8., block_w ,block_h)
block6_rect = pygame.Rect(WINDOW_WIDTH * 1 / 7., WINDOW_HEIGHT * 2 / 8., block_w ,block_h)


last_jump = False
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
            elif event.key == pygame.K_LEFT:
                vxy[0] -= 3
            elif event.key == pygame.K_RIGHT:
                vxy[0] += 3
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                vxy[0] = 0


    vxy += axy 
    txy += vxy 

    if txy[1] + BALL_RADIUS  >= WINDOW_HEIGHT - FLOOR_HEIGHT: 
        text = font.render("Fail!", True, font_color)
        text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 3))
        screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.wait(5000) 
        done = True

    if txy[0] + BALL_RADIUS  >= WINDOW_WIDTH:
        txy[0] = WINDOW_WIDTH - BALL_RADIUS 
    
    if txy[0] - BALL_RADIUS  < 0:
        txy[0] = BALL_RADIUS 

    if (WINDOW_WIDTH * 6 / 7.<=txy[0] + BALL_RADIUS and txy[0] - BALL_RADIUS <= WINDOW_WIDTH * 6 / 7.+ block_w) and (txy[1] + BALL_RADIUS >=WINDOW_HEIGHT * 7 / 8.) and (txy[1]< WINDOW_HEIGHT * 7 / 8.):
        vxy[1] = -13
        txy[1] = WINDOW_HEIGHT * 7 / 8. - BALL_RADIUS 
    
    if (WINDOW_WIDTH * 5 / 7.<=txy[0] + BALL_RADIUS and txy[0] - BALL_RADIUS<=WINDOW_WIDTH * 5 / 7.+ block_w) and (txy[1] + BALL_RADIUS >=WINDOW_HEIGHT * 6 / 8.) and (txy[1]< WINDOW_HEIGHT * 6 / 8.):
        vxy[1] = -13
        txy[1] = WINDOW_HEIGHT * 6 / 8. - BALL_RADIUS 

    if (WINDOW_WIDTH * 4 / 7.<=txy[0] + BALL_RADIUS and txy[0] - BALL_RADIUS<=WINDOW_WIDTH * 4 / 7.+ block_w) and (txy[1] + BALL_RADIUS >=WINDOW_HEIGHT * 5 / 8.) and (txy[1]< WINDOW_HEIGHT * 5 / 8.):
        vxy[1] = -13
        txy[1] = WINDOW_HEIGHT * 5 / 8. - BALL_RADIUS 

    if (WINDOW_WIDTH * 3 / 7.<=txy[0] + BALL_RADIUS and txy[0] - BALL_RADIUS<=WINDOW_WIDTH * 3 / 7.+ block_w) and (txy[1] + BALL_RADIUS >=WINDOW_HEIGHT * 4 / 8.) and (txy[1]< WINDOW_HEIGHT * 4 / 8.):
        vxy[1] = -13
        txy[1] = WINDOW_HEIGHT * 4 / 8. - BALL_RADIUS 

    if (WINDOW_WIDTH * 2 / 7.<=txy[0] + BALL_RADIUS and txy[0] - BALL_RADIUS<=WINDOW_WIDTH * 2 / 7.+ block_w) and (txy[1] + BALL_RADIUS >=WINDOW_HEIGHT * 3 / 8.) and (txy[1]< WINDOW_HEIGHT * 3 / 8.):
        vxy[1] = -13
        txy[1] = WINDOW_HEIGHT * 3 / 8. - BALL_RADIUS 

    if (WINDOW_WIDTH * 1 / 7.<=txy[0] + BALL_RADIUS and txy[0] - BALL_RADIUS<=WINDOW_WIDTH * 1 / 7.+ block_w) and (txy[1] + BALL_RADIUS >=WINDOW_HEIGHT * 2 / 8.) and (txy[1]< WINDOW_HEIGHT * 2 / 8.):

        if last_jump is False:
            vxy[1] = -13
            txy[1] = WINDOW_HEIGHT * 2 / 8. - BALL_RADIUS 
            last_jump = True
        elif last_jump is True:
            text = font.render("Congratulations!", True, font_color)
            text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 3))
            screen.blit(text, text_rect)
            pygame.display.flip()
            pygame.time.wait(5000) 
            done = True



    screen.fill(PINK)
    pygame.draw.circle(screen, BALL_COLOR, txy, BALL_RADIUS)
    pygame.draw.rect(screen, FLOOR_COLOR, floor_rect)
    pygame.draw.rect(screen, FLOOR_COLOR, block1_rect)
    pygame.draw.rect(screen, FLOOR_COLOR, block2_rect)
    pygame.draw.rect(screen, FLOOR_COLOR, block3_rect)
    pygame.draw.rect(screen, FLOOR_COLOR, block4_rect)
    pygame.draw.rect(screen, FLOOR_COLOR, block5_rect)
    pygame.draw.rect(screen, FLOOR_COLOR, block6_rect)


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
