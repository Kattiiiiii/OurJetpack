#load images
#pyg.image.load('image_name.png')

from re import X
import pygame as pyg
import os
import math
pyg.init()


#initialize game screen
screen = pyg.display.set_mode((1024, 768))
pyg.display.set_caption('Jumping Jet')

# Lists of images
running = [pyg.image.load(os.path.join("Img1/chuck_norris", "walk1.png")), pyg.image.load(os.path.join("Img1/chuck_norris", "walk2.png"))]
jumping = [pyg.image.load(os.path.join("Img1/chuck_norris", "steve1.png")), pyg.image.load(os.path.join("Img1/chuck_norris", "beggining.png")), pyg.image.load(os.path.join("Img1/chuck_norris", "flying1.png"))] #
dying = [pyg.image.load(os.path.join("Img1/chuck_norris", "dead.png")), pyg.image.load(os.path.join("Img1/chuck_norris", "end.png"))]
obsticle = [pyg.image.load(os.path.join("Img1/obsticle", "zap.png")), pyg.image.load(os.path.join("Img1/obsticle", "zap1.png")), pyg.image.load(os.path.join("Img1/obsticle", "zap2.png")), pyg.image.load(os.path.join("Img1/obsticle", "zap3.png")), pyg.image.load(os.path.join("Img1/obsticle", "zap4.png"))]
bg = pyg.image.load(os.path.join("Img1", "bg6.jpg"))

# the class Chuck operates the player chuck Norris and makes him run jump and so on.
class Chuck:
    x_pos = 80
    y_pos = 600 # we need to change(add) the hight of the ground
    max_vel = 1.5
    h_counter = 1   

    # we initialize the starting point, where chuck runns and reset the model.
    def __init__(self):
        self.chuck_img = running
        self.jump_img = jumping
        self.die_img = dying

        self.chuck_run = True
        self.chuck_jump = False
        self.chuck_die = False
        
        self.step_index = 0
        self.count_h = self.h_counter
        self.jet_engine = self.max_vel
        self.image = self.chuck_img[0]
        self.chuck_rect = self.image.get_rect()
        self.chuck_rect.x = self.x_pos
        self.chuck_rect.y = self.y_pos

    # for every update we check, if chucks state has changed and if so, we call the connected function
    def update (self, userInput):
        if self.chuck_run:
            self.run()
        if self.chuck_jump:
            pass
            # self.jump()
        if self.chuck_die:
            self.die()

        if self.step_index >= 10:
            self.step_index = 0

        # changing the position and visualisation of chuck
        if userInput[pyg.K_SPACE]:
            self.chuck_run = False
            self.chuck_jump = True
            self.chuck_die = False
            self.jump()

        if self.chuck_rect.y <= 0 and userInput[pyg.K_SPACE]:
            self.chuck_rect.y = 0
            self.h_counter = 0
            pass 
        elif self.y_pos >= 599:
            self.fall()


        if self.chuck_rect.y >= 601: # we need to add 'the dying of' chuck as a bool
            self.chuck_run = True
            self.chuck_jump = False
            self.chuck_die = False

    # if chuck has to run on the spot, we go threw the list of images and increase the step index
    def run(self):
        self.image = self.chuck_img[self.step_index // 5]
        self.chuck_rect = self.image.get_rect()
        self.chuck_rect.x = self.x_pos
        self.chuck_rect.y = self.y_pos
        self.step_index += 1
        self.h_counter = 0

    # if the user presses space, the player jumps in the air with the jetpack
    def jump(self):
        self.image = self.jump_img[self.step_index // 5]
        if self.h_counter < 30:
            self.h_counter += 3 
        self.chuck_rect.y -= self.jet_engine + (self.h_counter * 15) #* math.e ** 3

    def fall(self):
        if self.h_counter > -30:
            self.h_counter -= 3 
        self.chuck_rect.y -= self.jet_engine + (self.h_counter)

    # we need to add the death
    def die():
        pass

    # blits the image to the screen
    def draw(self, screen):
        screen.blit(self.image, (self.chuck_rect.x, self.chuck_rect.y))


#Game loop
def main():
    # for the backround
    global game_speed, x_pos_bg, y_pos_bg, meters
    run = True
    clock = pyg.time.Clock()
    player = Chuck()
    game_speed = 14
    meters = 0
    font= pyg.font.Font('freesansbold.ttf', 20)

    # keeps trakc of the score and increases the speed when the game continues for some time
    def score():
        global game_speed, meters
        meters += 1
        if meters % 100 == 0:
            game_speed += 1

        text = font.render("M" + str(meters), True, (255, 255, 0))
        textRect = text.get_rect()
        textRect.center = (500, 65)
        screen.blit(text, textRect)


    # backround
    x_pos_bg = 0
    y_pos_bg = 0

    # a function to create the backround according to the game speed
    def backround():
        global x_pos_bg, y_pos_bg
        image_width = bg.get_width()
        screen.blit(bg, (x_pos_bg, y_pos_bg))
        screen.blit(bg, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            screen.blit(bg, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_speed

    # continue running untill chuck dies
    while run:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                run = False
        
        screen.fill((0,0,0))
        userInput = pyg.key.get_pressed()

        backround()

        score()

        player.draw(screen)
        player.update(userInput)


        clock.tick(30)
        pyg.display.update()


'''
#keep game running till user quit the game
playingGame = True
while playingGame:

    #check for events in queue
    for event in pyg.event.get():
        #if game is of type quit, quit game  
        if event.type == pyg.QUIT:  
           playingGame = False

    #defining background color
    color = (0,0,0)
    screen.fill(color)
    pyg.display.flip()

'''

# we need to call the main to start the game
main()