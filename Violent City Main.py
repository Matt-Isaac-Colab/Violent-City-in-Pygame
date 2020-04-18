import pygame
import random
import sys
import os

from pygame.locals import *

pygame.init()

#define mouse
Mouse_x = 0
Mouse_y = 0
Game_On = 0

#define enemy
enemy_picture = 0
enemy_direction = 0
enemy_position_x = 0
enemy_position_y = 0
enemy_alive = False

# Default screen width / height
#WIDTH = 1366 #1366
#HEIGHT = 768 #768

# Mouse x, y and Mouse settings an Keyboard
Mouse_x, Mouse_y = pygame.mouse.get_pos() #Gets position of mouse

#Colours and Fonts
white = (255, 255, 255)
white_o = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
brown = (150, 75, 0)
gray = (112.95, 112.95, 112.95)
yellow = (255, 255, 0)
font = pygame.font.Font("IBMPlexSans-Regular.ttf", 40) #Imported Font
font_L = pygame.font.Font("IBMPlexSans-Regular.ttf", 100) #Imported Font
font_S = pygame.font.Font("IBMPlexSans-Regular.ttf", 17) #Imported Font


#Display settings
display_width, display_height = 1366, 768   # sets width and height
gameDisplay = pygame.display.set_mode((display_width,display_height), pygame.FULLSCREEN) #Sets display to height and width
pygame.display.set_caption("Violent City") # gives title ontop of gameDisplay

#Titles and Text
def Mouse_x_View(msg, color):       #this defines functions used to draw a title
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [500, 0])
def Mouse_y_View(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [500, 50])
def prompt(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [50, 500])
def instruction_line_1(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [50, 150])
def instruction_line_2(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [50, 250])

#status bar
def bullet_count(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [50, 250])
def time_display(msg, color):
    screen_text = font_S.render(msg, True, color)
    gameDisplay.blit(screen_text, [180, 60])
def kills_display(msg, color):
    screen_text = font_S.render(msg, True, color)
    gameDisplay.blit(screen_text, [70, 23])
def missed_display(msg, color):
    screen_text = font_S.render(msg, True, color)
    gameDisplay.blit(screen_text, [70, 60])
def speed_display(msg, color):
    screen_text = font_S.render(msg, True, color)
    gameDisplay.blit(screen_text, [175, 26])
def score_display(msg, color):
    screen_text = font_S.render(msg, True, color)
    gameDisplay.blit(screen_text, [70, 90])

#End screen
def end_display(msg, color):
    screen_text = font_L.render(msg, True, color)
    gameDisplay.blit(screen_text, [0, 100])
#Directory
main_dir = os.getcwd()

#Some Images
gun = pygame.image.load(os.path.join(main_dir, 'images\\gun.png')) #Loads Images from directory
crosshair = pygame.image.load(os.path.join(main_dir,'images\\crosshair.png'))
Start_Button = pygame.image.load(os.path.join(main_dir,'images\\start_button.png'))
bullet = pygame.image.load(os.path.join(main_dir,'images\\bullet.png'))
logo = pygame.image.load(os.path.join(main_dir,'images\\logo.png'))
reload = pygame.image.load(os.path.join(main_dir,'images\\reload.png'))
enemy_1 = pygame.image.load(os.path.join(main_dir,'images\\enemy_1.png'))
enemy_2 = pygame.image.load(os.path.join(main_dir,'images\\enemy_2.png'))
enemy_3 = pygame.image.load(os.path.join(main_dir,'images\\enemy_3.png'))
background = pygame.image.load(os.path.join(main_dir,'images\\back_01.jpeg'))
status_bar = pygame.image.load(os.path.join(main_dir,'images\\status_bar.png'))
replay = pygame.image.load(os.path.join(main_dir,'images\\replay.png'))
oh_snap = pygame.image.load(os.path.join(main_dir,'images\\oh_snap.png'))

