from Snake import Snake 
from Graphics import GameGraphics
import random
import pygame
class GameControl:
    def __init__(self,Name,screensize=(800,600),run=True):
        self.snake=Snake([screensize[0]/2,screensize[1]/2,1,0])
        self.Graphics=GameGraphics(Name,screensize)
        self.run=run
        self.foodplaces=list()
        self.nooffood=0
    def playerupdate(self):   #also check the snake is collided or not
        temporary=self.snake
        for i in range(self.snake.size):
            row,column=temporary.root[:2]
            self.Graphics.snakeimage(row,column)
            temporary=temporary.child
    
    def createfood(self):
        if len(self.foodplaces)==0:
            multiple_x=random.randint(0,39)
            multiple_y=random.randint(0,29)
            if self.nooffood<5:
                self.nooffood += 1
                self.foodplaces.append([multiple_x*20,multiple_y*20,1])
            else:
                self.nooffood=0
                self.foodplaces.append([multiple_x*20,multiple_y*20,2])

    def collisioncheck(self):
        temporary=self.snake
        x,y=self.snake.root[:2]
        if x>=self.Graphics.screensize[0]-1 or x<0:
            self.end()
        if y>=self.Graphics.screensize[1]-2 or y<0:
            self.end()
        for i in range(self.snake.size):
            row,column=temporary.root[:2]
            temporary=temporary.child
            if i>=1:
                if x==row and y==column:
                    self.end()

    def foodeaten(self):
        x_snakehead,y_snakehead=self.snake.getpositionofroot()[:2]
        for i in range(len(self.foodplaces)):
            x_food,y_food,value=self.foodplaces[i]
            if x_food==x_snakehead and y_food==y_snakehead:
                if value==1:
                    self.snake.oneating_food()
                else:
                    self.snake.oneatingspecial_food()
                self.foodplaces.pop(i) 

    def screenupdate(self):
        self.Graphics.screen.fill((0,0,0))
        keys=self.Graphics.checkforkeys()
        if keys[pygame.K_LEFT]:
            self.snake=self.snake.movementofsnake(positionx_y=(2,0))
        elif keys[pygame.K_RIGHT]:
            self.snake=self.snake.movementofsnake(positionx_y=(1,0))
        elif keys[pygame.K_UP]:
            self.snake=self.snake.movementofsnake(positionx_y=(0,3))
        elif keys[pygame.K_DOWN]:
            self.snake=self.snake.movementofsnake(positionx_y=(0,4))
        else:
            self.snake=self.snake.movementofsnake(positionx_y=(0,0))
        self.Graphics.boardpattern()
        self.createfood()
        self.playerupdate()
        self.collisioncheck()
        for i in self.foodplaces:
            self.Graphics.drawfood(i[2],i[:2])
        self.foodeaten()
        self.Graphics.update()
    
    def start(self):
        self.Graphics.start()
    
    def end(self):
        self.Graphics.end()
    
    