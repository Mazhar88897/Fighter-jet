import pygame
import math
from pygame import mixer
import os
import random
from stack import mystack as stack

pygame.init()

WIDTH, HEIGHT = 800, 600
pyInitial = 0
#create the screen
screen = pygame.display.set_mode((WIDTH , HEIGHT))


# Title and Icon
pygame.display.set_caption("Space Fighter")
icon = pygame.image.load(os.path.join('assets', 'icon.png'))
pygame.display.set_icon(icon)


# Background
background = pygame.image.load(os.path.join('assets', 'bg.jpg'))

# Background Music 
mixer.music.load(os.path.join('sounds', 'bgmusic.mp3'))
mixer.music.play(-1)
#operator for bullets and player images
pylist = ["pygame.transform.scale(pygame.transform.rotate(pygame.image.load(os.path.join('assets', 'bullet2.png')), 90), (40, 40))","pygame.transform.scale(pygame.transform.rotate(pygame.image.load(os.path.join('assets', 'bullet1.png')), -90), (40, 40))","pygame.transform.scale(pygame.transform.flip(pygame.image.load(os.path.join('assets', 'player2.png')), False, False), (70,70))","pygame.transform.scale(pygame.transform.flip(pygame.image.load(os.path.join('assets', 'player1.png')), True, False), (70,70))"]
py_stack = stack()
py_stack.multy(pylist)
#Initials for all the both of initial players
Initial = stack()
data_list = ["0","HEIGHT/2 - 35","WIDTH - 90","0","HEIGHT/2 - 35","20"]
Initial.multy(data_list)
#Player 1

player1 = eval(py_stack.pop())
player1X = eval(Initial.pop())
player1Y = eval(Initial.pop())
player1_change = eval(Initial.pop())

#Player 2
player2 = eval(py_stack.pop())
player2X = eval(Initial.pop())
player2Y = eval(Initial.pop())
player2_change = eval(Initial.pop())



#Bot
bot_up = pyInitial
bot_down = pyInitial

#Bullet of PLayer 1
bullet1 = eval(py_stack.pop()) 
bullet1X = pyInitial
bullet1Y = pyInitial
bullet1_change = 1.5
fire1 = True

#Bullet of PLayer 2
bullet2 = eval(py_stack.pop())
bullet2X = pyInitial
bullet2Y = pyInitial
bullet2_change = 1.5
fire2 = True

# Score Variable 
scoreOne = pyInitial
scoreTwo = pyInitial

# Loading Font
font = pygame.font.Font(os.path.join('fonts', 'Gameplay.ttf'), 32)
over_font = pygame.font.Font(os.path.join('fonts', 'Gameplay.ttf'), 70)

# Score display coordinates of player 1
text1X = 20
text1Y = 20

# Score display coordinates of player 2
text2X = WIDTH - 230
text2Y = 20
#Initializing empty stacks
task_1 = stack()
task_2 = stack()

def playerOneMovement(X, Y):
    screen.blit(player1, (X + 15, Y + 15))

def playerTwoMovement(X, Y):
    screen.blit(player2, (X + 15, Y + 15))

def botMovement():
    global bot_up, bot_down
    up_down = random.choice(["UP", "DOWN"])
    if up_down == "UP":
        bot_up += random.randint(35, 70)
    else:
        bot_down += random.randint(35, 70)

def bullet1Movement(X, Y):
    global fire1
    fire1 = False
    task_1.push(fire1)
    task_1.push(X)
    task_1.push(Y)
    screen.blit(bullet1, (X + 45, Y + 22))

def bullet2Movement(X, Y):
    global fire2
    fire2 = False
    task_2.push(fire2)
    task_2.push(X)
    task_2.push(Y)
    screen.blit(bullet2, (X - 15, Y + 22))

def collisionDetectorPlayerOne(b1x, b1y, p2x , p2y):
    global fire1
    global bullet1X 
    global bullet1Y
    
    task_1.multy([bullet1Y,bullet1X,fire1])
    
    if int(math.sqrt(math.pow(p2x - b1x, 2) + math.pow(p2y - b1y, 2))) < 60:
        task_1.pop(),task_1.pop(),task_1.pop() == (True,0,0)
        fire1 = True
        bullet1X = 0
        bullet1Y = 0
        return True
    

def collisionDetectorPlayerTwo(b2x, b2y, p1x, p1y):
    global fire2
    global bullet2X 
    global bullet2Y
     
    task_2.multy([bullet2Y,bullet2X,fire2]) 
    distance = int(math.sqrt(math.pow(b2x - p1x, 2) + math.pow(b2y - p1y, 2)))
    x,y,z = task_2.pop(),task_2.pop(),task_2.pop()
    if distance < 60 and distance > 20:
        (task_2.pop(),task_2.pop(),task_2.pop()) == (True,0,0)
        fire2 = True
        bullet2X = 0
        bullet2Y = 0
        return True
    else:
        
        task_2.clear()
    