#Sounds and Music
main_music = pygame.mixer.music.load(os.path.join(main_dir, 'music\\music.mp3'))
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(1)
ah = pygame.mixer.Sound(os.path.join(main_dir, 'sounds\\ah.wav'))
ah_2 = pygame.mixer.Sound(os.path.join(main_dir, 'sounds\\ah2.wav'))
ah_3 = pygame.mixer.Sound(os.path.join(main_dir, 'sounds\\ah3.wav'))
game_over = pygame.mixer.Sound(os.path.join(main_dir, 'sounds\\game_over.wav'))
reload_sound = pygame.mixer.Sound(os.path.join(main_dir, 'sounds\\reload.wav'))
shot_sound = pygame.mixer.Sound(os.path.join(main_dir, 'sounds\\shot.wav'))

#Start of Code
Game_On = False

def MainMenu():
    menu = True
    while menu:

        gameDisplay.fill(white)    #Fills Background
        gameDisplay.blit(Start_Button ,  ( 400, 500))
        gameDisplay.blit(logo, (450 , 50))    #Refers back to functions for colour and x, y
        prompt('Press any were to', black)
        instruction_line_1('Move mouse around to aim, click to shoot and press R to reload.', black)
        instruction_line_2('If at any point you need to quit press esc.', black)
        pygame.display.update()
        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:   # stops game from crashing by making sure it quits if it crashes
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                menu = False
                Game_Start()

