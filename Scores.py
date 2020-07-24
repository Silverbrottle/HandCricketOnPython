from tkinter import *
import mysql.connector
class scores:
    def __init__(self,root3):
        self.root3 = root3
        self.pname=StringVar()
        self.i=0
        self.x=[]
        w=1280
        h=720
        ws = self.root3.winfo_screenwidth()
        hs = self.root3.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.root3.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.root3.config(bg='#1ACDF3')
        self.root3.title("Scores")
        self.str1=StringVar()
        c1=Canvas(self.root3,height=720,width=1280,bg="#DCFBD3")
        c1.pack()
        self.nf=Label(self.root3,text="Record not Present in the Database\nCheck Playername again!",font=("Comic Sans MS", 16, 'bold'),bg="#DCFBD3",fg="red")
        self.lp1=Label(self.root3,text="-",font=("Comic Sans MS", 16),bg="#DCFBD3",fg="black")
        self.lp2=Label(self.root3,text="-",font=("Comic Sans MS", 16),bg="#DCFBD3",fg="black")
        self.lp3=Label(self.root3,text="-",font=("Comic Sans MS", 16),bg="#DCFBD3",fg="black")
        self.lp4=Label(self.root3,text="-",font=("Comic Sans MS", 16),bg="#DCFBD3",fg="black")
        self.lp5=Label(self.root3,text="-",font=("Comic Sans MS", 16),bg="#DCFBD3",fg="black")
        self.lp6=Label(self.root3,text="-",font=("Comic Sans MS", 16),bg="#DCFBD3",fg="black")
        self.lp7=Label(self.root3,text="-",font=("Comic Sans MS", 16),bg="#DCFBD3",fg="black")
        self.lp8=Label(self.root3,text="-",font=("Comic Sans MS", 16),bg="#DCFBD3",fg="black")
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="ayush777",
            database="handcricket"
        )
        self.mycursor = self.mydb.cursor()
        def change():
            l1=Label(self.root3,text="No. in Database",font=("Comic Sans MS", 16, 'bold'),bg="#DCFBD3",fg="black")
            l1.place(x=50,y=200)
            l2=Label(self.root3,text="Player",font=("Comic Sans MS", 16, 'bold'),bg="#DCFBD3",fg="black")
            l2.place(x=50,y=250)
            l3=Label(self.root3,text="Result",font=("Comic Sans MS", 16, 'bold'),bg="#DCFBD3",fg="black")
            l3.place(x=50,y=300)
            l4=Label(self.root3,text="Runs",font=("Comic Sans MS", 16, 'bold'),bg="#DCFBD3",fg="black")
            l4.place(x=50,y=350)
            l5=Label(self.root3,text="Fours",font=("Comic Sans MS", 16, 'bold'),bg="#DCFBD3",fg="black")
            l5.place(x=50,y=400)
            l6=Label(self.root3,text="Sixes",font=("Comic Sans MS", 16, 'bold'),bg="#DCFBD3",fg="black")
            l6.place(x=50,y=450)
            l7=Label(self.root3,text="Half Century",font=("Comic Sans MS", 16, 'bold'),bg="#DCFBD3",fg="black")
            l7.place(x=50,y=500)
            l8=Label(self.root3,text="Century",font=("Comic Sans MS", 16, 'bold'),bg="#DCFBD3",fg="black")
            l8.place(x=50,y=550)
            self.lp1.config(text="-")
            self.lp2.config(text="-")
            self.lp3.config(text="-")
            self.lp4.config(text="-")
            self.lp5.config(text="-")
            self.lp6.config(text="-")
            self.lp7.config(text="-")
            self.lp8.config(text="-")
        def enter():
            self.pname=self.nam.get()
            self.mycursor.execute("SELECT * FROM scores where playername=%s",(self.pname,))
            self.myresult = self.mycursor.fetchall()
            self.x=self.myresult
            if(len(self.myresult)==0):     
                self.nf.place(x=100,y=150)
            else:
                change()
                self.nf.config(text="")
                print(self.x)
                self.lp1.config(text=self.x[0][0])
                self.lp1.place(x=300,y=200)
                self.lp2.config(text=self.x[0][1])
                self.lp2.place(x=300,y=250)
                self.lp3.config(text=self.x[0][2])
                self.lp3.place(x=300,y=300)
                self.lp4.config(text=self.x[0][3])
                self.lp4.place(x=300,y=350)
                self.lp5.config(text=self.x[0][4])
                self.lp5.place(x=300,y=400)
                self.lp6.config(text=self.x[0][5])
                self.lp6.place(x=300,y=450)
                self.lp7.config(text=self.x[0][6])
                self.lp7.place(x=300,y=500)
                self.lp8.config(text=self.x[0][7])
                self.lp8.place(x=300,y=550)
                
                '''n=[0,1,2,3,4,5,6,7]
                for j in n:
                    print(self.x[0][j])
                    lp=Label(self.root3,text=str(self.x[0][j]),font=("Comic Sans MS", 16),bg="white",fg="black")
                    lp.place(x=300,y=200+self.i)
                    self.i+=50
                lp=Label(self.root3,text=str(self.x[0][7]),font=("Comic Sans MS", 16),bg="white",fg="black")
                lp.place(x=300,y=200+self.i)
                self.i=0'''
        
        search=Label(c1,text="Search Record:",font=("Comic Sans MS", 20, 'bold'),bg="#DCFBD3",fg="black")
        search.place(x=10,y=10)
        le=Label(c1,text="Enter Playername:",font=("Comic Sans MS", 16, 'bold'),bg="#DCFBD3",fg="black")
        le.place(x=10,y=60)
        self.nam=Entry(c1,bg="white",textvariable=self.pname,fg="black",font=("Comic Sans MS", 16),width=15)
        self.nam.place(x=210,y=60)
        enterb= Button(c1,width =5,relief=RAISED,text="Enter",bd=1,command=enter)
        enterb.config(highlightthickness=0,highlightcolor="#FB028D",activebackground="white",
                       activeforeground="#F22C2C",cursor="hand2", fg="white", bg="#F22C2C",font=("Helvetica", 16, 'bold'))
        enterb.place(x=60, y=100)  
            
        def Back():
            self.root3.destroy()
        button1 = Button(self.root3,width =10,relief=RAISED,text="Back",bd=1,command=Back)
        button1.config(highlightthickness=0,highlightcolor="#FB028D",activebackground="white",activeforeground="#F22C2C",cursor="hand2", fg="white", bg="#F22C2C",font=("Helvetica", 16, 'bold'))
        button1.place(x=600, y=660)

class database:
    def __init__(self,pn,res,runs,f,s,hc,c):
        self.pn=pn
        self.res=res
        self.runs=runs
        self.f=f
        self.s=s
        self.hc=hc
        self.c=c
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="ayush777",
            database="handcricket"
        )
        self.mycursor = self.mydb.cursor()

        self.sql = "INSERT INTO scores (playername,result,runs,fours,sixes,halfcentury,century) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        self.val = (self.pn,self.res,self.runs,self.f,self.s,self.hc,self.c)
        self.mycursor.execute(self.sql,self.val)

        self.mydb.commit()

        print(self.mycursor.rowcount, "record")
'''j=70
        i=70
        for p in range(0,7):
            c1.create_line(j,0,j,680,fill="#F97C07")
            j+=170
        for p in range(0,20):
            c1.create_line(0,i,1280,i,fill="#F97C07")
            i+=50
        
        self.mycursor.execute("SELECT * FROM scores")
        self.myresult = self.mycursor.fetchall()
        l=["playername","result","runs","fours","sixes","halfcentury","century"]
        i=0
        j=0'''
