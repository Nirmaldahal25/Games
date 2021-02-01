#! /usr/bin/python3
import tkinter as tk

class Graphics(tk.Tk):
    def __init__(self,Name:str,logo:str=None):
        super(Graphics,self).__init__()
        self.title(Name)
        self.photo=tk.PhotoImage(file=logo)
        self.iconphoto(False,self.photo)
        self.myset=list()
        self.myButton=None
        self.board=list()
    def start(self):
        self.setentries()
        self.processentries()
        self.submit()
        self.mainloop()
    
    def setentries(self):
        self.myset=[]
        self.board=[[0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0]]
        for i in range(81):
            self.myset.append(tk.Entry(self,width=10,fg="red"))
	
	    
  
    def processentries(self):
        k=0
        for i,entry in enumerate(self.myset):
            if i%9==0 and i!=0:
                k += 1
            entry.grid(row=k,column=i%9)

    def valid(self,board,validvalue,row,column):
        for i in range(0,9): #check whether the value is valid in row
            if board[row][i]==validvalue:
                return False
        
        for i in range(0,9):    #check whether the value is valid in column
            if board[i][column]==validvalue:
                return False

        row1=row//3  
        column1=column//3
        for i in range(row1*3,row1*3+3):
            for j in range(column1*3,column1*3+3):
                if board[i][j]==validvalue:
                    return False
        return True
    def findnextlocationfor0(self,board):
        for i in range(0,9):
            for j in range(0,9):
                if board[i][j]==0:
                    return i,j
        return None
    
    def solve(self,board):
        findedvalues=self.findnextlocationfor0(board)
        if not findedvalues: 
            return True
        else:
            row,column=findedvalues
        for value in range(1,10): 
            if self.valid(board,value,row,column):
                board[row][column]=value
                if self.solve(board):  
                    return True
                board[row][column]=0 
                                    
        return False 

    def myClick(self):
        row=0
        counter = 0
        for i,entry in enumerate(self.myset):
            value=entry.get()
            if i%9==0 and i!=0:
                row+=1
            if value in {'1','2','3','4','5','6','7','8','9'}:
                counter += 1
                self.board[row][i%9]=int(value)
        if counter>=16:
            # for i in self.board:
            #     print(i)
            self.solve(self.board)
            self.solved()
        else:
            mylabel=tk.Label(self,text="Numbers=[1 to 9] and at least 16 hints").grid(row=12,columnspan=3,column=0)
    
    def submit(self):
        self.myButton=tk.Button(self,text="Solve",pady=10,bg="red",command=self.myClick)
        self.myButton.grid(row=12,column=8)
    
    def restart(self):
        self.myButton.destroy()
        self.start()
    
    def solved(self):
        for entry in self.myset:
            entry.destroy()
        self.myset=[]
        column=0
        for i in range(81):
            if i%9==0 and i!=0:
                column += 1
            self.myset.append(tk.Label(self,text=str(self.board[i%9][column]),width=10).grid(row=[i%9],column=column))
        self.myButton.destroy()
        self.myButton=tk.Button(self,text="Resolve",pady=20,command=self.restart,bg='blue')
        self.myButton.grid(row=12,column=7,columnspan=1)

if __name__=='__main__':
    mainwidget=Graphics("Soduku Solver","./Soduku.png")
    mainwidget.start()
