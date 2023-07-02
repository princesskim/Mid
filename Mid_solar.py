import pygame
import numpy as np
import os
import math


def getRegularPolygon(N, r):
    v = np.zeros((N,2))
    for i in range(N):
        rad = i * 2 * np.pi / N
        x = np.cos(rad) * r
        y = np.sin(rad) * r
        v[i] = [x, y]
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



WINDOW_WIDTH = 1300
WINDOW_HEIGHT = 800


pygame.init()
pygame.display.set_caption("20191235 김시리")
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

#current_path = os.path.dirname(__file__)
assets_path = '/Users/siri/Downloads/3_Pygame/assets' #os.path.join(current_path, 'assests')
font = pygame.font.SysFont("Arial", 14)

# UFO 이미지 초기 설정
UFO_image1 = pygame.image.load(os.path.join(assets_path, 'UFO.png'))
UFO_x = WINDOW_WIDTH-100
UFO_y = int(WINDOW_HEIGHT / 2)
UFO_dx = 0
UFO_dy = 0

UFO_width = 50
UFO_height = 40
UFO_image = pygame.transform.scale(UFO_image1, (UFO_width, UFO_height))


def draw(M, points, color=(0,0,0), p0=None):
    R = M[0:2,0:2]
    t = M[0:2,2]
    points_transformed = (R @ points.T).T + t

    pygame.draw.polygon(screen, color, points_transformed, 1)
    if p0 is not None:
        pygame.draw.line(screen, color, p0, points_transformed[0] ,width=1)

spaceColor = (0, 0, 0)
sunColor = (255,228,0)
earthColor = (0,0,255)
moonColor = (166,166,166)
marsColor = (255,94,0)
phobosColor = (218,218,255)
deimosColor = (212,244,250)

#실제 radius(AU)에 비례 (* 100000000배)
sunR = 0.005 * 1000000
earthR = 0.00004 * 1000000
marsR = 0.00002 * 1000000
moonR = 0.00001 * 1000000
phobosR = 5 #0.00000007 
deimosR = 3 #0.00000004 

#실제 distance(AU)
distSE = 1  *  (sunR+400)     #태양-지구
distSM = 1.1  *  (sunR+400)    #태양-화성 1.6AU
distEM = 100.  #0.003  #지구-달
distMP = 40.  #0.00006 #화성-포보스
distMD = 80.  #0.00015  #화성-데이모스

#objects
Sun = getRegularPolygon(1000,sunR)
Earth = getRegularPolygon(8, earthR)
Moon = getRegularPolygon(3, moonR)
Mars = getRegularPolygon(8, marsR)
Phobos = getRegularPolygon(3, phobosR)
Deimos = getRegularPolygon(3, deimosR)

#자전 - rotation angle
angleSun = -5
angleEarth = 0
angleMoon = 0
angleMars = 0
anglePhobos = 0
angleDeimos = 0

#공전 - rotation angle
angleSE = -4
angleSM = -2
angleEM = 0
angleMP = 0
angleMD = 0

#angleSU = 0

