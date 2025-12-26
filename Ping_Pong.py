from tkinter.messagebox import RETRY
import pygame
import pygame.draw
import pygame.key
import random 

pygame.init() #инициализация библиотеки

pygame.font.init() #инициализация шрифта

TITLE = 'Ping-Pong'  # название игры
WIDTH = 800  # ширина окна игры
HEIGHT = 480  # высота окна игры

FPS = 60 #создание числа кадров для оптимизации работы игры

WHITE = (255, 255, 255) #создание белого цвета, используя палитру RGB
BLACK = (0, 0, 0) # создание черного цвета

PLATFORM_WIDTH = 100  # ширина игровой ракетки(платформы)
PLATFORM_HEIGHT = 15  # высота платформы
PLATFORM_SPEED = 10   # скорость движения платформы

platform_rect=pygame.rect.Rect(WIDTH / 2 - PLATFORM_WIDTH / 2, HEIGHT - PLATFORM_HEIGHT * 2, PLATFORM_WIDTH, PLATFORM_HEIGHT) # создание платформы (прямоугольной) (с ее шириной и высотой), расположение ее по центру экрана

CIRCLE_RADIUS = 15 # создание мячика для игры
CIRCLE_SPEED = 10 # скорость движения шарика
circle_first_collide = False  # первый отскок от платформы
circle_x_speed = 0  #скорость шарика по x
circle_y_speed = CIRCLE_SPEED # скорость шарика по y

circle_rect = pygame.rect.Rect(WIDTH / 2 - CIRCLE_RADIUS, HEIGHT / 2 - CIRCLE_RADIUS, CIRCLE_RADIUS * 2, CIRCLE_RADIUS * 2) # создание шарика и расположение его по центру экрана

score = 0  # кол-во очков

ARIAL_FONT_PATH = pygame.font.match_font('arial')   #находим нужный шрифт в библиотеке
ARIAL_FONT_48 = pygame.font.Font(ARIAL_FONT_PATH, 48)  # создаем нужный шрифт с размером 48
ARIAL_FONT_36 = pygame.font.Font(ARIAL_FONT_PATH, 36)  # создаем нужный шрифт с размером 36


screen = pygame.display.set_mode([WIDTH, HEIGHT]) # создание экрана игры с шириной и высотой
pygame.display.set_caption(TITLE) # задаем название игры

clock = pygame.time.Clock() #ускорение или замедление игры

game_over = False
run = True # переменная для работы цикла while
while run:
    for event in pygame.event.get():   #обработка событий полученных напрямую из игры
        if event.type == pygame.QUIT:
            run = False
            continue
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # выключение игры при помощи клавиши ESC
                run=False
                continue
            elif event.key == pygame.K_r:   # перезапуск игры при помощи клавишы R
                game_over = False       # перезапуск игры

                platform_rect.centerx = WIDTH / 2       # возвращаем игрока в изначальную позицию
                platform_rect.bottom = HEIGHT - PLATFORM_HEIGHT  

                circle_rect.center = [WIDTH / 2, HEIGHT / 2] #возвращаем шарик на изначальную позицию
                circle_x_speed = 0        # обнуляем скорость шарика
                circle_y_speed = CIRCLE_SPEED    # обнуляем скорость шарика
                circle_first_collide = False #обнуляем первое столкновение шарика и платформы

                score = 0 # обнуляем счет
                  

    screen.fill(BLACK) # заливаем весь экран черным цветом чтобы убрать следы при движении платформы


    if not game_over:   # процесс игры
        
        keys = pygame.key.get_pressed()  #создаем функционал клавиш

        if keys[pygame.K_a]:
            platform_rect.x -= PLATFORM_SPEED  #движение платфоры влево
        elif keys[pygame.K_d]:
            platform_rect.x += PLATFORM_SPEED   # движение платформы вправо

        if platform_rect.colliderect(circle_rect):   #проверяем столкновение шарика и платформы
            if not circle_first_collide:
                if random.randint(0, 1) == 0:       #случайный выбор направления полета шарика при первом отскоке
                    circle_x_speed = CIRCLE_SPEED
                else:
                     circle_x_speed = -CIRCLE_SPEED

                circle_first_collide = True
            
            circle_y_speed = -CIRCLE_SPEED

            score += 1

        pygame.draw.rect(screen, WHITE, platform_rect) #выведение прямоугольной белой платформы на экран игры

    circle_rect.x += circle_x_speed # движение щарика по x
    circle_rect.y += circle_y_speed  # движение шарика по y

    if circle_rect.bottom >= HEIGHT:
        game_over = True                   # проигрыш если мячик коснулся нижней части экрана
        circle_y_speed = -CIRCLE_SPEED     # возвращение шарика при проигрыше
    elif circle_rect.top <= 0:     # верхняя граница экрана , т.к с y=0
        circle_y_speed = CIRCLE_SPEED
    elif circle_rect.left <= 0:         # левая граница экрана
        circle_x_speed = CIRCLE_SPEED
    elif circle_rect.right >= WIDTH:   # правая граница экрана
        circle_x_speed = -CIRCLE_SPEED


    pygame.draw.circle(screen, WHITE, circle_rect.center, CIRCLE_RADIUS) #выведение белого круглого шарика на экран игры

    score_surface = ARIAL_FONT_48.render(str(score), True, WHITE)  # создание текста на экране игры белого цвета сглаженного содержащего score
    
    if not game_over:
        screen.blit(score_surface, [WIDTH / 2 - score_surface.get_width() / 2, 15])  # отрисовка значения очков по середине по x и на высоте 15 пикселей
    else:
        retry_surface = ARIAL_FONT_36.render('Press R to restart', True, WHITE)  #конец игры при проигрыше, вывод текста о перезапуске
        screen.blit(score_surface, [WIDTH / 2 - score_surface.get_width() / 2, HEIGHT / 3])  # вывод кол-ва набранных очков
        screen.blit(retry_surface, [WIDTH / 2 - retry_surface.get_width() / 2, HEIGHT / 3 + score_surface.get_height()])  # вывод сообщения о перезапуске относительно предыдущего сообщения


    clock.tick(FPS)  #задаем кол-во кадров в игре

    pygame.display.flip() # обновляем полностью весь экран игры для вывода платформы


pygame.quit() # выключение игры




