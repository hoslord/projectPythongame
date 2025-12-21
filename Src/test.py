import os

os.environ['SDL_AUDIODRIVER'] = 'dummy'
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide' 
os.environ['SDL_VIDEODRIVER'] = 'dummy'
os.environ['XDG_RUNTIME_DIR'] = '/tmp'

import pygame
import sys
import pygame.draw
import pygame.key
import random 

pygame.init()
pygame.mixer.quit() 

pygame.font.init()

RETRY = 4

clock = pygame.time.Clock() 

TITLE = 'Ping-Pong'  
WIDTH = 800  
HEIGHT = 480  

WHITE = (255, 255, 255) 
BLACK = (0, 0, 0) 

PLATFORM_WIDTH = 100  
PLATFORM_HEIGHT = 15  
PLATFORM_SPEED = 10   

platform_rect=pygame.rect.Rect(WIDTH / 2 - PLATFORM_WIDTH / 2, HEIGHT - PLATFORM_HEIGHT * 2, PLATFORM_WIDTH, PLATFORM_HEIGHT) 
CIRCLE_RADIUS = 15 
CIRCLE_SPEED = 10 
circle_first_collide = False  
circle_x_speed = 0  
circle_y_speed = CIRCLE_SPEED 

circle_rect = pygame.rect.Rect(WIDTH / 2 - CIRCLE_RADIUS, HEIGHT / 2 - CIRCLE_RADIUS, CIRCLE_RADIUS * 2, CIRCLE_RADIUS * 2) 

score = 0  

ARIAL_FONT_PATH = pygame.font.match_font('arial')   
ARIAL_FONT_48 = pygame.font.Font(ARIAL_FONT_PATH, 48)  
ARIAL_FONT_36 = pygame.font.Font(ARIAL_FONT_PATH, 36)  


screen = pygame.display.set_mode([WIDTH, HEIGHT]) 
pygame.display.set_caption(TITLE) 

game_over = False
run = True 
while run:
    for event in pygame.event.get():   
        if event.type == pygame.QUIT:
            run = False
            continue
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  
                run=False
                continue
            elif event.key == pygame.K_r:   
                game_over = False       

                platform_rect.centerx = WIDTH / 2       
                platform_rect.bottom = HEIGHT - PLATFORM_HEIGHT  

                circle_rect.center = [WIDTH / 2, HEIGHT / 2] 
                circle_x_speed = 0        
                circle_y_speed = CIRCLE_SPEED    
                circle_first_collide = False

                score = 0 
                  

    screen.fill(BLACK) 

    if not game_over:   
        
        keys = pygame.key.get_pressed()  

        if keys[pygame.K_a]:
            platform_rect.x -= PLATFORM_SPEED  
        elif keys[pygame.K_d]:
            platform_rect.x += PLATFORM_SPEED   

        if platform_rect.colliderect(circle_rect):   
            if not circle_first_collide:
                if random.randint(0, 1) == 0:       
                    circle_x_speed = CIRCLE_SPEED
                else:
                     circle_x_speed = -CIRCLE_SPEED

                circle_first_collide = True
            
            circle_y_speed = -CIRCLE_SPEED

            score += 1

        pygame.draw.rect(screen, WHITE, platform_rect) 

    circle_rect.x += circle_x_speed 
    circle_rect.y += circle_y_speed  

    if circle_rect.bottom >= HEIGHT:
        game_over = True                   
        circle_y_speed = -CIRCLE_SPEED     
    elif circle_rect.top <= 0:     
        circle_y_speed = CIRCLE_SPEED
    elif circle_rect.left <= 0:         
        circle_x_speed = CIRCLE_SPEED
    elif circle_rect.right >= WIDTH:   
        circle_x_speed = -CIRCLE_SPEED


    pygame.draw.circle(screen, WHITE, circle_rect.center, CIRCLE_RADIUS) 

    score_surface = ARIAL_FONT_48.render(str(score), True, WHITE)  
    
    if not game_over:
        screen.blit(score_surface, [WIDTH / 2 - score_surface.get_width() / 2, 15])  
    else:
        retry_surface = ARIAL_FONT_36.render('Press R to restart', True, WHITE) 
        screen.blit(score_surface, [WIDTH / 2 - score_surface.get_width() / 2, HEIGHT / 3])  
        screen.blit(retry_surface, [WIDTH / 2 - retry_surface.get_width() / 2, HEIGHT / 3 + score_surface.get_height()]) 


    clock.tick(60)  

    pygame.display.flip() 


pygame.quit() 




