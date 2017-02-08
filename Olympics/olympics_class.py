import pygame
import time

pygame.init()

black = [0, 0, 0]
white = [255, 255, 255]
green = [0, 255, 0]
brown = [128, 64, 0]

screen_width = 600
screen_height = 900

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("OLYMPICS")

player_boy = pygame.image.load('blue_blob.png')
player_girl = pygame.image.load('pink_blob.png')


timer = 10


def count_down(count):
    if count < 2:
        go = font.render("GO", 1, black)
        screen.blit(go, (400, 50))
        screen.blit(go, (200, 50))
    count = count - 1
    time.sleep(1)
    return count
    

def display(message):
    font = pygame.font.Font(None, 36)
    text = font.render(message, 1, black)
    screen.blit(text, (350, 0))

def field():
    screen.fill(brown)
    pygame.draw.line(screen, white, [0, 50], [600,50],5)
    pygame.draw.line(screen, white, [0, 850], [600,850],5)
    pygame.draw.line(screen, white, [300, 50], [300,850],5)
    pygame.draw.line(screen, white, [50, 0], [50,900],5)#left
    pygame.draw.line(screen, white, [550, 0], [550,900],5)#right
    pygame.draw.line(screen, green, [0, 0], [0,900],95)
    pygame.draw.line(screen, green, [600, 0], [600,900],95)
    

class Players():
    
    def __init__(self,x,y,player):
        self.x = x
        self.y = y
        self.player = player

    def draw(self,screen):
        player_rectangle = self.player.get_rect()
        self.player_rectangle = player_rectangle
        player_rectangle.move_ip(self.x, self.y)
        screen.blit(self.player,(self.x,self.y))

    def left(self):
        if timer > 0:
            self.x += 0
            self.y -= 0
        elif timer <= 0:
            self.x -= 5
            self.y -= 5

    def right(self):
        if timer > 0:
            self.x += 0
            self.y -= 0
        elif timer <= 0:
            self.x += 5
            self.y -= 5

    def position_one(self):
        if self.x < 300:
            self.x = 300
        elif self.x > screen_width - 50 - self.player_rectangle.width:
            self.x = screen_width - 50 - self.player_rectangle.width
        elif self.y < 0:
            self.y = 0
        elif self.y > screen_height - self.player_rectangle.height:
            self.y = screen_height - self.player_rectangle.height

    def position_two(self):
        if self.x < 50:
            self.x = 50
        elif self.x > screen_width -300 - self.player_rectangle.width:
            self.x = screen_width - 300 - self.player_rectangle.width
        elif self.y < 0:
            self.y = 0
        elif self.y > screen_height - self.player_rectangle.height:
            self.y = screen_height - self.player_rectangle.height

clock = pygame.time.Clock()

pygame.display.set_caption("Instructions screen!")

font = pygame.font.Font(None, 30)

display_instructions = True

instruction_page = 1

while display_instructions:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            instruction_page += 1
            if instruction_page == 3:
                display_instructions = False

    if instruction_page == 1:
        screen.fill(black)
        text = font.render("Instructions", True, white)
        screen.blit(text,[0,0])
        text_two = font.render("First one across the line wins!", True, white)
        screen.blit(text_two,[0,50])
        text_three = font.render("Click to continue", True, white)
        screen.blit(text_three,[0,100])

    elif instruction_page == 2:
        screen.fill(black)
        text = font.render("Left player use Z and C to run", True, white)
        screen.blit(text,[0,0])
        text_two = font.render("Right player use left and right arrow keys to run", True, white)
        screen.blit(text_two,[0,50])
        text_three = font.render("Click to start game", True, white)
        screen.blit(text_three,[0,100])



    clock.tick(20)

    pygame.display.update()
        

done = False
game_over = False
    
boy = Players(400,810,player_boy)
girl = Players(160,810,player_girl)

while not done:
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                boy.left()
            elif event.key == pygame.K_RIGHT:
                boy.right()
            if event.key == pygame.K_z:
                girl.left()
            elif event.key == pygame.K_c:
                girl.right()

  
    field()
    boy.draw(screen)
    boy.position_one()
    girl.draw(screen)
    girl.position_two()             
    font = pygame.font.Font(None, 40)
    font_two = pygame.font.Font(None, 80)
    text1 = font.render("START",True, white)
    text2 = font.render("FINISH", True, white)
    text3 = font.render("YOU WIN", True, white)
    text4 = font_two.render("GAME OVER", True, green)
    screen.blit(text2, [250, 0])
    screen.blit(text1, [250,865])
    
    if boy.y <= 15:
        screen.blit(text3,[350,100])
        if boy.y == 0:
            game_over = True
    if girl.y <= 15:
        screen.blit(text3,[100,100])
        if girl.y == 0:
            game_over = True
    if game_over == True:
        screen.fill(black)
        screen.blit(text4,[120, screen_height / 2])
    if timer >= 1:
        timer = count_down(timer)
    
    display("Ready Steady:" + str(timer))

    clock.tick(30)
    pygame.display.update()
    
pygame.quit()










































