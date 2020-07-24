from tkinter import *
from Play import play
class name:
    def __init__(self,rootp):
        self.rootp = rootp
        w=1280
        h=720
        ws = self.rootp.winfo_screenwidth()
        hs = self.rootp.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.rootp.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.rootp.config(bg='#DCFBD3')
        self.rootp.title("Start")
        self.rootp.resizable(0,0)
        self.name=StringVar()
            

        def enter():
            na(n)
            self.rootp.destroy()
            
        c=Canvas(self.rootp,height=700,width=1200,bg="#DCFBD3",bd=0,highlightcolor="#DCFBD3",relief=RIDGE,cursor="ibeam")
        c.pack()
        l1=Label(self.rootp,text="Enter Playername:",font=("Comic Sans MS", 20, 'bold'),bg="white",fg="black")
        l1.place(x=10,y=100)
        nam=Entry(self.rootp,bg="white",fg="black",textvariable=self.name,font=("Comic Sans MS", 20, 'bold'))
        nam.place(x=450,y=100)
        n=nam.get()
        
        '''button1 = Button(self.rootp,width =10,relief=RAISED,text="Enter",bd=1,command=Back)
        button1.config(highlightthickness=0,highlightcolor="#FB028D",activebackground="white",
                       activeforeground="#F22C2C",cursor="hand2", fg="white", bg="#F22C2C",font=("Helvetica", 16, 'bold'))
        button1.place(x=600, y=600)'''
        button2 = Button(self.rootp,width =10,relief=RAISED,text="Enter",bd=1,command=enter)
        button2.config(highlightthickness=0,highlightcolor="#FB028D",activebackground="white",
                       activeforeground="#F22C2C",cursor="hand2", fg="white", bg="#F22C2C",font=("Helvetica", 16, 'bold'))
        button2.place(x=600, y=680)
