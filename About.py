from tkinter import *
class about:
    def __init__(self,root4):
        self.root4 = root4
        w=1280
        h=720
        ws = self.root4.winfo_screenwidth()
        hs = self.root4.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.root4.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.root4.config(bg='#DCFBD3')
        self.root4.title("About")
        self.root4.resizable(0,0)
        def Back():
            self.root4.destroy()
        c=Canvas(self.root4,height=700,width=1200,bg="#DCFBD3",bd=0,highlightcolor="#DCFBD3",relief=RIDGE,cursor="ibeam")
        ab="Abhinav Pisharody\t\t21"
        al="Alisto Pinto\t\t17"
        ay="Ayush Navgiri\t\t07"
        hc="Hand Cricket"
        co="Open Source Technology(OST)"
        c.create_text(45,20,text="About:",font=("Comic Sans MS", 24, 'bold'),anchor=NW,fill="#350A08")
        c.create_text(45,100,text="Project:",font=("Comic Sans MS", 24, 'bold'),anchor=NW,fill="#350A08")
        c.create_text(45,150,text="Course:",font=("Comic Sans MS", 24, 'bold'),anchor=NW,fill="#350A08")
        c.create_text(45,200,text="Credits:\n    Name\t\t\tRoll No.",font=("Comic Sans MS", 24, 'bold'),anchor=NW,fill="#350A08")
        c.create_text(180,100,text=hc,font=("Comic Sans MS", 24),anchor=NW,fill="#350A08")
        c.create_text(180,150,text=co,font=("Comic Sans MS", 24),anchor=NW,fill="#350A08")
        c.create_text(100,300,text=ab,font=("Comic Sans MS", 22),anchor=NW,fill="#350A08")
        c.create_text(100,350,text=al,font=("Comic Sans MS", 22),anchor=NW,fill="#350A08")
        c.create_text(100,400,text=ay,font=("Comic Sans MS", 22),anchor=NW,fill="#350A08")
        c.create_text(45,450,text="Reference:",font=("Comic Sans MS", 22,'bold'),anchor=NW,fill="#350A08")
        c.create_text(200,450,text=" Made in Python.\n Tkinter used for GUI.",font=("Comic Sans MS", 22),anchor=NW,fill="#350A08")
        c.create_text(45,575,text="cc All Rights Reserved",font=("Comic Sans MS", 12),anchor=NW,fill="black")
        c.place(x=40,y=10)
        button1 = Button(self.root4,width =10,highlightthickness=1,highlightcolor="black",relief=RAISED,text="Back",bd=1,command=Back)
        button1.config(activebackground="gray",activeforeground="white",cursor="hand2", fg="black", bg="white",font=("Comic Sans MS", 16, 'bold'))
        button1.place(x=100, y=630)
