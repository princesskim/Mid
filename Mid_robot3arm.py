import pygame
import numpy as np



def getRectangle(width, height, x=0, y=0):
    v=np.array([[x,       y],
                [x+width, y],
                [x+width, y+height],
                [x,       y+height]],
                dtype = 'float')
    return v


def R3mat(deg): 
    theta = np.deg2rad(deg)
    c = np.cos(theta)
    s = np.sin(theta)
    R = np.array([[ c, -s, 0], 
                  [ s,  c, 0],
                  [ 0,  0, 1] ])
    return R

def T3mat(a,b): 
    t = np.eye(3)
    t[0,2] = a
    t[1,2] = b
    return t

def draw(M, points, color=(0,0,0)):
    R = M[0:2,0:2]
    t = M[0:2,2]
    points_transformed = (R @ points.T).T + t

    pygame.draw.polygon(screen, BLACK, points_transformed) #, width=3)




WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700

BLACK = (0, 0, 0)
PINK = (255, 200, 210)

pygame.init()
pygame.display.set_caption("20191235 김시리")
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

center1 = [50.0, 50.0]
angle1 = 70
angle2 =-110
angle3 = 90
angle4 = 39


w1 = 250
h1 = 60
rect1 = getRectangle(w1,h1)

w2 = 210
h2 = 40
rect2 = getRectangle(w2,h2)

w3 = 170
h3 = 30
rect3 = getRectangle(w3,h3)

#gripper
wg = 25
hg = 15
rect4 = getRectangle(wg,hg)
rect5 = getRectangle(wg,hg)

gap12 = 40
gap23 = 40
gap3g = 40

gripL = h3/2.


done = False
while not done:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Mouse Button is Pressed!")
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
            elif event.key == pygame.K_q:
                angle1 -= 3
            elif event.key == pygame.K_w:
                angle1 += 3
            elif event.key == pygame.K_a:
                angle2 -= 3
            elif event.key == pygame.K_s:
                angle2 += 3
            elif event.key == pygame.K_z:
                angle3 -= 3
            elif event.key == pygame.K_x:
                angle3 += 3
            elif event.key == pygame.K_c:
                angle4 -= 3
            elif event.key == pygame.K_v:
                angle4 += 3
            elif event.key == pygame.K_LEFT:
                center1[0]-=10.
            elif event.key == pygame.K_RIGHT:
                center1[0]+=10.
            elif event.key == pygame.K_UP:
                center1[1]-=10.
            elif event.key == pygame.K_DOWN:
                center1[1]+=10.           
            elif event.key == pygame.K_SPACE:
                if gripL ==  h3/2. :
                    gripL = h3/2. - hg/2.
                elif gripL ==  h3/2. - hg/2. :
                    gripL = h3/2.

                
            
    screen.fill(PINK)

    pygame.draw.line(screen, BLACK, center1, [center1[0],0.0], 10)
    
    pygame.draw.circle(screen, BLACK, center1, 10)
    M1 =  np.eye(3) @ T3mat(center1[0], center1[1]) @ R3mat(angle1) @ T3mat(0, -h1/2.)
    draw(M1, rect1, BLACK)
    
    C12_1 = M1 @ T3mat(w1, h1/2.) 
    center12_1 = C12_1[0:2,2]
    pygame.draw.circle(screen, BLACK, center12_1, 10)
    C12_2 = C12_1 @ T3mat(gap12, 0.)
    center12_2 = C12_2[0:2,2]
    pygame.draw.circle(screen, BLACK, center12_2, 10)
    pygame.draw.line(screen, BLACK, center12_1, center12_2, 10)
    M2 = C12_2 @ R3mat(angle2) @ T3mat(0,-h2/2.)
    draw(M2, rect2, BLACK)

    C23_2 = M2 @ T3mat(w2, h2/2.) 
    center23_2 = C23_2[0:2,2]
    pygame.draw.circle(screen, BLACK, center23_2, 10)
    C23_3 = C23_2 @ T3mat(gap23, 0.)
    center23_3 = C23_3[0:2,2]
    pygame.draw.circle(screen, BLACK, center23_3, 10)
    pygame.draw.line(screen, BLACK, center23_2, center23_3, 10)
    M3 = C23_3 @ R3mat(angle3) @ T3mat(0,-h3/2.)
    draw(M3, rect3, BLACK)

    C3g_3 = M3 @ T3mat(w3, h3/2.) 
    center3g_3 = C3g_3[0:2,2]
    pygame.draw.circle(screen, BLACK, center3g_3, 10)
    C3g_g = C3g_3 @ T3mat(gap3g, 0.)
    center3g_g = C3g_g[0:2,2]
    pygame.draw.circle(screen, BLACK, center3g_g, 5)
    pygame.draw.line(screen, BLACK, center3g_3, center3g_g, 10)
    
    M4 = C3g_g  @ R3mat(angle4) @ T3mat(0,-hg/2.) @ T3mat(0, gripL) 
    draw(M4, rect4, BLACK)
    M5 = C3g_g  @ R3mat(angle4) @ T3mat(0,-hg/2.) @ T3mat(0, -gripL) 
    draw(M5, rect5, BLACK)

    Cg1 = M4 @ T3mat(0, hg/2.) 
    centerg1 = Cg1[0:2,2]
    pygame.draw.circle(screen, BLACK, centerg1, 5)
    Cg2 = M5 @ T3mat(0, hg/2.) 
    centerg2 = Cg2[0:2,2]
    pygame.draw.circle(screen, BLACK, centerg2, 5)
    pygame.draw.line(screen, BLACK, centerg1, centerg2, 10)


    pygame.display.flip()
    clock.tick(60)

pygame.quit()