done = False
while not done:


    # / 자전주기(일)
    angleSun += 1 / 27.
    angleEarth += 1 / 1.
    angleMoon += 1 / 27.3
    angleMars += 1 / 1.
    anglePhobos += 1 / 0.32
    angleDeimos += 1 / 1.26

    # / 공전주기(일)
    angleSE += 1 / 365.
    angleSM += 1 / 687.
    angleEM += 1 / 27.3
    angleMP += 1 / 0.32
    angleMD += 1 / 1.26

    #angleSU +=  1 / 365.

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
            elif event.key == pygame.K_LEFT:
                UFO_dx = -3
            elif event.key == pygame.K_RIGHT:
                UFO_dx = 3
            elif event.key == pygame.K_UP:
                UFO_dy = -3
            elif event.key == pygame.K_DOWN:
                UFO_dy = 3

           

            # elif event.key == pygame.K_s: #해 주변으로 맴돌아
            #     distSU = math.sqrt((center[0] - UFO_x) ** 2 + (center[1]- UFO_y) ** 2)
            #     angleSU = math.degrees(math.acos(distSU / abs((center[0] - UFO_x))))
            #     Mufo = T3mat(center[0], center[1]) @ R3mat(angleSU) @  T3mat(distSU,0) @ R3mat(-angleSU)
            #     R = Mufo[0:2,0:2]
            #     t = Mufo[0:2,2]
            #     points_transformed = (R @ np.array([UFO_x,UFO_y], dtype = 'float').T).T + t
            #     UFO_x = points_transformed[0]
            #     UFO_y = points_transformed[1]
            #     UFO_dx = 0
            #     UFO_dy = 0
            # elif event.key == pygame.K_e: #지구 주변으로 맴돌아
            #     
            # elif event.key == pygame.K_m: #화성 주변으로 맴돌아
            #     
        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                UFO_dx = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                UFO_dy = 0

    UFO_x += UFO_dx
    UFO_y += UFO_dy
    
    screen.fill(spaceColor)
    #pygame.draw.line(screen, (255,255,255), [0,WINDOW_HEIGHT/2.], [WINDOW_WIDTH, WINDOW_HEIGHT/2.] ,width= 1)


    screen.blit(UFO_image, [UFO_x, UFO_y])

    center = (-sunR+50., WINDOW_HEIGHT/2.)

    Msun = T3mat(center[0], center[1]) @ R3mat(angleSun)
    draw(Msun, Sun, sunColor, center) 

    Mearth = T3mat(center[0], center[1]) @ R3mat(angleSE) @  T3mat(distSE,0) @ R3mat(-angleSE) @ R3mat(angleEarth)
    draw(Mearth, Earth, earthColor, Mearth[:2,2])
    
    Mmoon = Mearth @ R3mat(angleEM) @  T3mat(distEM,0) @R3mat(-angleEM) @R3mat(angleMoon) 
    draw(Mmoon, Moon, moonColor, Mmoon[:2,2])

    Mmars = T3mat(center[0], center[1]) @ R3mat(angleSM) @  T3mat(distSM,0) @ R3mat(-angleSM) @ R3mat(angleMars)
    draw(Mmars, Mars, marsColor, Mmars[:2,2])
    
    Mphobos = Mmars @ R3mat(angleMP) @  T3mat(distMP,0) @R3mat(-angleMP) @R3mat(anglePhobos) 
    draw(Mphobos, Moon, phobosColor, Mphobos[:2,2])

    Mdeimos = Mmars @ R3mat(angleMD) @  T3mat(distMD,0) @R3mat(-angleMD) @R3mat(angleDeimos) 
    draw(Mdeimos, Moon, deimosColor, Mdeimos[:2,2])

    pygame.draw.circle(screen,(40,40,40),Mearth[:2,2], distEM,1) 
    pygame.draw.circle(screen,(40,40,40),Mmars[:2,2], distMP,1) 
    pygame.draw.circle(screen,(40,40,40),Mmars[:2,2], distMD,1) 

    sun_text = font.render("SUN", True, sunColor)
    sun_text_rect = sun_text.get_rect(topleft=(center[0] + sunR + 10, center[1] -7))
    screen.blit(sun_text, sun_text_rect)

    earth_text = font.render("EARTH", True, earthColor)
    earth_text_rect = earth_text.get_rect(topleft=(Mearth[0,2]+earthR+10, Mearth[1,2] -7))
    screen.blit(earth_text, earth_text_rect)

    mars_text = font.render("MARS", True, marsColor)
    mars_text_rect = mars_text.get_rect(topleft=(Mmars[0,2]+marsR+10, Mmars[1,2] -7))
    screen.blit(mars_text, mars_text_rect)

    moon_text = font.render("MOON", True, moonColor)
    moon_text_rect = earth_text.get_rect(topleft=(Mearth[0,2]-20, Mearth[1,2] + distEM +5))
    screen.blit(moon_text, moon_text_rect)

    phobos_text = font.render("PHOBOS", True, phobosColor)
    phobos_text_rect = mars_text.get_rect(topleft=(Mmars[0,2]-30, Mmars[1,2] + distMP +5))
    screen.blit(phobos_text, phobos_text_rect)

    deimos_text = font.render("DEIMOS", True, deimosColor)
    deimos_text_rect = mars_text.get_rect(topleft=(Mmars[0,2]-30, Mmars[1,2] + distMD +5))
    screen.blit(deimos_text, deimos_text_rect)

    
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()




