#load images
#pyg.image.load('image_name.png')

import pygame as pyg
pyg.init()


#initialize game screen
screen = pyg.display.set_mode((400,300))
pyg.display.set_caption('Jumping Jet')

#Game loop

#keep game running till user quit the game
playingGame = True
while playingGame:

    #check for events in queue
    for event in pyg.event.get():
        #if game is of type quit, quit game  
        if event.type == pyg.QUIT:  
           playingGame = False

    #defining background color
    color = (255,255,0)
    screen.fill(color)
    pyg.display.flip()
    
# hier ein kommentar von Ole

