from tkinter import *
from time import time, sleep

class instructions:
    
    def __init__(self,root1):
        self.root1 = root1
        w=1280
        h=720
        ws = self.root1.winfo_screenwidth()
        hs = self.root1.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.root1.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.root1.config(bg="#DCFBD3")
        self.root1.title("Instructions")
        self.root1.resizable(0,0)
        sum="*In this version of the game we simulate the basic play of Hand Cricket.You play with the computer as\n  your oppenent and compete to win.\n*Once the game starts you can choose your desired option.\n*The computer will randomly choose it's playing hand and after comparing both hands the result will be\n  displayed."
        bat="a) There are 6 options you can choose from :\n    1.  1 Run\n    2.  2 Run\n    3.  3 Run\n    4.  4 Four!\n    5.  5 Run\n    6.  6 Six!"
        bowl="b) In bowling if you choose the same option as the opponent you get a Wicket!"
        rule="If your score is greater than the opponent or you take all the wickets within the given target, YOU WIN!!!"
        c=Canvas(self.root1,height=700,width=1200,bg="#DCFBD3",bd=0,highlightcolor="#DCFBD3",relief=RIDGE,cursor="ibeam")
        c.create_text(45,20,text="Instructions for playing Hand Cricket:",font=("Comic Sans MS", 24, 'bold'),anchor=NW,fill="#350A08")
        c.create_text(45,80,text=sum,font=("Comic Sans MS", 18),anchor=NW,fill="#350A08")
        c.create_text(50,260,text="Batting & Bowling:",font=("Comic Sans MS", 16,'bold'),anchor=NW,fill="#350A08")
        c.create_text(50,300,text=bat,font=("Comic Sans MS", 14),anchor=NW,fill="#350A08")
        c.create_text(50,500,text=bowl,font=("Comic Sans MS", 14),anchor=NW,fill="#350A08")
        c.create_text(50,550,text=rule,font=("Comic Sans MS", 16,'bold'),anchor=NW,fill="#350A08")
        c.place(x=40,y=10)
        
        def Back():
            self.root1.destroy()
            
        button1 = Button(self.root1,width =10,highlightthickness=1,highlightcolor="black",relief=RAISED,text="Back",bd=1,command=Back)
        button1.config(activebackground="gray",activeforeground="white",cursor="hand2", fg="black", bg="white",font=("Comic Sans MS", 16, 'bold'))
        button1.place(x=100, y=630)
        
        
