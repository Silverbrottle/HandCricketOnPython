from tkinter import *
from random import randint
from Scores import database
import time
from PIL import ImageTk,Image
    
class play():
    def __init__(self,top):
        self.pname=StringVar()
        self.top= top
        self.pscore=0
        self.worl=""
        self.hc=0
        self.cen=0
        self.fr=0
        self.si=0
        self.score=0
        self.w=0
        self.c=0
        self.target=0
        w=1280
        h=720
        ws = self.top.winfo_screenwidth()
        hs = self.top.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.top.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.top.config(bg='white')
        self.top.title("Play!!!")
        self.top.resizable(0,0)
        
        str1=StringVar()
        str1="Computer has choosen.\nWaiting for your Turn"
        c2=Canvas(self.top,bg="white",height=100,width=450)
        c2.pack()
        c1=Canvas(self.top,bg="white",height=720,width=1280)
        c1.pack()
        
        def enter():
            self.pname=nam.get()
            print(self.pname)
            c2.destroy()
        le=Label(c2,text="Enter Playername:",font=("Comic Sans MS", 16, 'bold'),bg="white",fg="black")
        le.place(x=10,y=20)
        nam=Entry(c2,bg="white",textvariable=self.pname,fg="black",font=("Comic Sans MS", 16),width=15)
        nam.place(x=210,y=20)
        enterb= Button(c2,width =5,relief=RAISED,text="Enter",bd=1,command=enter)
        enterb.config(highlightthickness=0,highlightcolor="#FB028D",activebackground="white",
                       activeforeground="#F22C2C",cursor="hand2", fg="white", bg="#F22C2C",font=("Helvetica", 16, 'bold'))
        enterb.place(x=60, y=60)
        
        batsman = ImageTk.PhotoImage(Image.open("batsman6.jpg"))
        self.top.batsman=batsman
        batpic=c1.create_image(660,0,image=batsman,anchor=NW)

        bowler = ImageTk.PhotoImage(Image.open("bowlerog3.jpg"))
        self.top.bowler=bowler
        bowlpic=c1.create_image(0,0,image=bowler,anchor=NW)
        
        filename = PhotoImage(file='giphy2.gif',format = 'gif -index 1')
        self.top.filename=filename
        def loading():
            self.f1=c1.create_image(400,325,image=filename,anchor=NW)
        loading()
        
        c1.create_line(640,0,640,445,fill="#F97C07")
        c1.create_line(660,0,660,445,fill="#0761F9")
        c1.create_line(640,550,640,720,fill="#F97C07")
        c1.create_line(660,505,660,720,fill="#0761F9")

        four=c1.create_text(800,150,fill="#F907B6",font="Times 26 italic bold",text="")
        six=c1.create_text(800,150,fill="#F907B6",font="Times 26 italic bold",text="")

        l1=Label(c1,text="Computer",font=("Comic Sans MS", 20, 'bold'),bg="white",fg="black")
        l1.place(x=300,y=50)
        l2=Label(c1,text="Player",font=("Comic Sans MS", 20, 'bold'),bg="white",fg="black")
        l2.place(x=850,y=50)
        l3=Label(c1,text=str1,font=("Comic Sans MS", 20),bg="white",fg="black")
        l3.place(x=300,y=250)
        scoreLabel=Label(c1,text="",font=("Comic Sans MS", 20),bg="white",fg="#F907B6")
        scoreLabel.place(x=690,y=350)
        wicketLabel=Label(c1,text="",font=("Comic Sans MS", 20),bg="white",fg="#F907B6")
        wicketLabel.place(x=375,y=350)

        tagp=Label(c1,text="Player",font=("Comic Sans MS", 20),bg="white",fg="#F97C07")
        tagp.place(x=680,y=450)
        tagd=Label(c1,text="VS",font=("Comic Sans MS", 20),bg="white",fg="black")
        tagd.place(x=630,y=450)
        tagc=Label(c1,text="Computer",font=("Comic Sans MS", 20),bg="white",fg="#0761F9")
        tagc.place(x=500,y=450)
        tag2=Label(c1,text="",justify=LEFT,font=("Comic Sans MS", 24),bg="white",fg="#F97C07")
        tag2.place(x=580,y=500)
        tag3=Label(c1,text="",font=("Comic Sans MS", 24),bg="white",fg="#0761F9")
        tag3.place(x=660,y=500)
        tag4=Label(c1,text="-",font=("Comic Sans MS", 24),bg="white",fg="black")
        win=Label(c1,text="YOU WIN!!!",font=("Comic Sans MS", 30),bg="white",fg="#0761F9")
        lose=Label(c1,text="YOU LOST!!!",font=("Comic Sans MS", 30),bg="white",fg="red")  
        
        def Back():
            self.top.destroy()

        def fsclear():
            c1.itemconfig(four,text="")
            c1.itemconfig(six,text="")
            
        def Run1():
            if(self.c==3):
                bowling(1)
            else:
                batting(1)
        def Run2():
            fsclear()
            if(self.c==3):
                bowling(2)
            else:
                batting(2)
        def Run3():
            fsclear()
            if(self.c==3):
                bowling(3)
            else:
                batting(3)
        def Run4():
            fsclear()
            if(self.c==3):
                bowling(4)
            else:
                batting(4)
        def Run5():
            fsclear()
            if(self.c==3):
                bowling(5)
            else:
                batting(5)
        def Run6():
            fsclear()
            if(self.c==3):
                bowling(6)
            else:
                batting(6)
        def disable():
            button1.config(state=DISABLED)
            button2.config(state=DISABLED)
            button3.config(state=DISABLED)
            button4.config(state=DISABLED)
            button5.config(state=DISABLED)
            button6.config(state=DISABLED)
        def enable():
            button1.config(state=NORMAL)
            button2.config(state=NORMAL)
            button3.config(state=NORMAL)
            button4.config(state=NORMAL)
            button5.config(state=NORMAL)
            button6.config(state=NORMAL)
        def change():
            b1.destroy()
            c1.delete(self.f1)
            scoreLabel.config(text="")
            c1.itemconfig(four,text="")
            c1.itemconfig(six,text="")
            tagp.config(text="Computer")
            tagp.place(x=680,y=450)
            tagc.config(text="Player")
            tagc.place(x=540,y=450)
            tag2.config(text="0",fg="#F97C07")
            tag3.config(text="0",fg="#0761F9")
            l1.config(text="Player")
            l2.config(text="Computer")
            l3.config(text=str1)
            l3.place(x=680,y=200)
            button1.place(x=400,y=200)
            button2.place(x=500,y=200)
            button3.place(x=400,y=250)
            button4.place(x=500,y=250)
            button5.place(x=400,y=300)
            button6.place(x=500,y=300)
            enable()
        def batting(p):
            self.p=p
            tag4.place(x=640,y=500)
            scoreLabel.config(text="")
            self.t = [1,2,3,4,5,6]
            self.computer = self.t[randint(0,5)]
            self.str=str(self.computer)
            c1.delete(self.f1)
            l3.config(text="The Computer chose:\n   "+str(self.str))
            if (self.p == self.computer):
                print("You are OUT!")
                self.w=self.w+1
                self.c=self.w
                self.counter1=0
                self.counter2=0
                if(self.w==3):
                    scoreLabel.config(text="ALL OUT!!!")
                    disable()
                    tag2.config(text=str(self.score))
                    tag3.config(text=str(self.w))
                    self.pscore=self.score
                    self.target=self.score
                    self.score=0
                    self.w=0
                    b1.place(x=550,y=600)
                else:
                    scoreLabel.config(text="You are OUT!!!")
                    tag2.config(text=str(self.score))
                    tag3.config(text=str(self.w))
            else:
                if(self.p==4):
                    self.fr+=1
                    c1.itemconfig(four,text="FOUR!!!")
                elif(self.p==6):
                    self.si+=1
                    c1.itemconfig(six,text="SIX!!!")
                self.score=self.score+self.p
                self.counter1=self.counter2=self.score
                if(self.counter1>=50):
                    self.hc+=1
                if(self.counter2>=100):
                    self.cen+=1
                tag2.config(text=str(self.score))
                tag3.config(text=str(self.w))
                print("Your score is",self.score)

        def bowling(p):
            self.p=p
            tag4.place(x=640,y=500)
            wicketLabel.config(text="")
            self.t = [1,2,3,4,5,6]
            self.computer = self.t[randint(0,5)]
            self.str=str(self.computer)
            c1.delete(self.f1)
            l3.config(text="The Computer chose:\n   "+str(self.str))
            if (self.p == self.computer):
                print("You got a WICKET")
                self.w=self.w+1
                if(self.w==3):
                    if(self.score<self.target):
                        disable()
                        tag3.config(text=str(self.w))
                        wicketLabel.config(text="ALL OUT!!!")
                        self.worl="WIN"
                        database(self.pname,self.worl,self.pscore,self.fr,self.si,self.hc,self.c)
                        win.place(x=550,y=100)
                        lostby=self.target-self.score
                        scoreLabel.config(text="Computer Lost By: \n"+str(lostby)+" Runs.")
                        back.place(x=580,y=600)
                else:
                    wicketLabel.config(text="You got a WICKET!!!")
                    tag2.config(text=str(self.score))
                    tag3.config(text=str(self.w))
            else:
                self.score=self.score+self.computer
                if(self.score>self.target):
                    disable()
                    scoreLabel.config(text="Computer Wins!!!")
                    self.worl="LOST"
                    database(self.pn,self.worl,str(self.pscore),str(self.fr),str(self.si),str(self.hc),str(self.c))
                    lose.place(x=550,y=100)
                    back.place(x=580,y=600)
                else:
                    if(self.computer==4):
                        c1.itemconfig(four,text="FOUR!!!")
                    elif(self.computer==6):
                        c1.itemconfig(six,text="SIX!!!")
                    tag2.config(text=str(self.score))
                    tag3.config(text=str(self.w))
                    print("Your score is",self.score)
        
        button1 = Button(c1,width =5,relief=RAISED,text="1",bd=1,command=Run1,
                         highlightthickness=0,highlightcolor="#FB028D",activebackground="white",
                         activeforeground="#F22C2C",cursor="hand2", fg="black", bg="white",font=("Helvetica", 16, 'bold'))
        button1.place(x=700,y=200)
        button2 = Button(c1,width =5,relief=RAISED,text="2",bd=1,command=Run2,
                         highlightthickness=0,highlightcolor="#FB028D",activebackground="white",
                         activeforeground="#F22C2C",cursor="hand2", fg="black", bg="white",font=("Helvetica", 16, 'bold'))
        button2.place(x=800,y=200)
        button3 = Button(c1,width =5,relief=RAISED,text="3",bd=1,command=Run3,
                         highlightthickness=0,highlightcolor="#FB028D",activebackground="white",
                         activeforeground="#F22C2C",cursor="hand2", fg="black", bg="white",font=("Helvetica", 16, 'bold'))
        button3.place(x=700,y=250)
        button4 = Button(c1,width =5,relief=RAISED,text="4",bd=1,command=Run4,
                         highlightthickness=0,highlightcolor="#FB028D",activebackground="white",
                         activeforeground="#F22C2C",cursor="hand2", fg="black", bg="white",font=("Helvetica", 16, 'bold'))
        button4.place(x=800,y=250)
        button5 = Button(c1,width =5,relief=RAISED,text="5",bd=1,command=Run5,
                         highlightthickness=0,highlightcolor="#FB028D",activebackground="white",
                         activeforeground="#F22C2C",cursor="hand2", fg="black", bg="white",font=("Helvetica", 16, 'bold'))
        button5.place(x=700,y=300)
        button6 = Button(c1,width =5,relief=RAISED,text="6",bd=1,command=Run6,
                         highlightthickness=0,highlightcolor="#FB028D",activebackground="white",
                         activeforeground="#F22C2C",cursor="hand2", fg="black", bg="white",font=("Helvetica", 16, 'bold'))
        button6.place(x=800,y=300)
        b1=Button(c1,width =15,relief=RAISED,text="Start Bowling",bd=1,command=change,
                         highlightthickness=0,highlightcolor="#FB028D",activebackground="white",
                         activeforeground="#F22C2C",cursor="hand2", fg="black", bg="white",font=("Helvetica", 16, 'bold'))
        back=Button(c1,width =10,relief=RAISED,text="Back",bd=1,command=Back,
                         highlightthickness=0,highlightcolor="#FB028D",activebackground="white",
                         activeforeground="#F22C2C",cursor="hand2", fg="black", bg="white",font=("Helvetica", 16, 'bold'))
    


        

        

        
