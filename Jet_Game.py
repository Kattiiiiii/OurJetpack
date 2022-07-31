#load images
#pyg.image.load('image_name.png')

import pygame as pyg
import os
#pyg.init()


#initialize game screen
screen = pyg.display.set_mode((1024, 768))
pyg.display.set_caption('Jumping Jet')

# Lists of images
running = [pyg.image.load(os.path.join("Img1/chuck_norris", "walk1.png")), pyg.image.load(os.path.join("Img1/chuck_norris", "walk2.png"))]
jumping = [pyg.image.load(os.path.join("Img1/chuck_norris", "steve1.png")), pyg.image.load(os.path.join("Img1/chuck_norris", "beggining.png")), pyg.image.load(os.path.join("Img1/chuck_norris", "flying1.png"))]
dying = [pyg.image.load(os.path.join("Img1/chuck_norris", "dead.png")), pyg.image.load(os.path.join("Img1/chuck_norris", "end.png"))]
obsticle = [pyg.image.load(os.path.join("Img1/obsticle", "zap.png")), pyg.image.load(os.path.join("Img1/obsticle", "zap1.png")), pyg.image.load(os.path.join("Img1/obsticle", "zap2.png")), pyg.image.load(os.path.join("Img1/obsticle", "zap3.png")), pyg.image.load(os.path.join("Img1/obsticle", "zap4.png"))]

class Chuck:
    x_pos = 80
    y_pos = 310

    def __init__(self):
        self.chuck_img = running
        self.jump_img = jumping
        self.die_img = dying

        self.chuck_run = True
        self.chuck_jump = False
        self.chuck_die = False
        
        self.step_index = 0
        self.image = self.chuck_img[0]
        self.chuck_rect = self.image.get_rect()
        self.chuck_rect.x = self.x_pos
        self.chuck_rect.y = self.y_pos

    def update (self, userInput):
        if self.chuck_run:
            self.run()
        if self.chuck_jump:
            self.jump()
        if self.chuck_die:
            self.die()

        if self.step_index >= 10:
            self.step_index = 0

        if userInput[pyg.K_SPACE] and not (self.y_pos <= 0):
            self.chuck_run = False
            self.chuck_jump = True
            self.chuck_die = False

        if self.y_pos <= 310: # we need to add 'the dying of' chuck as a bool
            self.chuck_run = True
            self.chuck_jump = False
            self.chuck_die = False

    def run(self):
        self.image = self.chuck_img[self.step_index // 5]
        self.chuck_rect = self.image.get_rect()
        self.chuck_rect.x = self.x_pos
        self.chuck_rect.y = self.y_pos
        self.step_index += 1

    def jump():
        pass

    def die():
        pass

    def draw(self, screen):
        screen.blit(self.image, (self.chuck_rect.x, self.chuck_rect.y))


#Game loop
def main():
    run = True
    clock = pyg.time.Clock()
    player = Chuck()

    while run:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                run = False
        
        screen.fill((0,0,0))
        userInput = pyg.key.get_pressed()

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

main()