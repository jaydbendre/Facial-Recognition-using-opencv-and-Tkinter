import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import views
from tkinter import messagebox as tm

class MainPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master

        # Configuring
        self.master.geometry("{0}x{1}+0+0".format(self.master.winfo_screenwidth()-10, self.master.winfo_screenheight()-10))
        self.master.title("Attendance System")
        #self.master.configure(background = "red")
        
        #self.img = tk.PhotoImage(file = ('C:\\xampp\\htdocs\\asset-tracker-PythonProject\\asset.png'))
        #self.master.tk.call("wm", "iconphoto", self.master._w, self.img)

        # Creating Frame
        self.frame = tk.Frame(self.master)

        # ****** Navbar ******
        self.navbar = tk.Frame(self.master, background = "black")

        self.navbar_ui()
        
        self.navbar.pack(side="left",fill = "y")

        #self.frameB = ttk.Frame(self.master)
        
        ttk.Label(self.frame, text = "").pack()
        self._asset_tracker_btn_clicked_()
        
        self.frame.pack()

    def navbar_ui(self):
        """ NavBar UI """
        children = list(self.navbar.children.values())
        for child in children:
            child.destroy()
         
        # Declaring the elements
        #self.logo = tk.Button(self.navbar, text = "Logo", bg = "black", fg = "white", 
        #            relief = "flat", font = ("Georgia", "12", "bold"), command = self._asset_tracker_btn_clicked_)
        """self.logo = tk.Button(self.navbar, image = img, bg = "black", fg = "white", 
                    relief = "flat", font = ("Georgia", "12", "bold"), command = self._asset_tracker_btn_clicked_)"""
        self.name = tk.Button(self.navbar, text = "Attendance System", bg = "black", fg = "white", 
                    relief = "flat", font = ("Georgia", "12", "bold"), command = self._asset_tracker_btn_clicked_)
        self.sign_up = tk.Button(self.navbar, text = "Sign Up", bg = "black", fg = "white", 
                        relief = "flat", font = ("Georgia", "12", "bold"), command = self._signup_btn_clicked_)
        self.login = tk.Button(self.navbar, text = "Login", bg = "black", fg = "white", 
                        relief = "flat", font = ("Georgia", "12", "bold"), command = self._login_btn_clicked_)
        self.problem = tk.Button(self.navbar, text = "Problem Statement", bg = "black", fg = "white", 
                        relief = "flat", font = ("Georgia", "12", "bold"), command = self._problem_btn_clicked_)
        self.soln = tk.Button(self.navbar, text = "Solution", bg = "black", fg = "white", 
                        relief = "flat", font = ("Georgia", "12", "bold"), command = self._soln_btn_clicked_)
        # Placing them
        #self.logo.grid(row = 0,column = 0,sticky = "w", padx = 3)
        self.name.pack(anchor="center",pady=30)
        self.problem.pack(anchor="center",pady=30)
        self.soln.pack(anchor="center",pady=30)
        self.sign_up.pack(anchor="s",pady=30)
        self.login.pack(anchor="s",pady=30)        

    def _asset_tracker_btn_clicked_(self):
        """ Main Page """
        children = list(self.frame.children.values())
        for child in children:
            child.destroy()
        
        # Style
        style = ttk.Style()
        style.configure('btn.TButton', font = ('Trebuchet MS', 12), foreground = "black", background = "black")
        style.configure('heading.TLabel', font = ('Georgia', 32, 'bold'), foreground = "Red")

        #logo = tk.PhotoImage(file = ('C:\\xampp\\htdocs\\asset-tracker-PythonProject\\logo.png'))

        # ****** Heading ******
        ttk.Label(self.frame).pack()
        ttk.Label(self.frame, text = "Welcome to", style = "heading.TLabel").pack(anchor = "center",pady=20)
        #ttk.Label(self.frame, image = self.img, style = 'heading.TLabel').pack(anchor = "c")
        ttk.Label(self.frame, text = "Attendance", style = "heading.TLabel").pack(anchor = "center",pady=20)
        ttk.Label(self.frame, text = "System!", style = "heading.TLabel").pack(anchor = "center",pady=20)

        # ****** Main Page ******
        """self.signup = ttk.Button(self.frame, text = "Sign Up", style = 'btn.TButton',command = self._signup_btn_clicked_)
        self.login = ttk.Button(self.frame, text = "Login", style = 'btn.TButton', command = self._login_btn_clicked_)
        self.close = ttk.Button(self.frame, text = "Exit", style = 'btn.TButton', command = self.master.quit)

        self.heading.pack(fill = "x")
        tk.Label(self.frame, text = "").pack()
        self.signup.pack(fill = "x")
        tk.Label(self.frame, text = "").pack()
        self.login.pack(fill = "x")
        tk.Label(self.frame, text = "").pack()
        self.close.pack(fill = "x")"""

    def _signup_btn_clicked_(self):
        """ Navigating to the sign up page """
        children = list(self.frame.children.values())
        for child in children:
            child.destroy()
        self.signup_page()
        
    def _problem_btn_clicked_(self):
        """" Navigating to problem statement """
        children = list(self.frame.children.values())
        for child in children:
            child.destroy()
        self.problem_page()
        
    def _login_btn_clicked_(self):
        """ Navigating to login page """
        children = list(self.frame.children.values())
        for child in children:
            child.destroy()
        self.login_page(1)

    def signup_page(self):
        """ The signup page """
        # Label
        self.heading = ttk.Label(self.frame, text = "Attendance System", font = ('Georgia', 32, 'bold'), foreground = "Red")

        # Style
        style = ttk.Style()
        style.configure('btn.TButton', font = ('Trebuchet MS', 12), foreground = "#ffffff", background = "#0fd2ee")
        style.configure('label.TLabel', font = ('Trebuchet MS', 14), foreground = "Black", padding = 2, relief = "flat")

        # Widgets
        self.sign_up_frame = tk.LabelFrame(self.frame, text = "", padx = 50, pady = 40, borderwidth = 10,
                                highlightthickness = 5, highlightbackground = "white")

        self.name_label = ttk.Label(self.sign_up_frame, text = "Enter name : ", style = "label.TLabel")
        self.name = ttk.Entry(self.sign_up_frame)
        
        self.email_id_label = ttk.Label(self.sign_up_frame, text = "Enter email-id : ", style = "label.TLabel")
        self.email_id = ttk.Entry(self.sign_up_frame)

        #self.username_label = ttk.Label(self.frame, text = "Enter username : ", style = "label.TLabel")
        #self.username = ttk.Entry(self.frame)
        
        self.password_label = ttk.Label(self.sign_up_frame, text = "Enter password : ", style = "label.TLabel")
        self.password = ttk.Entry(self.sign_up_frame, show = "*")
        
        self.dept_name_label = ttk.Label(self.sign_up_frame, text = "Select department : ", style = "label.TLabel")
        self.dept_name = ttk.Combobox(self.sign_up_frame, values = ["dept1",'dept2', 'dept3', 'dept4'])
        self.dept_name.current(0)

        self.room_label = ttk.Label(self.sign_up_frame, text = "Enter class : ", style = "label.TLabel")
        self.room = ttk.Entry(self.sign_up_frame)

        self.gender = tk.IntVar()
        self.gender_label = ttk.Label(self.sign_up_frame, text = "Gender : ", style = "label.TLabel")
        self.male = ttk.Radiobutton(self.sign_up_frame, text = "Male", value = 0, variable = self.gender)
        self.female = ttk.Radiobutton(self.sign_up_frame, text = "Female", value = 1, variable = self.gender)

        self.phone_no_label = ttk.Label(self.sign_up_frame, text = "Enter Roll number : ", style = "label.TLabel")
        self.phone_no = ttk.Entry(self.sign_up_frame)

        self.submitbtn = tk.Button(self.sign_up_frame, text = "SUBMIT", command = self._submit_btn_clicked,
                            font = ('Trebuchet MS', 12), foreground = "white", background = "#0861E5", padx = 50, pady = 0)
        self.resetbtn = tk.Button(self.sign_up_frame, text = "RESET", command = self._reset_btn_clicked,
                            font = ('Trebuchet MS', 12), foreground = "white", background = "red", padx = 50, pady = 0)
        #self.submitbtn = tk.Button(self.frame, text = "SUBMIT", background = "blue", foreground = "white", command = self._submit_btn_clicked)
        #self.resetbtn = tk.Button(self.frame, text = "RESET", background = "red", foreground = "white", command = self._reset_btn_clicked)
        #self.gobackbtn = ttk.Button(self.frame, text = "GO BACK", command = self._goback_btn_clicked)

        # Configuring Layout of the page
        self.heading.grid(columnspan = 2)
        self.sign_up_frame.grid(row = 1, columnspan = 2, pady = 10)
        #self.gobackbtn.grid(row = 1, sticky= "w")
        
        ttk.Label(self.sign_up_frame, text = "Student Registration", font = ("Georgia", 16, "bold"), foreground = "black").grid(row = 0, columnspan = 2, pady = 5)
        self.name_label.grid(row = 2, sticky = "e", pady = 20)
        self.name.grid(row = 2, column = 1, pady = 20)
        
        self.email_id_label.grid(row = 3, sticky = "e", pady = 20)
        self.email_id.grid(row = 3, column = 1, pady = 20)
        
        #self.username_label.grid(row = 4, sticky = "e")
        #self.username.grid(row = 4, column = 1)
        
        self.password_label.grid(row = 5, sticky = "e", pady = 20)
        self.password.grid(row = 5, column = 1, pady = 20)
        
        self.dept_name_label.grid(row = 6, sticky = "e", pady = 20)
        self.dept_name.grid(row = 6, column = 1, pady = 20)

        self.room_label.grid(row = 7, sticky = "e", pady = 20)
        self.room.grid(row = 7, column = 1, pady = 20)

        self.gender_label.grid(row = 8, sticky = "e", pady = 20)
        self.male.grid(row = 8, column = 1, sticky = "w", pady = 20)
        self.female.grid(row = 8, column = 1, sticky = "e", pady = 20)

        self.phone_no_label.grid(row = 9, sticky = "e", pady = 20)
        self.phone_no.grid(row = 9, column = 1, pady = 20)

        #ttk.Label(self.frame,text = "", style = "label.TLabel").grid(row = 10)
        self.submitbtn.grid(row = 11, column = 0, sticky = "w", pady = 20)
        self.resetbtn.grid(row = 11, column = 1, sticky = "e", pady = 20)

    def _submit_btn_clicked(self):
        """ Submits the form and sends data to the server/api """

        if self.name.get() == "" or self.password.get() == "" or self.email_id.get() == "" or self.dept_name.get() == "":
            tm.showerror('SignUp Error', "All Fields Required")
        else:
            dept_id = None
            if self.dept_name.get() == "dept1":
                dept_id = 1
            elif self.dept_name.get() == "dept2":
                dept_id = 2
            elif self.dept_name.get() == "dept3":
                dept_id = 3
            elif self.dept_name.get() == "dept4":
                dept_id = 4
            
            gender = None
            if self.gender.get() == 0:
                gender = "M"
            else : 
                gender = "F"
            data = {
                'details'   : 
                {
                'name'      : self.name.get(), 
                "gender"    : gender, 
                "dept_id"   : dept_id,
                "roll_no"   : self.phone_no.get()
                },
                'password'  : self.password.get(),
                'email_id'  : self.email_id.get(),
                "class"     : self.room.get(),
                "role_id"   : 0
                }
            
            #print(data)
    
            children = list(self.frame.children.values())

            views.store(data, self.master)
           
    def _reset_btn_clicked(self):
        """ Resets all the fields """
        self.name.delete(0, "end")
        self.email_id.delete(0, "end")
        self.password.delete(0, "end")
        self.gender.set(value = None)
        self.dept_name.current(0)
        self.phone_no.delete(0, "end")
        self.room.delete(0, "end")
        #self.username.delete(0, "end")
        return

    def login_page(self, c):
        """ The login page """
        if c == 1:
            # Destroying the frame
            children = list(self.frame.children.values())
            for child in children:
                child.destroy()

        self.heading = ttk.Label(self.frame, text = "Attendance System", font = ('Georgia', 32, 'bold'), foreground = "Red")
        
        self.login_frame = tk.LabelFrame(self.frame,text = "", borderwidth = 10, padx = 40, pady = 40,
                                        highlightthickness = 5, highlightbackground = "white")
        

        style = ttk.Style()
        style.configure('btn.TButton', font = ('Trebuchet MS', 12), foreground = "#ffffff", background = "#0fd2ee")
        style.configure('label.TLabel', font = ('Trebuchet MS', 14), foreground = "Black", padding = 2)

        self.ulabel = ttk.Label(self.login_frame, text = "Email Id : ", style = "label.TLabel")
        self.plabel = ttk.Label(self.login_frame, text = "Password : ", style = "label.TLabel")
        
        self.email_id = ttk.Entry(self.login_frame, width = 50)
        self.password = ttk.Entry(self.login_frame, show = "*", width = 50)
        
        self.loginbtn = tk.Button(self.login_frame, text = "LOGIN", command = self._login_btn_clicked, 
                            font = ('Trebuchet MS', 12), foreground = "white", background = "#0861E5", padx = 60, pady = 0,)

        # Adding the widgets
        self.heading.pack(anchor = "center", padx = 20, pady = 10)

        self.ulabel.pack(anchor = "center", padx = 20, pady = 10)
        self.email_id.pack(anchor = "center", padx = 20, pady = 10)

        self.plabel.pack(anchor = "center", padx = 20, pady = 10)
        self.password.pack(anchor = "center", padx = 20, pady = 10)

        self.loginbtn.pack(anchor = "center", padx = 20, pady = 20)
        self.login_frame.pack(padx = 30, pady = 30)

    def _login_btn_clicked(self):

        if self.email_id.get() == "" or self.password.get() == "":
            tm.showerror("Login Error", "Wrong username or password!")

        else:
            # Check if the person exists on the database
            # If yes, then continue!
            # If no, then redriect to the sign up page
            
            data = {
                'email_id' : self.email_id.get(),
                'password' : self.password.get(),
            } 
            views.login(data, self.master)
            self.destroyPage() 
    
    def problem_page(self):
        """ Problem Page """
        style = ttk.Style()
        #style.configure("TLabelframe.Label", font = ("Georgia", 32, "bold"), foreground = "red", padx = 50, pady = 100)
        style.configure("TLabelframe", bd = "red",)
        style.configure("s.TLabel", font = ('Georgia', 14, "bold")) 
        
        self.problem_page_frame = tk.Frame(self.frame, highlightbackground = "white", highlightthickness = 5, highlightcolor = "red")
        self.problem_page_frame.configure(bd = 0,)
        
        ttk.Label(self.problem_page_frame, text = "Problem Statement", style = "heading.TLabel").pack(anchor = "center", pady = 30)
        self.problem_page_frame.pack(anchor = "center", pady = 100)
        ttk.Label(self.problem_page_frame, text = "Attendance System", style = "s.TLabel").pack(anchor = "center", padx = 30 ,pady = 30)
        statement = "Taking attendance is a cumbersome and tiresome task.\nKeeping track of attendance and generating a report\nat end semester is difficult. In the orthodox method of\ntaking attendance, there are chances of proxy attendance.\nDevelop a facial identification and detection system to solve\nthe problem. The system should be should be easy to\nuse, robust and rapid."
        ttk.Label(self.problem_page_frame, text = statement, font = ("Georgia",14,"bold")).pack(anchor = "center", padx = 30, pady = 30)
    
    def soln_page(self):
        """ Solution Page """
        
        style = ttk.Style()
        style.configure("TLabelframe.Label", font = ("Georgia", 32, "bold"), foreground = "red", padx = 10, pady = 100)
        style.configure("TLabelframe", borderwidth = 12)
        style.configure("s.TLabel", font = ('Georgia', 32, "bold") , foreground = "red" ) 
        
        self.problem_page_frame = tk.LabelFrame(self.frame, highlightbackground = "white", highlightthickness = 5, highlightcolor = "red")
        self.problem_page_frame.configure(borderwidth = 10)
        
        self.problem_page_frame.pack(anchor = "center", pady = 100)
        ttk.Label(self.problem_page_frame, text = "Solution", style = "s.TLabel").pack(anchor = "center", padx = 30 ,pady = 30)
        statement = "Offered Solution provides a facial recognition system combining opencv AI with python.\nOpenCv is a neural network AI which is used to map your face data as a form of nodes in a trainer file \n The solution enables the students to view their attendance and enables the teachers to mark batch attendances by \nusing the camera of their device, thus saving time for marking attendances"
        ttk.Label(self.problem_page_frame, text = statement , font = ("Georgia",14,"bold")).pack(anchor = "center", padx = 30, pady = 30)
        img=tk.PhotoImage(file="download.png")
        l=tk.Label(self.problem_page_frame,image=img)
        l.image=img
        l.pack()
    def destroyPage(self):
        """ Destroys the whole page i.e. clears the window """
        self.frame.destroy()
        self.frame = None
        self.navbar.destroy()
    
    def _soln_btn_clicked_(self):
        """" Navigating to solution statement """
        children = list(self.frame.children.values())
        for child in children:
            child.destroy()
        self.soln_page()
        
