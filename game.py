#Main game file

import pygame, sys
from pygame.locals import *
from snake import *
from apple import *
#Setup some constants/colors
DARKGREEN = (162, 209, 73)
LIGHTGREEN = (170, 215, 81)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
LIGHTRED = (240, 120, 120)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
LIGHTBLUE = (120, 240, 120)
YELLOW = (255, 255, 0)
TRANSPARENTWHITE = (255, 255, 255, 128)
FONT = "freesansbold.ttf"

FPS = 20
BOX_SIZE = 35
DISPLAYX = 455
DISPLAYY = 455

#DIRECTIONS
UP = "UP"
DOWN = "DOWN"
LEFT = "LEFT"
RIGHT = "RIGHT"

#Score
SCORE = 0
HIGHSCORE = 0


pygame.init()
dis=pygame.display.set_mode((DISPLAYX, DISPLAYY))
CLOCK = pygame.time.Clock()
pygame.display.update()
pygame.display.set_caption("Snake game by Joshua Kim and Vartan Yildiz")

# game_over=False

#font_style = pygame.font.SysFont(None, 50)
#
#def message(msg,color):
#    mesg = font_style.render(msg, True, color)
#    dis.blit(mesg, [DISPLAYX/2, DISPLAYY/2])


count_font = pygame.font.SysFont("freesansbold.ttf", 35)

def apple_count(count):
    value = count_font.render("Score: " + str(count), True, WHITE)
    high_score_value = count_font.render("Best: " + str(get_high_score()), True, WHITE)
    dis.blit(value, [0, 0])
    dis.blit(high_score_value, [0, BOX_SIZE])

def get_high_score():
    score_file = open("highscore.txt")
    high_score = 0
    for line in score_file:
        high_score = line
    return int(high_score)

def set_high_score(score):
    file_write = open("highscore.txt", "w")
    file_write.write(str(score))
    file_write.close()



def game_loop():

    global SCORE

    #Create new snake
    snake_obj = Snake(BLUE, "RIGHT", dis, BOX_SIZE)
    #Create new apple
    apple = Apple(RED, dis, BOX_SIZE, snake_obj)
    
    while True:

        
        #count = len(snake_obj.positions) - 1    
        
        pygame.display.update()

        for event in pygame.event.get():
            
            if event.type == pygame.KEYDOWN:
                
                if event.key == K_LEFT:
                    if snake_obj.direction != RIGHT:
                        snake_obj.direction = LEFT
                        

                elif event.key == K_RIGHT:
                    if snake_obj.direction != LEFT:
                        snake_obj.direction = RIGHT
                        
                elif event.key == K_UP:
                    if snake_obj.direction != DOWN:
                        snake_obj.direction = UP
                        
                elif event.key == K_DOWN:
                    if snake_obj.direction != UP:
                        snake_obj.direction = DOWN
                        
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        if collision_check(snake_obj) == True:
            SCORE = 0
            game_over()
            return

        
        if snake_obj.direction == LEFT:
            snake_obj.move(LEFT)
            
        elif snake_obj.direction == RIGHT:
            snake_obj.move(RIGHT)
        elif snake_obj.direction == UP:
            snake_obj.move(UP)
        elif snake_obj.direction == DOWN:
            snake_obj.move(DOWN)

        #applecount = 0
        
        if snake_obj.eat_apple(apple):
            apple.place_on_grid(DISPLAYX, DISPLAYY)
            SCORE += 1
            

            #Check if score is a high score
            if SCORE > get_high_score():
                set_high_score(SCORE)
            apple_count(SCORE)
            #applecount += 1

        else:
            snake_obj.positions.remove(snake_obj.positions[-1])
            snake_obj.tail_coords = snake_obj.positions[-1]


        #font = pygame.font.Font("freesansbold.ttf", 18)
        #text = font.render(applecount, True, green, blue)
        #textRect = text.get_rect()
        #textRect.center = (425 // 2, 425 // 2)

        #Try using message for counter overlay


        
        #message(applecount, RED)



        draw_game_area()
        apple.draw()
        snake_obj.draw()
        
        apple_count(SCORE)
 
        pygame.display.update()
        CLOCK.tick(FPS)
def draw_game_area():
    #Loop through all the rows and corresponding columns to create "boxes"/grids 
    #on the play-area via Pygame rect objects.
    for boxx in range(DISPLAYX):
        for boxy in range(DISPLAYY):
            # box_width = boxx* BOX_SIZE
            # box_length = boxy* BOX_SIZE

            grid_box = pygame.Rect(boxx * BOX_SIZE, boxy * BOX_SIZE, BOX_SIZE, BOX_SIZE)
            if boxx % 2 == 0:

                if boxy % 2 == 0:
                    pygame.draw.rect(dis, LIGHTGREEN, grid_box)
                else:
                    pygame.draw.rect(dis, DARKGREEN, grid_box)
                
            elif boxy % 2 != 0:
                pygame.draw.rect(dis, LIGHTGREEN, grid_box)
            
            else:
                pygame.draw.rect(dis, DARKGREEN, grid_box)
    
    
def collision_check(snake_obj):
    #Checks for collision with world borders.

    if snake_obj.head_coords[0] < 0 or snake_obj.head_coords[1] < 0:

        return True
    if snake_obj.head_coords[0] >= 425 or snake_obj.head_coords[1] >= 425:

        return True
    for i in range(1, len(snake_obj.positions)):
        
        if snake_obj.positions[i] == snake_obj.head_coords:
            draw_game_area()
            snake_obj.draw()
            pygame.display.update()
            return True
    else:
        return False

def text_objects(text, font):
    textsurface = font.render(text, True, BLACK)
    return textsurface, textsurface.get_rect()



