import pygame 
class GameGraphics:
    #screensize is a tuple or a list and run is boolean 
    def __init__(self,Name,screensize):
        self.Name=Name
        self.screensize=[screensize[0]+1,screensize[1]+1]
        self.screen=None
        self.board=list()
        for i in range(0,self.screensize[1]+1,20):
            self.board.append([(0,i),(800,i)])
        for i in range(0,self.screensize[0]+1,20):
            self.board.append([(i,0),(i,600)])
    def checkforkeys(self):
        keys=pygame.key.get_pressed()
        return keys
    def start(self):
        pygame.init()
        pygame.display.set_caption(self.Name) #Name of Window
        self.screen=pygame.display.set_mode(self.screensize)
    def boardpattern(self):
        for board in self.board:
            pygame.draw.lines(self.screen,(255,255,255),closed=True,points=board)
    
    def snakeimage(self,row,column):
        rectangleobject=pygame.Rect(row,column+2,20,16)    #position x,y width height
        pygame.draw.rect(self.screen,(0,255,0),rectangleobject)
    
    def drawfood(self,color,position):
        if color==1:
            color=(0,0,255) #blue
        if color==2:
            color=(255,0,0) #red
        pygame.draw.circle(self.screen,color,(position[0]+10,position[1]+10),8)

    def end(self):
        pygame.quit()
        exit()

    def update(self):
        pygame.display.update()
        # pygame.display.flip()