def blit_text_center(text, win, color):
    render = font.render(text, 1, color)
    win.blit(render, (WIDTH // 2 - render.get_width() // 2, HEIGHT // 2 - render.get_height() // 2))

def blit_text(text, win, font_size, color, x, y):
    over_font = pygame.font.Font(os.path.join('fonts', 'Gameplay.ttf'), font_size-20)
    render = over_font.render(text, 1, color)
    win.blit(render, (x, y))

def displayScore(X, Y):
    score = font.render("Score : " + str(scoreOne), True, (255, 255, 255))
    screen.blit(score, (X, Y))

def displayScoreTwo(X, Y)   :
    score = font.render("Score : " + str(scoreTwo), True, (255, 255, 255))
    screen.blit(score, (X, Y))

def show_main_menu(win):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        
        if event.type == pygame.KEYDOWN:
              if event.key  == pygame.K_RETURN:
                    return False

    win.blit(background, (0, 0))
    blit_text_center("Press Enter key to begin!", win, (255, 255, 255))
    blit_text("Player  Controls", win, 40, (255, 255, 255), *(10, 10))
    blit_text("up - Move Up", win, 40, (255, 255, 255), *(10, 50))
    blit_text("down - Move Down", win, 40, (255, 255, 255), *(10, 90))
    blit_text("SPACE - Action key", win, 40, (255, 255, 255), *(10, 130))
    
    pygame.display.update()
    
    return True

def show_game_mode_menu(win):
    """
    It returns a tuple of two bool, the first index is the bool for the multiplayer while the second is the bool for the game mode menu
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        
        if event.type == pygame.KEYDOWN:
            if event.key  == pygame.K_SPACE:
                return False, False
           


    win.blit(background, (0, 0))
    blit_text("GET READY FOR RIDE", win, 50, (255, 255, 255), *(210, 230))
    blit_text("Press space key to start the game and beware of fighter jets", win, 40, (255, 255, 255), *(20, 270))
    pygame.display.update()
    
    return False, True 

def gameover():
    global scoreOne
    global scoreTwo
    blit_text(f"GAMEOVER", screen, 60, (255, 255, 255), 270, 230)

    if scoreOne == 3:
        win_sound = mixer.Sound(os.path.join('sounds', 'win.wav'))
        win_sound.play()  
        blit_text_center(f"HURRAHHH!!! YOU WON", screen, (255, 255, 255))
        
    elif scoreTwo == 3:
        blit_text_center(f"YOU LOSE", screen, (255, 255, 255))
        lose_sound = mixer.Sound(os.path.join('sounds', 'lose.wav'))
        lose_sound.play() 
    
    scoreOne = 0
    scoreTwo = 0

running = True
main_menu = True
game_mode = True
Xgame = True
while running:
    
    #Backgroung Image 
    screen.blit(background, (0, 0))

    #Main Menu 
    if main_menu:
        main_menu = show_main_menu(screen)
        continue
    
    #Game Mode Menu
    if game_mode:
        game_mode_menu = show_game_mode_menu(screen)
        game_mode = game_mode_menu[1]
        
        continue

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             running = False
        
        #Movement Detection for player 1
        if event.type == pygame.KEYDOWN:
              if event.key  == pygame.K_UP:
                  player1_change = -1
               
              if event.key == pygame.K_DOWN:
                  player1_change = +1

              if event.key == pygame.K_SPACE:
                  if fire1 is True:
                    fire1_sound = mixer.Sound(os.path.join('sounds', 'fire1.mp3'))
                    fire1_sound.play()
                    bullet1X = player1X
                    bullet1Y = player1Y
                    bullet1Movement(bullet1X, bullet1Y)
                    
        if event.type == pygame.KEYUP:
              if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                 player1_change = 0

        
    
    if bot_up > 0 and bot_down == 0:
            player2_change = -1
            bot_up -= 1
    elif bot_up <= 0 and bot_down == 0:
             botMovement()
      
        
    if bot_up % 2 == 0:
            if fire2 is True:
                fire2_sound = mixer.Sound(os.path.join('sounds', 'fire1.mp3'))
                fire2_sound.play()  
                bullet2X = player2X
                bullet2Y = player2Y
                bullet2Movement(bullet2X, bullet2Y)
                
            if bot_down > 0 and bot_up == 0:
                player2_change = +1
                bot_down -= 1
            elif bot_down <= 0 and bot_up == 0:
                botMovement()
        
       
    #Movement Calculation for player 1
    player1Y += player1_change 

    if player1Y <= 70:
        player1Y = 70
    
    if player1Y >= HEIGHT-90:
        player1Y = HEIGHT-90
    
    #Movement Calculation for player 2
    player2Y += player2_change 

    if player2Y <= 70:
        player2Y = 70
    
    if player2Y >= HEIGHT-90:
        player2Y = HEIGHT-90

    # Bullet Movement for player 1 
    if bullet1X >= WIDTH :
        fire1 = True

    if fire1 is False:
        bullet1Movement(bullet1X, bullet1Y)    
        bullet1X += bullet1_change
        
    
    # Bullet Movement for player 2
    if bullet2X <= 0:
        fire2 = True

    if fire2 is False:
        bullet2Movement(bullet2X, bullet2Y)    
        bullet2X -= bullet2_change
        
    #Checking for Collision 
    if collisionDetectorPlayerOne(bullet1X, bullet1Y, player2X, player2Y) is True:
       scoreOne += 1
       c_sound = mixer.Sound(os.path.join('sounds', 'hit.mp3'))
       c_sound.play() 

    if collisionDetectorPlayerTwo(bullet2X, bullet2Y, player1X, player1Y) is True:
       scoreTwo += 1
       c_sound = mixer.Sound(os.path.join('sounds', 'hit.mp3'))
       c_sound.play() 

    
    displayScore(text1X, text1Y)
    displayScoreTwo(text2X, text2Y)
    playerOneMovement(player1X, player1Y)
    playerTwoMovement(player2X, player2Y)

    #To slow down the movement of the bot and the bullet (Because the bot is overpowered) when in single player
    if  Xgame:
        pygame.display.update()

    #Checking for Who Won
    if scoreOne == 3 or scoreTwo == 3:
        gameover()
        pygame.display.update()
        pygame.time.delay(4000)
        main_menu = game_mode = True
        bot_up = bot_down = 0
        player1Y = player2Y = HEIGHT/2 - 35
        playerOneMovement(player1X, player1Y)
        playerTwoMovement(player2X, player2Y)
    
    pygame.display.update() 