def start_screen():

    font = pygame.font.Font(FONT, 60)
    play_font = pygame.font.Font(FONT, 30)
    

    font_surface = font.render("SNAKE", True, WHITE)
    play_surface = play_font.render("Press P to Play", True, WHITE)
    score_surface = play_font.render("High Score: " + str(get_high_score()), True, YELLOW)


    rect_font = font_surface.get_rect()
    play_rect_font = play_surface.get_rect()
    score_rect = score_surface.get_rect()

    rect_font.center = ((DISPLAYX / 2), (DISPLAYY / 2))
    play_rect_font.center = ((DISPLAYX / 2), (DISPLAYY / 1.65))
    score_rect.center = ((DISPLAYX / 2), (DISPLAYY / 1.45))
    draw_game_area()
    dis.blit(font_surface, rect_font)
    dis.blit(play_surface, play_rect_font)
    dis.blit(score_surface, score_rect)
    pygame.display.update()









    #Difficulty Buttons
    
    difficulty_main_font = pygame.font.Font(FONT, 20)
    
    
    difficulty_surface = difficulty_main_font.render("Select Difficulty (changes speed)", True, WHITE)
    
    difficulty_rect_font = difficulty_surface.get_rect()
    
    difficulty_rect_font.center = ((DISPLAYX / 1.95), (DISPLAYY / 1.65))
    
    
    
    
    
    #gameDisplay.blit(TextSurf, TextRect)
    
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    
    #Easy button
    if 150+100 > mouse[0] > 150 and 450+50 > mouse[1] > 450:
        pygame.draw.rect(dis, LIGHTGREEN,(150,450,100,50))
        #if click[0] == 1:
            #speed change
    else:
        pygame.draw.rect(dis, GREEN,(150,450,100,50))
    
    easy_font = pygame.font.Font("freesansbold.ttf", 15)
    textSurf, textRect = text_objects("Easy", easy_font)
    textRect.center = ((150+50), (450 + 25))
    dis.blit(textSurf, textRect)
    
    
    #Normal Button
    if 350+100 > mouse[0] > 350 and 450+50 > mouse[1] > 450:
        pygame.draw.rect(dis, LIGHTBLUE,(350,450,100,50))
    else:
        pygame.draw.rect(dis, BLUE,(350,450,100,50))
    
    normal_font = pygame.font.Font("freesansbold.ttf", 15)
    textSurf, textRect = text_objects("Normal", normal_font)
    textRect.center = ((350+50), (450 + 25))
    dis.blit(textSurf, textRect)
    
    #Hard Button
    if 550+100 > mouse[0] > 550 and 450+50 > mouse[1] > 450:
        pygame.draw.rect(dis, LIGHTRED,(550,450,100,50))
    else:
        pygame.draw.rect(dis, RED,(550,450,100,50))
    
    normal_font = pygame.font.Font("freesansbold.ttf", 15)
    textSurf, textRect = text_objects("Hard", normal_font)
    textRect.center = ((350+50), (450 + 25))
    dis.blit(textSurf, textRect)
    pygame.display.update()
    
    #Buttons end
    pygame.display.update()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:

                if event.key == K_p:
                    game_loop()
                elif event.key == K_s:
                    settings_screen()
        
        CLOCK.tick(FPS)


    
def game_over():
    
    font = pygame.font.Font(FONT, 60)
    play_font = pygame.font.Font(FONT, 30)

    font_surface = font.render("GAME OVER", True, WHITE)
    play_surface = play_font.render("Press P to play again", True, WHITE)

    rect_font = font_surface.get_rect()
    play_rect_font = play_surface.get_rect()

    rect_font.center = ((DISPLAYX / 2), (DISPLAYY / 2.5))
    play_rect_font.center = ((DISPLAYX / 1.95), (DISPLAYY / 1.75))

    dis.blit(font_surface, rect_font)
    dis.blit(play_surface, play_rect_font)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    game_loop()
        CLOCK.tick(FPS)
    
def settings_screen():

    color_orders = [BLUE, RED, GREEN, YELLOW]
    font = pygame.font.Font(FONT, 40)
    small_font = pygame.font.Font(FONT, 23)
    
    settings_surf = dis.convert_alpha()
    font_surface = font.render("SETTINGS", True, BLACK)
    escape_surface = small_font.render("Press ESC or S to Escape", True, BLACK)
    color_option_text_surface = small_font.render("Color: ", True, BLACK)


    settings_background_rect = pygame.Rect(DISPLAYX / 6, DISPLAYY / 6, DISPLAYX / 1.5, DISPLAYY - DISPLAYY / 5)
    color_rect = pygame.Rect(DISPLAYX / 2, DISPLAYY / 2.15, BOX_SIZE * 1.25, BOX_SIZE * 1.25)
    rect_font = font_surface.get_rect()
    escape_rect_font = escape_surface.get_rect()
    color_option_font_rect = color_option_text_surface.get_rect()



    rect_font.center = ((DISPLAYX / 2), (DISPLAYY / 4))
    escape_rect_font.center = ((DISPLAYX / 2), (DISPLAYY / 3))
    color_option_font_rect.center = ((DISPLAYX / 3), (DISPLAYY / 2))
    draw_game_area()

    pygame.draw.rect(settings_surf, TRANSPARENTWHITE, settings_background_rect)
    pygame.draw.rect(settings_surf, color_orders[0], color_rect)

    dis.blit(settings_surf, (0, 0))
    dis.blit(color_option_text_surface, color_option_font_rect)
    dis.blit(font_surface, rect_font)
    dis.blit(escape_surface, escape_rect_font)
    
    pygame.display.update()
    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s or event.key == pygame.K_ESCAPE:
                    #Exit setting screen
                    start_screen()

            CLOCK.tick(FPS)
def main():

    while True:
        start_screen()
        # game_loop()
    
main()
