from tkinter import *
from PIL import ImageTk,Image
from Instructions import instructions
from Play import play
from Scores import scores
from About import about
class FrontPage:
    def __init__(self,root):
        self.root = root
        w=1280
        h=720
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.root.title("Introduction")
        self.root.resizable(0,0)
        my_frame = Frame(self.root, bd = 20)
        my_frame.pack()
        
        filename = ImageTk.PhotoImage(Image.open("cric-gg.jpg"))
        background_label = Label(self.root, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        def Ins():
            root1=Tk()
            frame1 = instructions(root1)
            root1.mainloop()
        def Play():
            top=Toplevel()
            frame2=play(top)
            top.mainloop()
        def Scores():
            root3=Tk()
            frame3=scores(root3)
            root3.mainloop()
        def About():
            root4=Tk()
            frame4=about(root4)
            root4.mainloop()
        def Exit():
            print("Thanks for playing Hand Cricket PC Edition!\nVisit us again")
            self.root.destroy()
            
        button1 = Button(self.root,width =15,relief=RAISED,text="Play !",bd=1,highlightthickness=0,highlightcolor="#FB028D",command=Play)
        button1.config(activebackground="white",activeforeground="#F22C2C",cursor="hand2", fg="white", bg="#F22C2C",font=("Helvetica", 16, 'bold'))
        button1.place(x=960, y=360)
        
        button2 = Button(self.root,width =15,relief=RAISED,text="Instructions",bd=1,highlightthickness=0, command=Ins)
        button2.config(activebackground="white",activeforeground="#F22C2C",cursor="hand2", fg="white", bg="#F22C2C",font=("Helvetica", 16, 'bold'))
        button2.place(x=960, y=400)
        
        button3 = Button(self.root,width =15,relief=RAISED,text="Scores",bd=1,highlightthickness=0,command=Scores)
        button3.config(activebackground="white",activeforeground="#F22C2C",cursor="hand2", fg="white", bg="#F22C2C",font=("Helvetica", 16, 'bold'))
        button3.place(x=960, y=440)
        
        button4 = Button(self.root,width =15,relief=RAISED,text="About",bd=1,highlightthickness=0,command=About)
        button4.config(activebackground="white",activeforeground="#F22C2C",cursor="hand2", fg="white", bg="#F22C2C",font=("Helvetica", 16, 'bold'))
        button4.place(x=960, y=480)
        
        button5 = Button(self.root,width =15,relief=RAISED,text="Exit",bd=1,highlightthickness=0,command=Exit)
        button5.config(activebackground="white",activeforeground="#F22C2C",cursor="hand2", fg="white", bg="#F22C2C",font=("Helvetica", 16, 'bold'))
        button5.place(x=960, y=520)

        self.root.mainloop()
        
        
        
if __name__=="__main__":
    root = Tk()
    frame = FrontPage(root)
    

