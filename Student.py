##Student User GUI
from tkinter import ttk
from tkinter import messagebox as tm
import views
import tkinter as tk
import ast
from PIL import ImageTk
class Student(tk.Frame):
    def __init__(self,master,data):
        tk.Frame.__init__(self, master)
        self.master = master
        self.flag=[True,False,False]
        self.k=0
        self.data=data
        self.data["details"]=ast.literal_eval(self.data["details"])
        # Configuring
        #tk.attributes("-fullscreen",True)
        self.master.geometry("{0}x{1}+0+0".format(self.master.winfo_screenwidth()-10, self.master.winfo_screenheight()-10))
        self.master.title("Attendance Management System")
        #self.master.configure(background = "red")

        # Creating Frame
        self.frame = tk.Frame(self.master)

        # Label
        #ttk.Label(self.frame, text = "Hello User!").pack()

        # Creating page layout
        #navbar : 
        style = ttk.Style()
        #style.configure("BW.TLabel", foreground="white", background="black")
        style.configure("B.TButton",foreground="black", bg="black",activebackground="grey", font=("Times New Roman",20,"bold"))
        self.toolbar=tk.Frame(self.master, bg = "black")
        logo=tk.Button(self.toolbar,bg='#000000',fg='#ffffff',activebackground="black",activeforeground="white",relief='flat',text='Attendance\nManager',command=self.welcome, font=("Times New Roman",16,"bold"))
        logo.pack(side="top",padx=30,pady=30)
        b1=tk.Button(self.toolbar,bg='#000000',fg='#ffffff',activebackground="black",activeforeground="white",relief='flat',text='Attendance Record',command=self.attendance_record, font=("Times New Roman",16,"bold"))
        b1.pack(side="top",padx=30,pady=30)
        b2=tk.Button(self.toolbar,bg='#000000',fg='#ffffff',activebackground="black",activeforeground="white",relief='flat',text='Student : \n {}'.format(self.data["details"]["name"]),command=self.profile, font=("Times New Roman",16,"bold"))
        b2.pack(side="top",padx=30,pady=30)
        
        b3=tk.Button(self.toolbar,bg='#000000',fg='#ffffff',activebackground="black",activeforeground="white",
                        relief='flat', text='Logout', command=self._logout_btn_clicked, font=("Times New Roman",16,"bold"))
        b3.pack(side="top",padx=30,pady=30)
        self.toolbar.pack(side="left",fill="y")
        self.welcome()
        self.frame.pack()

    def _logout_btn_clicked(self, ):    
        """ Logs out the user """
        self.destroy_page()
        import MainPage
        MainPage.MainPage(self.master).login_page(1)

    def destroy_page(self):
        """ Destory the page """
        #self.navbar.destroy()
        self.frame.destroy()
        self.toolbar.destroy()


    def welcome(self):
        if self.k>0:
            self.destroy_frame()
        style=ttk.Style()
        style.configure("X.TLabel",foreground="red")
        self.welcome_frame=tk.Frame(self.frame)
        ttk.Label(self.welcome_frame,text="Welcome , {}".format(self.data["details"]["name"].capitalize()),font=("Times New Roman",40,"bold")).grid(row=0,column=0,padx=40,pady=60)
        self.welcome_frame.pack()
        self.flag[0]=True
        self.k=self.k+1
        pass
    
    def attendance_record(self):
        self.destroy_frame()
        self.arf=tk.Frame(self.frame)
        subject_allocated=views.fetch_subjects(self.data["class"])
        #attendance=views.fetch_attendance(self.data["u_id"],self.data["class"])
        #print(attendance)
        ttk.Label(self.arf,text="Attendance Record",font=("Times New Roman",30,"bold")).pack()
        self.inside_frame=tk.Frame(self.arf)
        ttk.Label(self.inside_frame,text="Subject",font=("Times New Roman",20,"bold")).grid(row=1,column=1,padx=50,pady=20,sticky="w")
        ttk.Label(self.inside_frame,text="Professor",font=("Times New Roman",20,"bold")).grid(row=1,column=2,padx=50,pady=20,sticky="w")
        ttk.Label(self.inside_frame,text="% Attendance",font=("Times New Roman",20,"bold")).grid(row=1,column=3,padx=50,pady=20,sticky="w")
        #print(subject_allocated)
        z=2
        for x in subject_allocated.values():
            for i in range(len(x["role"])):
                ttk.Label(self.inside_frame,text=x["role"][i],font=("Times New Roman",15)).grid(row=z,column=1,padx=50,pady=20,sticky="w")
                z=z+1
        z=2
        for x in subject_allocated.values():
            name=views.fetch_tname(x["t_id"])
            for i in range(len(x["role"])):
                ttk.Label(self.inside_frame,text=name.capitalize(),font=("Times New Roman",15)).grid(row=z,column=2,padx=50,pady=20,sticky="w")
                z=z+1

        style=ttk.Style()
        style.theme_use(themename="clam")
        style.configure("G.Horizontal.TProgressbar",foreground="green",background="green")
        style.configure("D.Horizontal.TProgressbar",foreground="yellow",background="yellow")
        style.configure("CD.Horizontal.TProgressbar",foreground="red",background="red")
        z=2
        cp=list()
        for x in subject_allocated.values():
            for i in range(len(x["role"])):   
                a=views.calc_attendance(x["role"][i],x["subject_allotment_id"],self.data["class"],self.data["u_id"])
                if a<=50:
                    ttk.Progressbar(self.inside_frame,value=a,style="CD.Horizontal.TProgressbar").grid(row=z,column=4,padx=0,pady=20)
                elif a>50 and a<75:
                    ttk.Progressbar(self.inside_frame,value=a,style="D.Horizontal.TProgressbar").grid(row=z,column=4,padx=0,pady=20)
                else:
                    ttk.Progressbar(self.inside_frame,value=a,style="G.Horizontal.TProgressbar").grid(row=z,column=4,padx=0,pady=20)
                ttk.Label(self.inside_frame,text="{:.2f}".format(a)).grid(row=z,column=3,pady=20)
                z=z+1
                cp.append(a)
        ttk.Label(self.inside_frame,text="Cumilative\nAttendance : ",font=("Times New Roman",15,"bold")).grid(row=z+1,column=2,pady=20)
        ttk.Label(self.inside_frame,text="{:.2f}".format(sum(cp)/len(cp)),font=("Times New Roman",15,"bold")).grid(row=z+1,column=3,pady=20)
        self.inside_frame.pack(anchor="w",padx="0",pady=50)

        self.arf.pack()
        self.flag[1]=True

    def profile(self):
        self.destroy_frame()
        self.profile_frame=tk.Frame(self.frame)
        ttk.Label(self.profile_frame,text="Profile Page",font=("Times New Roman",30,"bold")).grid(row=0,columnspan=2)
        self.inside_frame=tk.Frame(self.profile_frame)
        #self.profile_photo_frame=tk.Frame(self.profile_frame)
        
        #ttk.Label(self.profile_photo_frame,text="Profile Photo",font=("Times New Roman",15,"bold")).grid(row=0,column=0,padx=30,pady=40)
        #self.img = tk.PhotoImage(file = ('C:\\xampp\\htdocs\\user_profile.png'))
        #self.inside_frame.tk.call("wm", "iconphoto", self.inside_frame._w, self.img)

        style=ttk.Style()
        style.theme_use(themename="clam")
        #style.configure("X.TLabel",foreground="black",font=("Times New Roman",15,"Bold"))
        ttk.Label(self.inside_frame,text="Unique Id : ",font=("Times New Roman",15,"bold")).grid(row=1,column=1,padx=20,pady=30)
        ttk.Label(self.inside_frame,text=self.data["u_id"],font=("Times New Roman",15,"bold")).grid(row=1,column=2,padx=20,pady=30)
        ttk.Label(self.inside_frame,text="Name : ",font=("Times New Roman",15,"bold")).grid(row=2,column=1,padx=20,pady=30)
        ttk.Label(self.inside_frame,text=self.data["details"]["name"],font=("Times New Roman",15,"bold")).grid(row=2,column=2,padx=20,pady=30)
        ttk.Label(self.inside_frame,text="Roll No : ",font=("Times New Roman",15,"bold")).grid(row=3,column=1,padx=20,pady=30)
        ttk.Label(self.inside_frame,text=self.data["details"]["roll_no"],font=("Times New Roman",15,"bold")).grid(row=3,column=2,padx=20,pady=30)
        ttk.Label(self.inside_frame,text="Class : ",font=("Times New Roman",15,"bold")).grid(row=4,column=1,padx=20,pady=30)
        ttk.Label(self.inside_frame,text=self.data["class"],font=("Times New Roman",15,"bold")).grid(row=4,column=2,padx=20,pady=30)
        ttk.Label(self.inside_frame,text="Department : ",font=("Times New Roman",15,"bold")).grid(row=5,column=1,padx=20,pady=30)
        ttk.Label(self.inside_frame,text=views.dept_id[int(self.data["details"]["dept_id"])],font=("Times New Roman",15,"bold")).grid(row=5,column=2,padx=20,pady=30)
        ttk.Label(self.inside_frame,text="Gender : ",font=("Times New Roman",15,"bold")).grid(row=6,column=1,padx=20,pady=30)
        ttk.Label(self.inside_frame,text=self.data["details"]["gender"],font=("Times New Roman",15,"bold")).grid(row=6,column=2,padx=20,pady=30)       
        ttk.Label(self.inside_frame,text="Email Id : ",font=("Times New Roman",15,"bold")).grid(row=7,column=1,padx=20,pady=30)
        ttk.Label(self.inside_frame,text=self.data["email_id"],font=("Times New Roman",15,"bold")).grid(row=7,column=2,padx=20,pady=30)
        ttk.Label(self.inside_frame,text="Password : ",font=("Times New Roman",15,"bold")).grid(row=8,column=1,padx=20,pady=30)
        ttk.Label(self.inside_frame,text=self.data["password"],font=("Times New Roman",15,"bold")).grid(row=8,column=2,padx=20,pady=30)
        
        
        #profile=ImageTk.PhotoImage(file="user_profile.png")
        #tk.Label(self.profile_photo_frame,image=profile).grid(row=0,pady=30)
        
        #self.profile_photo_frame.grid(row=1,column=0,sticky="w")
        self.inside_frame.grid(row=1,column=1,sticky="e")
        self.profile_frame.pack()
        self.flag[2]=True

    def destroy_frame(self):
        if self.flag[0]:
            self.welcome_frame.destroy()
            self.flag[0]=False
        elif self.flag[1]:
            self.arf.destroy()
            self.flag[1]=False
        elif self.flag[2]:
            self.profile_frame.destroy()
            self.flag[2]=False
        #print(self.flag)
        pass
"""
master=tk.Tk()
Student(master,"test")
master.mainloop()
"""