def Game_Start():
    global kills, score, level, missed

    #FPS and Time
    fps = 60
    minute = fps*60
    second = fps
    clock.tick(fps)
    current_time = pygame.time.get_ticks()
    wait_time = current_time + 1000
    wantReload = False
    previous_time = pygame.time.get_ticks()
    time_seconds = 0
    time_minutes = 0

    # Score & stats
    kills = 0
    score = 0

    # Missed
    missed = 0
    maxMissed = 20

    # Enemy speed
    level = 1 # Enemy speed = starting speed + level

    Game_On = True

    #Bullet coord and Bullet settings
    bulletsleft = 10
    bullet_1 = (1334, 16)
    bullet_2 = (1302, 16)
    bullet_3 = (1270, 16)
    bullet_4 = (1238, 16)
    bullet_5 = (1206, 16)
    bullet_6 = (1174, 16)
    bullet_7 = (1142, 16)
    bullet_8 = (1110, 16)
    bullet_9 = (1078, 16)
    bullet_10 = (1046, 16)

    #Reload and Diplay
    def bullet_display():
        if bulletsleft == 10:
            [gameDisplay.blit(bullet, bullet_1) and gameDisplay.blit(bullet, bullet_2) and gameDisplay.blit(bullet, bullet_3) and
            gameDisplay.blit(bullet, bullet_4) and gameDisplay.blit(bullet, bullet_5) and gameDisplay.blit(bullet, bullet_6) and
            gameDisplay.blit(bullet, bullet_7) and gameDisplay.blit(bullet, bullet_8) and gameDisplay.blit(bullet, bullet_9) and
            gameDisplay.blit(bullet, bullet_10)]
        if bulletsleft == 9:
            [gameDisplay.blit(bullet, bullet_1) and gameDisplay.blit(bullet, bullet_2) and gameDisplay.blit(bullet, bullet_3) and
            gameDisplay.blit(bullet, bullet_4) and gameDisplay.blit(bullet, bullet_5) and gameDisplay.blit(bullet, bullet_6) and
            gameDisplay.blit(bullet, bullet_7) and gameDisplay.blit(bullet, bullet_8) and gameDisplay.blit(bullet, bullet_9)]
        if bulletsleft == 8:
            [gameDisplay.blit(bullet, bullet_1) and gameDisplay.blit(bullet, bullet_2) and gameDisplay.blit(bullet, bullet_3) and
            gameDisplay.blit(bullet, bullet_4) and gameDisplay.blit(bullet, bullet_5) and gameDisplay.blit(bullet, bullet_6) and
            gameDisplay.blit(bullet, bullet_7) and gameDisplay.blit(bullet, bullet_8)]
        if bulletsleft == 7:
            [gameDisplay.blit(bullet, bullet_1) and gameDisplay.blit(bullet, bullet_2) and gameDisplay.blit(bullet, bullet_3) and
            gameDisplay.blit(bullet, bullet_4) and gameDisplay.blit(bullet, bullet_5) and gameDisplay.blit(bullet, bullet_6) and
            gameDisplay.blit(bullet, bullet_7)]
        if bulletsleft == 6:
            [gameDisplay.blit(bullet, bullet_1) and gameDisplay.blit(bullet, bullet_2) and gameDisplay.blit(bullet, bullet_3) and
            gameDisplay.blit(bullet, bullet_4) and gameDisplay.blit(bullet, bullet_5) and gameDisplay.blit(bullet, bullet_6)]
        if bulletsleft == 5:
            [gameDisplay.blit(bullet, bullet_1) and gameDisplay.blit(bullet, bullet_2) and gameDisplay.blit(bullet, bullet_3) and
            gameDisplay.blit(bullet, bullet_4) and gameDisplay.blit(bullet, bullet_5)]
        if bulletsleft == 4:
            [gameDisplay.blit(bullet, bullet_1) and gameDisplay.blit(bullet, bullet_2) and gameDisplay.blit(bullet, bullet_3) and
            gameDisplay.blit(bullet, bullet_4)]
        if bulletsleft == 3:
            [gameDisplay.blit(bullet, bullet_1) and gameDisplay.blit(bullet, bullet_2) and gameDisplay.blit(bullet, bullet_3)]
        if bulletsleft == 2:
            [gameDisplay.blit(bullet, bullet_1) and gameDisplay.blit(bullet, bullet_2)]
        if bulletsleft == 1:
            [gameDisplay.blit(bullet, bullet_1)]
        if bulletsleft <= 0:
            gameDisplay.blit(reload, (1142, 16))


    #mouse update
    def mouse_update():
        global Mouse_x, Mouse_y
        if Mouse_x != (0, 0, 0): #update if mouse is somewhere it can't be so it always updates
            Mouse_x, Mouse_y = pygame.mouse.get_pos()

    def enemy_spawn():
        global enemy_picture, enemy_direction, enemy_position_x, enemy_position_y, enemy_alive, enemy_width, enemy_height
        if enemy_alive == True:
            return

        #Set Global Position and direction
        were_spawn = random.randint(1, 4)
        enemy_type = random.randint(1, 3)
        if were_spawn == 1:         #left
            enemy_position_y = random.uniform(0, 568)
            enemy_position_x = -200
            enemy_direction = 1
        elif were_spawn == 2:         #top
            enemy_position_y = -200
            enemy_position_x = random.uniform(0, 1166)
            enemy_direction = 2
        elif were_spawn == 3:         #right
            enemy_position_y = random.uniform(0, 568)
            enemy_position_x = 1366
            enemy_direction = 3
        elif were_spawn == 4:         #bottom
            enemy_position_y = 768
            enemy_position_x = random.uniform(0, 1166)
            enemy_direction = 4

        #Set global picture
        if enemy_type == 1:
            enemy_picture = enemy_1
            enemy_height = 200
            enemy_width = 144
        elif enemy_type == 2:
            enemy_picture = enemy_2
            enemy_height = 200
            enemy_width = 162
        elif enemy_type == 3:
            enemy_picture = enemy_3
            enemy_height = 200
            enemy_width = 137

        enemy_alive = True

    def enemy_move():
        global enemy_picture, enemy_direction, enemy_position_x, enemy_position_y, enemy_alive, missed
        if enemy_alive == False:
            return
        if enemy_direction == 1:
            enemy_position_x = enemy_position_x + level * 0.5 + 3
            if enemy_position_x >= 1566:
                missed = missed + 1
                enemy_alive = False
        elif enemy_direction == 2:
            enemy_position_y = enemy_position_y + level * 0.5 + 3
            if enemy_position_y >= 768:
                missed = missed + 1
                enemy_alive = False
        elif enemy_direction == 3:
            enemy_position_x = enemy_position_x - level * 0.5 - 3
            if enemy_position_x <= -200:
                missed = missed + 1
                enemy_alive = False
        elif enemy_direction == 4:
            enemy_position_y = enemy_position_y - level * 0.5 - 3
            if enemy_position_y <= -200:
                missed = missed + 1
                enemy_alive = False

    def enemy_draw():
        global enemy_picture, enemy_direction, enemy_position_x, enemy_position_y, enemy_alive
        if enemy_alive == False:
            return

        gameDisplay.blit(enemy_picture, (enemy_position_x, enemy_position_y))

    def hit():
        global enemy_height, enemy_width, enemy_alive, kills, score, level
        if  Mouse_x >= enemy_position_x and Mouse_x <= enemy_position_x + enemy_width and Mouse_y >= enemy_position_y and Mouse_y <= enemy_position_y + enemy_height:
            kills = kills + 1
            score = score + 2 * level
            ah_no = random.randint(1, 3)
            if ah_no == 1:
                ah.play()
            if ah_no == 2:
                ah_2.play()
            if ah_no == 3:
                ah_3.play()
            enemy_alive = False
            if kills == 10 * level:
                level = level + 1


    while Game_On:
        pygame.mouse.set_visible(False) # Makes mouse invisible
        current_time = pygame.time.get_ticks()

        #Paint the Screen
        gameDisplay.fill(black)
        gameDisplay.blit(background, (0, 0))
        #Enemy Update and Draw
        enemy_spawn()
        enemy_move()
        enemy_draw()

        if current_time - previous_time >= 1000:
            previous_time = pygame.time.get_ticks()
            time_seconds = time_seconds +1
        if time_seconds == 60:
            time_seconds = 0
            time_minutes = time_minutes + 1
        if missed == 10:
            game_over.play()
            Game_On = False


        #status bar titles
        gameDisplay.blit(status_bar, (5, 5))
        kills_display(str(kills), white)
        missed_display(str(missed), white)
        speed_display(str(level), white)
        time_display(str(time_minutes) +':'+ str(time_seconds), white)
        score_display(str(score), white)

        #Update and Mouse
        mouse_update()
        #Mouse_x_View ( "Mouse X =" + str(Mouse_x), white) # Displays x and y of mouse
        #Mouse_y_View ("Mouse Y =" + str(Mouse_y), white)
        gameDisplay.blit(gun, (Mouse_x , 608)) #Gun hand runs on the same as the x axis of the mouse but stays at the bottom
        gameDisplay.blit(crosshair, (Mouse_x - 16, Mouse_y - 16)) # Cross hair is 32 pixels long so you need to take 16 from the x and y to get the center

        #Update bullets
        if current_time >= wait_time and wantReload == True:
            bulletsleft = 10
            wantReload = False
        bullet_display()
        #bullet_count(str(bulletsleft), white)

        #Update display with new information
        pygame.display.update()

        key = pygame.key.get_pressed()
        #if key[pygame.K_b]:
        #    missed = missed + 1
        if key[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
        if key[ord('r')] and bulletsleft <= 0:
            if wantReload == False:
                reload_sound.play()
                wait_time = current_time + 1000
                wantReload = True

        for event in pygame.event.get():  # stops game from crashing by making sure it quits if it crashes
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bulletsleft != 0:
                    bulletsleft = bulletsleft - 1
                    shot_sound.play()
                    hit()

    while Game_On == False:
        pygame.mouse.set_visible(True)
        gameDisplay.fill(black)
        gameDisplay.blit(background, (0, 0))
        gameDisplay.blit(oh_snap, (0, 0))
        gameDisplay.blit(replay, (0, 60))
        end_display('Your Final Score is =' + str(score), white)
        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
        if key[pygame.K_SPACE]:
            MainMenu()

        pygame.display.update()
        for event in pygame.event.get():  # stops game from crashing by making sure it quits if it crashes
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

MainMenu()
