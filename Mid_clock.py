import pygame
import numpy as np
import os

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

    pygame.draw.polygon(screen, BLACK, points_transformed)


WINDOW_WIDTH = 700
WINDOW_HEIGHT = 700

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BROWN = (51,0,0)

pygame.init()
pygame.display.set_caption("20191235 김시리")
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

current_path = os.path.dirname(__file__)
piano_path = os.path.join(current_path, 'piano')

tok_snd = pygame.mixer.Sound(os.path.join(piano_path, 'tok.mp3'))
tak_snd = pygame.mixer.Sound(os.path.join(piano_path, 'tak.mp3'))
ring_snd = pygame.mixer.Sound(os.path.join(piano_path, 'hour_ring.mp3'))

font = pygame.font.SysFont("Arial", 30, True) #글씨체, 크기, 굵기여부



#default time ; 10h 59m 40s
angleH = -90. + (10. + 59/60. + (40/60)/60.) * 30
angleM = -90. + (59 + 40/60.) * 6
angleS = -90. + 40 * 6

frame =0 

#시침
H_w = 120
H_h = 7
rectH = getRectangle(H_w, H_h)
#분침
M_w = 170
M_h = 7
rectM = getRectangle(M_w ,M_h)
#초침
S_w = 170
S_h = 3
rectS = getRectangle(S_w ,S_h) 

#시계 칸 그리기 용도
rect = getRectangle(15,2)
#5칸마다 그려지는 긴 줄
rectL = getRectangle(30,2)


done = False
while not done:
    frame+=1
    angleS += 6. #1초에 6도
    angleM += 6 /60. #1분에 6도
    angleH += (6/60.)/60. #1시간에 6도


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Mouse Button is Pressed!")
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
            elif event.key == pygame.K_UP:
                angleM += 360/60. #1분 미래
                angleH += 30/60.
            elif event.key == pygame.K_DOWN:
                angleM -= 360/60. #1분 과거
                angleH -= 30/60.
            elif event.key == pygame.K_RIGHT:
                angleM += 5 * 360/60. #5분 미래
                angleH += 5 * 30/60.
            elif event.key == pygame.K_LEFT:
                angleM -= 5 * 360/60. #5분 과거
                angleH -= 5 * 30/60.


    #똑딱 초침 소리
    if (angleM + 90.) % 360. <= 6 /60.:
        ring_snd.play() 
 
    elif frame%2 == 0: 
        tok_snd.play() 

    else:
        tak_snd.play() 

    screen.fill(WHITE)

    center = (WINDOW_WIDTH/2., WINDOW_HEIGHT/2.)

    M_H = T3mat(center[0], center[1]) @ R3mat(angleH) @ T3mat(-20,-H_h/2.)
    draw(M_H, rectH, BLACK)
    M_M = T3mat(center[0], center[1]) @ R3mat(angleM) @ T3mat(-30,-M_h/2.)
    draw(M_M, rectM, BLACK)
    M_S = T3mat(center[0], center[1]) @ R3mat(angleS) @ T3mat(-30,-S_h/2.)
    draw(M_S, rectS, BLACK)

    pygame.draw.circle(screen, BROWN, center, 270, 40) #시계 테두리
    pygame.draw.circle(screen, WHITE, center, 2) #침 고정 핀


    #60칸 그리기
    for num in range(60):
        num+=1 # 1, 2, ~ , 60
        angle = -90. + num * 6.
        M = T3mat(center[0], center[1]) @ R3mat(angle) @ T3mat(160,1)

        if num%5==0:
            M1 = M @ T3mat(-15,0)
            R = M1[0:2,0:2]
            t = M1[0:2,2]
            points_transformed = (R @ rectL.T).T + t
        else:
            R = M[0:2,0:2]
            t = M[0:2,2]
            points_transformed = (R @ rect.T).T + t
        pygame.draw.polygon(screen, BROWN, points_transformed)
        

    #숫자 그리기
    for num in range(12):
        num+=1 # 1, 2, ~ , 12
        angle = -90. + num * 30.
        M = T3mat(center[0], center[1]) @ R3mat(angle) @ T3mat(200,0)
        text = font.render( str(num), True, BLACK)
        text_rect = text.get_rect(center=M[0:2,2])
        #verticalalignment='center'
        # #horizontalalignment='center'
        screen.blit(text, text_rect)
 
    pygame.display.flip()
    clock.tick(1) #1초에 1번 while loop

pygame.quit()




