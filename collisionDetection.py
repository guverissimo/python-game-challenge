import pygame, sys, random
from pygame.locals import *

# Set up pygame.
pygame.init()
mainClock = pygame.time.Clock()

# Set up the window.
WINDOWWIDTH = 800
WINDOWHEIGHT = 600
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Challenge | Sprint 2')
screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

# Set up the colors.
BLACK = (0, 0, 0)
PURPLE = (190, 3, 252)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BG_COLOR = (28, 22, 46)
font = pygame.font.Font(None, 28)
TEXT = (0, 191, 224)

# Set up the player and food data structure.
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# Run the game loop.

def game():
    points = 0
    foodCounter = 0
    NEWFOOD = 40
    FOODSIZE = 20
    player_width = 30
    player = pygame.Rect(300, 300, 30, 30)
    foods = []
    for i in range(15):
        foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))
        
    

    # Set up movement variables.
    moveLeft = False
    moveRight = False
    moveUp = False
    moveDown = False

    movespeed = 4

    while True:
        screen.fill(BLACK)
        mx, my = pygame.mouse.get_pos()
        draw_text('Menu (F1)', font, WHITE, screen, 20, WINDOWHEIGHT -30)
        draw_text('Velocidade: ', font, WHITE, screen, 150, WINDOWHEIGHT - 30)
        draw_text(f'{int(movespeed)}', font, WHITE, screen, 270, WINDOWHEIGHT -30)
        draw_text('Pontos: ', font, WHITE, screen, 400, WINDOWHEIGHT - 30)
        draw_text(f'{points} ', font, WHITE, screen, 480, WINDOWHEIGHT - 30)

    # Check for events.
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_F1:
                    main_menu()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                # Change the keyboard variables.
                if event.key == K_LEFT or event.key == K_a:
                    moveRight = False
                    moveLeft = True
                if event.key == K_RIGHT or event.key == K_d:
                    moveLeft = False
                    moveRight = True
                if event.key == K_UP or event.key == K_w:
                    moveDown = False
                    moveUp = True
                if event.key == K_DOWN or event.key == K_s:
                    moveUp = False
                    moveDown = True
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_LEFT or event.key == K_a:
                    moveLeft = False
                if event.key == K_RIGHT or event.key == K_d:
                    moveRight = False
                if event.key == K_UP or event.key == K_w:
                    moveUp = False
                if event.key == K_DOWN or event.key == K_s:
                    moveDown = False
                if event.key == K_x:
                    player.top = random.randint(0, WINDOWHEIGHT - player.height)
                    player.left = random.randint(0, WINDOWWIDTH - player.width)

            # if event.type == MOUSEBUTTONUP:
            #     foods.append(pygame.Rect(event.pos[0], event.pos[1], FOODSIZE, FOODSIZE))

        foodCounter += 1
        if foodCounter >= NEWFOOD:
            # Add new food.
            if len(foods) <= 15:
                foodCounter = 0
                foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))

            
        if moveDown:
            player.top += movespeed
            if player.top > WINDOWHEIGHT:
                player.top = 0 - player.height  # Aparece na parte superior
        if moveUp:
            player.top -= movespeed
            if player.top < 0 - player.height:
                player.top = WINDOWHEIGHT  # Aparece na parte inferior
        if moveLeft:
            player.left -= movespeed
            if player.left < 0 - player.width:
                player.left = WINDOWWIDTH  # Aparece no lado direito
        if moveRight:
            player.right += movespeed
            if player.right > WINDOWWIDTH:
                player.left = 0 - player.width  # Aparece no lado esquerdo
            

        # Draw the player onto the surface.
        pygame.draw.rect(windowSurface, PURPLE, player)

        # Check if the player has intersected with any food squares.
        for food in foods[:]:
            if player.colliderect(food):
                foods.remove(food)
                points += 1
                print(f"Pontos: {points} points")
                if movespeed <= 20:
                    movespeed += 0.2;


        # Draw the food.
        for i in range(len(foods)):
            pygame.draw.rect(windowSurface, GREEN, foods[i])
        # Draw the window onto the screen.
        pygame.display.update()
        mainClock.tick(40 )


def main_menu():
    while True:
        
        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        
        screen.fill(BG_COLOR)
        draw_text('Menu Inicial', font, TEXT, screen, 20, 20)

        mx, my = pygame.mouse.get_pos()

        # Draw the buttons     X,  Y   sizes
        button_1 = pygame.Rect(50, 80, 200, 50)
        button_2 = pygame.Rect(50, 140, 200, 50)
        button_3 = pygame.Rect(50, 200, 200, 50)


        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        if button_3.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()

        pygame.draw.rect(screen, (35, 36, 36), button_1)
        pygame.draw.rect(screen, (35, 36, 36), button_2)
        pygame.draw.rect(screen, (35, 36, 36), button_3)

        draw_text('Iniciar', font, WHITE, screen, 70, 90)
        draw_text('Configurações', font, WHITE, screen, 70, 150)
        draw_text('Sair', font, (255,0,0), screen, 70, 210)


        pygame.display.update()
        
def options():
    running = True
    while running:
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.main_menu()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                
        screen.fill((0, 100, 100))
        draw_text('Configurações', font, WHITE, screen, 20, 20)
        
        mx, my = pygame.mouse.get_pos()
              
        button_1 = pygame.Rect(50, 100, 200, 50)
        
        if button_1.collidepoint((mx, my)):
            if click:
                running = False
        


                
        pygame.draw.rect(screen, [255, 0, 0], button_1)
        draw_text('Voltar', font, WHITE, screen, 70, 100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()
main_menu()