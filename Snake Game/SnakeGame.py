from GameControl import GameControl
import pygame

if __name__=='__main__':
    gamecontrolflow=GameControl("Snake Game")
    gamecontrolflow.start()
    while gamecontrolflow.run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gamecontrolflow.run=False
        gamecontrolflow.screenupdate()
    gamecontrolflow.end()