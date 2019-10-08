# Admin GUI

from tkinter import ttk
from tkinter import messagebox as tm
import views
import tkinter as tk
import ast

class Admin(tk.Frame):
    def __init__(self,master,data):
        tk.Frame.__init__(self, master)
        self.master = master

        # Configuring
        #tk.attributes("-fullscreen",True)
        self.master.geometry("{0}x{1}+0+0".format(self.master.winfo_screenwidth()-10, self.master.winfo_screenheight()-10))
        self.master.title("Attendance System")
        #self.master.configure(background = "red")

        # Data
        self.data = data
        self.data["details"] = ast.literal_eval(self.data["details"])

        # ****** NavBar ******
        self.navbar = tk.Frame(self.master, background = "black")

        self.navbar_ui()
        
        self.navbar.pack(side="left",fill = "y")


        # Creating Frame
        self.frame = tk.Frame(self.master)

        self.welcome_page()

        # Creating page layout
        self.frame.pack()

    def navbar_ui(self):
        """ NavBar UI """
        children = list(self.navbar.children.values())
        for child in children:
            child.destroy()
         
        # Declaring the elements
        self.name = tk.Button(self.navbar, text = "Attendance System", bg = "black", fg = "white", 
                    relief = "flat", font = ("Georgia", "12", "bold"), command = self.welcome_page)
        self.sign_up = tk.Button(self.navbar, text = "Manage Students", bg = "black", fg = "white", 
                        relief = "flat", font = ("Georgia", "12", "bold"), command = self._manage_students_btn_clicked)
        self.login = tk.Button(self.navbar, text = "Logout", bg = "black", fg = "white", 
                        relief = "flat", font = ("Georgia", "12", "bold"), command = self._logout_btn_clicked)
        self.problem = tk.Button(self.navbar, text = self.data["details"]["name"]+"\nAdmin", bg = "black", fg = "white", 
                        relief = "flat", font = ("Georgia", "12", "bold"), command = self.profile)
        self.soln = tk.Button(self.navbar, text = "Manage Teachers", bg = "black", fg = "white", 
                        relief = "flat", font = ("Georgia", "12", "bold"), command = self._manage_teachers_btn_clicked)

       # Layout
        self.name.pack(anchor="center",pady=30)
        self.problem.pack(anchor="center",pady=30)
        self.soln.pack(anchor="center",pady=30)
        self.sign_up.pack(anchor="s",pady=30)
        self.login.pack(anchor="s",pady=30)        

    def welcome_page(self):
        """ Welcome Page """
        self.destroy_frame()
        ttk.Label(self.frame, text = "Welcome\n"+self.data["details"]["name"].capitalize()+"!", font = ("Georgia", 30, "bold"), 
                foreground = "red").pack(anchor = "center")

    def destroy_frame(self):
        """ Destroying the frame widgets """
        children = list(self.frame.children.values())
        for child in children:
            child.destroy()

    def profile(self):
        """ Profile of the admin """
        self.destroy_frame()

        # Styles
        s = ttk.Style()
        s.configure("heading.TLabel", font = ("Georgia", 30, "bold"), foreground = "red")
        s.configure("")

        ttk.Label(self.frame, text = "Profile", style = "heading.TLabel").grid(row = 0, columnspan = 2, padx = 10, pady = 20)
        
        ttk.Label(self.frame, text = "UId : ", font = ("Arial", 20, "bold")).grid(row = 1, column = 0, padx = 10, pady = 10, sticky = "e")
        ttk.Label(self.frame, text = self.data["u_id"], font = ("Arial", 20, )).grid(row = 1, column = 1, padx = 10, pady = 10)
       
        ttk.Label(self.frame, text = "Name : ", font = ("Arial", 20, "bold")).grid(row = 2, column = 0, padx = 10, pady = 10, sticky = "e")
        ttk.Label(self.frame, text = self.data["details"]["name"], font = ("Arial", 20, )).grid(row = 2, column = 1, padx = 10, pady = 10)
        
        ttk.Label(self.frame, text = "Department : ", font = ("Arial", 20, "bold")).grid(row = 3, column = 0, padx = 10, pady = 10, sticky = "e")
        ttk.Label(self.frame, text = self.data["details"]["dept_id"], font = ("Arial", 20, )).grid(row = 3, column = 1, padx = 10, pady = 10)
        
        ttk.Label(self.frame, text = "Gender : ", font = ("Arial", 20, "bold")).grid(row = 4, column = 0, padx = 10, pady = 10, sticky = "e")
        ttk.Label(self.frame, text = self.data["details"]["gender"], font = ("Arial", 20, )).grid(row = 4, column = 1, padx = 10, pady = 10)
        
        ttk.Label(self.frame, text = "E-mail Id : ", font = ("Arial", 20, "bold")).grid(row = 5, column = 0, padx = 10, pady = 10, sticky = "e")
        ttk.Label(self.frame, text = self.data["email_id"], font = ("Arial", 20, )).grid(row = 5, column = 1, padx = 10, pady = 10)
        
    def destroy_page(self):
        """ Destory the page """
        self.navbar.destroy()
        self.frame.destroy()

    def _logout_btn_clicked(self, ):    
        """ Logs out the user """
        self.destroy_page()
        import MainPage
        MainPage.MainPage(self.master).login_page(1)

    def _manage_students_btn_clicked(self):
        """ Navigates to manage user frame after clearing the frame """
        self.destroy_frame()
        self.manage_students()
    
    def manage_students(self):
        """ Can view the details of the students """
        self.btn_frame = ttk.Frame(self.frame)
        self.table_frame = ttk.Frame(self.frame)

        self.btn_frame.pack()
        self.table_frame.pack()

        # Widgets
        ttk.Label(self.btn_frame, text = "Select Class : ").grid(row = 0, padx = 10, pady = 10)
        self.class_select = ttk.Combobox(self.btn_frame, values = ["D1", "D2", "D3", "D4"])
        self.class_select.current(0)
        self.class_select.grid(row = 0, column = 1, padx = 10, pady = 10)

        tk.Button(self.btn_frame, text = "GO", padx = 15, 
                        font = ("Georgia", 10, "bold"), background = "#06C5CA", foreground = "white", 
                        command = self.student_details).grid(row = 1, columnspan = 2, sticky = "e", pady = 10)

    def student_details(self):
        """ Student details displayed """
        data = views.get_student_details(self.class_select.get(), 1)
        #print(data)
        col = ["uid", "name", "roll no", "gender", "email"]

        s = ttk.Style()
        s.configure("TLabelframe.Label", font = ("Georgia", 16, "bold"), foreground = "red")

        self.att_label_frame = ttk.LabelFrame(self.table_frame, text = "Class : " + self.class_select.get())
        self.att_label_frame.configure(borderwidth = 30)
        self.att_label_frame.pack(padx = 30, pady = 30)

        self.tree = ttk.Treeview(self.att_label_frame, selectmode = "extended", style = "Custom.Treeview")
        self.treesb = ttk.Scrollbar(self.frame, orient = "vertical", command = self.tree.yview)
        self.tree.configure(yscrollcommand = self.treesb.set)
        self.tree.pack()
        self.tree["columns"] = tuple(col)
        self.tree["show"] = "headings"

        self.tree.tag_configure("evenrow", foreground = "black", background = "#D3D3D3", font = ('Georgia',10))
        self.tree.tag_configure("oddrow", foreground = "black", background = "#FFFFFF", font = ('Georgia',10))

        for c in col:
            self.tree.column(c, width = 100, anchor = "c")
            self.tree.heading(c, text = c.capitalize())
        
        for r in list(data.keys()):
            values = list()
            values.extend(
                (data[r]["u_id"], data[r]["name"], r, data[r]["gender"], data[r]["email_id"])
            )

            if int(r)%2:
                tag = "oddrow"
            else:
                tag = "evenrow"

            self.tree.insert("", 'end', text = r, values = values, tag = tag)   
        
        self.tree.bind("<ButtonRelease-1>",self.row_clicked)

    def _manage_teachers_btn_clicked(self):
        """ Navigates to manage teachers frame after destroying the frame """
        self.destroy_frame()
        teacher_details = views.get_teacher_details()
        self.manage_teachers(teacher_details)
    
    def manage_teachers(self, t_det):
        """ Manage teachers frame widgets defined here """
        # Dividing main frame into two
        self.btn_frame = ttk.Frame(self.frame)
        self.detials_frame = ttk.Frame(self.frame)

        self.btn_frame.pack()
        self.detials_frame.pack()

        # Creating add teacher btn
        children = list(self.btn_frame.children.values())
        for child in children:
            child.destroy()

        children = list(self.detials_frame.children.values())
        for child in children:
            child.destroy()
            
        self.add = tk.Button(self.btn_frame, text = "Add New Teacher", foreground = "white", background = "#0582F3",
                    font = ("Georgia", 12, "bold"), padx = 30, command = self.add_teacher)
        self.add.pack(side = "left",  padx = 10, pady = 40)

        if t_det == -1:
            ttk.Label(self.frame, text = "No records found!", font = ("Arial", 24, "bold")).pack(anchor = "center", padx = 10, pady = 15)
        else:
            self.t_details_table(t_det)            

    def t_details_table(self, t_det):
        """ Creates the teachers table """
        col = ["UId", "Name", "Department", "gender", "Role", "Email"]

        self.tree = ttk.Treeview(self.detials_frame, selectmode = "extended", style = "Custom.Treeview")
        self.treesb = ttk.Scrollbar(self.detials_frame, orient = "vertical", command = self.tree.yview)
        self.tree.configure(yscrollcommand = self.treesb.set)

        self.tree["columns"] = tuple(col)
        self.tree["show"] = "headings"

        self.tree.tag_configure("evenrow", foreground = "black", background = "#D3D3D3", font = ('Georgia',10))
        self.tree.tag_configure("oddrow", foreground = "black", background = "#FFFFFF", font = ('Georgia',10))

        w = 130
        for c in col:
            if c is "Email" or c is "Role":
                w = 155
            self.tree.column(c, width = w, anchor = "c")
            self.tree.heading(c, text = c.capitalize())
        
        role = {
            1 : "Subject Teacher",
            2 : "Class Teacher",
        }

        dept_id = {
            1 : "dept1",
            2 : "dept2",
            3 : "dept3",
            4 : "dept4",
        }
        x = 0
        _role = ""
        for r in t_det:
            if r["role"] == 2:
                _role = str(role[int(r["role"])]) + " (" +str(r["class"]) + ")"
            else:
                _role = role[int(r["role"])]
            values = list()
            values.extend(
                (r["u_id"], r["details"]["name"], dept_id[int(r["details"]["dept_id"])], r["details"]["gender"], _role,r["email_id"])
            )

            if x%2:
                tag = "oddrow"
            else:
                tag = "evenrow"

            x += 1

            self.tree.insert("", 'end', text = r, values = values, tag = tag)   

        self.tree.bind("<ButtonRelease-1>",self.row_clicked)
        #self.tree.insert("",'end',text="L",values=(1, "Harshita", "F", "phone_no",))
            

        self.tree.pack(padx = 10, pady = 10)

    def row_clicked(self, event):
        data = self.tree.item(self.tree.focus())["values"]
        answer = tm.askquestion("Delete?","Do you want to delete " + data[1] +" ?")

        if answer == "yes":
            views.delete_user(data[0])
            tm.showinfo("Deleted!","User successfully deleted")

    def add_teacher(self):
        """ Adds a new teacher to the database """
        children = list(self.detials_frame.children.values())
        for child in children:
            child.destroy()

        # Updating the button
        self.add.configure(text = "View Teachers", command = self._manage_teachers_btn_clicked)

        # Style
        style = ttk.Style()
        style.configure('btn.TButton', font = ('Trebuchet MS', 12), foreground = "#ffffff", background = "#0fd2ee")
        style.configure('label.TLabel', font = ('Trebuchet MS', 14), foreground = "Black", padding = 2, relief = "flat")
        
        # Widgets
        self.add_teacher_frame = tk.LabelFrame(self.detials_frame, text = "", padx = 50, pady = 40, borderwidth = 10,
                                highlightthickness = 5, highlightbackground = "white")
        self.add_teacher_frame.pack()

        self.name_label = ttk.Label(self.add_teacher_frame, text = "Enter name : ", style = "label.TLabel")
        self.name = ttk.Entry(self.add_teacher_frame)
        
        self.email_id_label = ttk.Label(self.add_teacher_frame, text = "Enter email-id : ", style = "label.TLabel")
        self.email_id = ttk.Entry(self.add_teacher_frame)

        #self.username_label = ttk.Label(self.frame, text = "Enter username : ", style = "label.TLabel")
        #self.username = ttk.Entry(self.frame)
        
        self.password_label = ttk.Label(self.add_teacher_frame, text = "Enter password : ", style = "label.TLabel")
        self.password = ttk.Entry(self.add_teacher_frame, show = "*")
        
        self.dept_name_label = ttk.Label(self.add_teacher_frame, text = "Select department : ", style = "label.TLabel")
        self.dept_name = ttk.Combobox(self.add_teacher_frame, values = ["dept1",'dept2', 'dept3', 'dept4'])
        self.dept_name.current(0)

        self.room_label = ttk.Label(self.add_teacher_frame, text = "Enter class(if class teacher) : ", style = "label.TLabel")
        self.room = ttk.Entry(self.add_teacher_frame)

        self.gender = tk.IntVar()
        self.gender_label = ttk.Label(self.add_teacher_frame, text = "Gender : ", style = "label.TLabel")
        self.male = ttk.Radiobutton(self.add_teacher_frame, text = "Male", value = 0, variable = self.gender)
        self.female = ttk.Radiobutton(self.add_teacher_frame, text = "Female", value = 1, variable = self.gender)

        self.phone_no_label = ttk.Label(self.add_teacher_frame, text = "Select Role : ", style = "label.TLabel")
        self.phone_no = ttk.Combobox(self.add_teacher_frame, values = [1,2])
        self.phone_no.current(0)

        self.submitbtn = tk.Button(self.add_teacher_frame, text = "SUBMIT", command = self._submit_btn_clicked,
                            font = ('Trebuchet MS', 12), foreground = "white", background = "#0861E5", padx = 50, pady = 0)
        self.resetbtn = tk.Button(self.add_teacher_frame, text = "RESET", command = self._reset_btn_clicked,
                            font = ('Trebuchet MS', 12), foreground = "white", background = "red", padx = 50, pady = 0)
        
        ttk.Label(self.add_teacher_frame, text = "Teacher Registration", font = ("Georgia", 16, "bold"), foreground = "black").grid(row = 0, columnspan = 2, pady = 5)
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
            
            if self.room.get() == "":
                ct = "NULL"
            else :
                ct = self.room.get()
            data = {
                'details'   : 
                {
                    'name'      : self.name.get(), 
                    "gender"    : gender, 
                    "dept_id"   : dept_id,
                    "roll_no"   : "NULL"
                },
                'password'  : self.password.get(),
                'email_id'  : self.email_id.get(),
                "class"     : ct,
                "role_id"   : int(self.phone_no.get())
                }
            print(data)
            views.store(data, self.master)
            tm.showinfo("Successfully Added!", "New teacher was successfully added")
            self._manage_teachers_btn_clicked()
    
    def _reset_btn_clicked(self):
        """ Resets all the fields """
        self.name.delete(0, "end")
        self.email_id.delete(0, "end")
        self.password.delete(0, "end")
        self.gender.set(value = None)
        self.dept_name.current(0)
        self.phone_no.current(0)
        self.room.delete(0, "end")
        #self.username.delete(0, "end")
        return



