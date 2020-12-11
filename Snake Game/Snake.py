class SnakeBody:
    def __init__(self,root):
        self.root=root  #a list of direction and position
        self.child=None

class Snake(SnakeBody):
    def __init__(self,root):
        super(Snake,self).__init__(root) 
        self.size=1 
    
    
    def oneating_food(self,obj=None):
        if obj is None:
            obj=self
        if obj.child is None:
            self.size += 1
            self.addnewbodytolist()
        else:
            self.oneating_food(obj.child)
    
    def oneatingspecial_food(self,obj=None):
        if obj is None:
            obj=self
        if self.size<4:  #if the size of the snake is lees than 4 only deduces snake size by one
            # if self.size==2:
            #     obj.child=None
            #     self.size -= 1
            # elif obj.child.child is None:
            #     obj.child=None #pthon will automatically free the memory 
            #     self.size -= 1 
            # if self.size==2:
            #     self.delete1nodeatend()
            # else:
            #     self.oneatingspecial_food(obj.child)
            self.delete1nodeatend()
        else:
            self.delete2nodesatend()

    def delete2nodesatend(self,obj=None,Counter=0):
        if obj is None:
            obj=self
        Counter += 1
        if self.size-2==Counter:  #delete 2 elements of the child 
            self.size=self.size-2
            obj.child=None
        else:
            self.delete2nodesatend(obj.child,Counter)
    
    def delete1nodeatend(self,obj=None,Counter=0):
        if obj is None:
            obj=self
        Counter += 1
        if self.size-1==Counter:  #delete 1 elements of the child 
            obj.child=None
            self.size -= 1
        else:
            self.delete1nodeatend(obj.child,Counter)
    
    def addnewbodytolist(self,obj=None):
        if obj is None:
            obj=self
        if obj.child is None:
            if obj.root[2]:
                obj.child=SnakeBody([obj.root[0]+20,obj.root[1],obj.root[2],obj.root[3]])
            elif obj.root[3]:
                obj.child=SnakeBody([obj.root[0],obj.root[1]-20,obj.root[2],obj.root[3]])
            elif not obj.root[2]:
                obj.child=SnakeBody([obj.root[0]-20,obj.root[1],obj.root[2],obj.root[3]])
            else:
                obj.child=SnakeBody([obj.root[0],obj.root[1]+20,obj.root[2],obj.root[3]])
        else:
            self.addnewbodytolist(obj.child)
            

    def getpositionofroot(self):
        return self.root
    
    def validcontrol(self,cord1,cord2):
        if cord1[0]==2 and cord2[0]==1:
            return False
        if cord1[0]==1 and cord2[0]==2:
            return False 
        if cord1[1]==3 and cord2[1]==4:
            return False
        if cord1[1]==4 and cord2[1]==3:
            return False
        return True

    def movementofsnake(self,positionx_y):
        x_direction,y_direction=self.getpositionofroot()[:2]
        x_dir,y_dir=self.getpositionofroot()[2:]
        valid=self.validcontrol(positionx_y,[x_dir,y_dir])
        if valid and positionx_y[0]==1:
            mainroot=Snake(root=[x_direction+20,y_direction,positionx_y[0],positionx_y[1]])
        elif valid and positionx_y[0]==2:
            mainroot=Snake(root=[x_direction-20,y_direction,positionx_y[0],positionx_y[1]])
        elif valid and positionx_y[1]==3:
            mainroot=Snake(root=[x_direction,y_direction-20,positionx_y[0],positionx_y[1]])
        elif valid and positionx_y[1]==4:
            mainroot=Snake(root=[x_direction,y_direction+20,positionx_y[0],positionx_y[1]])
        else:
            if x_dir==1:
                x_direction += 20
                mainroot=Snake(root=[x_direction,y_direction,x_dir,y_dir])
            elif x_dir==2:
                x_direction -= 20
                mainroot=Snake(root=[x_direction,y_direction,x_dir,y_dir])
            elif y_dir==3:
                y_direction -= 20
                mainroot=Snake(root=[x_direction,y_direction,x_dir,y_dir])
            elif y_dir==4:
                y_direction += 20
                mainroot=Snake(root=[x_direction,y_direction,x_dir,y_dir])
            else:
                mainroot=Snake(root=[x_direction,y_direction,x_dir,y_dir])
        mainroot.size=self.size
        if self.child:
            temporary=self.child
            newsubnode=SnakeBody(self.root)
            newsubnode.child=temporary
            mainroot.child=newsubnode
        self=mainroot
        self.size += 1
        self.delete1nodeatend()
        return self