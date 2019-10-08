from tkinter import ttk
from tkinter import messagebox as tm
import views
import ast
import tkinter as tk
import datetime
from datetime import date

##Class Teacher GUI
class ClassTeacher(tk.Frame):
    def __init__(self,master,data):
            tk.Frame.__init__(self, master)
            self.master = master

            # Configuring
            #tk.attributes("-fullscreen",True)
            self.master.geometry("{0}x{1}+0+0".format(self.master.winfo_screenwidth()-10, self.master.winfo_screenheight()-10))
            self.master.title("Attendance Management System")
            #self.master.configure(background = "red")

            # Data
            self.data = data
            self.data["details"] = ast.literal_eval(self.data["details"])

            # Creating Frames
            self.navbar = tk.Frame(self.master, bg = "black")
            self.frame = tk.Frame(self.master)

            
            # Creating page layout
            self.navbar_ui()
            self.welcome_page()
            self.navbar.pack(side = "left", fill = "y")
            self.frame.pack()
        
    def navbar_ui(self):
        """ NavBar UI """
        passchildren = list(self.navbar.children.values())
        for child in passchildren:
            child.destroy()
         
        # Declaring the elements
        self.name = tk.Button(self.navbar, text = "Attendance System", bg = "black", fg = "white", 
                    relief = "flat", font = ("Georgia", 12, "bold"), command = self.welcome_page)
        self.sign_up = tk.Button(self.navbar, text = "Class Attendance", bg = "black", fg = "white", 
                        relief = "flat", font = ("Georgia", "12", "bold"), command = self._class_attendance_btn_clicked)
        self.login = tk.Button(self.navbar, text = "Logout", bg = "black", fg = "white", 
                        relief = "flat", font = ("Georgia", "12", "bold"), command = self._logout_btn_clicked)
        self.problem = tk.Button(self.navbar, text = self.data["details"]["name"].capitalize()+"\nClass Teacher", bg = "black", fg = "white", 
                        relief = "flat", font = ("Georgia", "12", "bold"), command = self.profile)
        self.soln = tk.Button(self.navbar, text = "View Attendance", bg = "black", fg = "white", 
                        relief = "flat", font = ("Georgia", "12", "bold"), command = self._view_attendance_btn_clicked)
        self.mark_attedance = tk.Button(self.navbar, text = "Mark Attendance", bg = "black", fg = "white", 
                        relief = "flat", font = ("Georgia", "12", "bold"), command = self._mark_attendance_btn_clicked)
        self.edit_attedance = tk.Button(self.navbar, text = "Edit Attendance", bg = "black", fg = "white", 
                        relief = "flat", font = ("Georgia", "12", "bold"), command = self._edit_attendance_btn_clicked)
            

        # Placing them
        self.name.pack(anchor="center",pady=30)
        self.problem.pack(anchor="center",pady=30)
        self.soln.pack(anchor="center",pady=30)
        self.mark_attedance.pack(anchor="center",pady=30)
        self.edit_attedance.pack(anchor="center",pady=30)
        self.sign_up.pack(anchor="s",pady=30)
        self.login.pack(anchor="s",pady=30)        

    def welcome_page(self):
        """ Welcome Page """
        self.destroy_frame()
        ttk.Label(self.frame, text = "Welcome\n"+self.data["details"]["name"].capitalize()+"!", font = ("Georgia", 30, "bold"), 
                foreground = "red").pack(anchor = "center")

    def profile(self):
        """ Profile of the class teacher """
        self.destroy_frame()

        # Styles
        s = ttk.Style()
        s.configure("heading.TLabel", font = ("Georgia", 30, "bold"), foreground = "red")
        s.configure("")

        ttk.Label(self.frame, text = "Profile", style = "heading.TLabel").grid(row = 0, columnspan = 2, padx = 10, pady = 20)
        #print(self.data)
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
        
        ttk.Label(self.frame, text = "Class Teacher of : ", font = ("Arial", 20, "bold")).grid(row = 6, column = 0, padx = 10, pady = 10, sticky = "e")
        ttk.Label(self.frame, text = self.data["class"], font = ("Arial", 20, )).grid(row = 6, column = 1, padx = 10, pady = 10)
        
        ttk.Label(self.frame, text = "Subjects Taught : ", font = ("Arial", 20, "bold")).grid(row = 7, column = 0, padx = 10, pady = 10, sticky = "e")
        
        sub_list = views.get_subject(self.data["u_id"])
        classes = list(sub_list["subjects"].keys())
        
        # Display Order : Subject(class)
        row = 7
        col = 1
        for c in classes:
            for s in sub_list["subjects"][c]:
                sub = s + " (" + c + ")"
                ttk.Label(self.frame, text = sub, font = ("Arial", 12, )).grid(row = row, column = col, padx = 10, pady = 10)
                row += 1

    def destroy_frame(self):
        """ Destroying the frame widgets """
        children = list(self.frame.children.values())
        for child in children:
            child.destroy()

    def destroy_page(self):
        """ Destory the page """
        self.navbar.destroy()
        self.frame.destroy()

    def _logout_btn_clicked(self, ):    
        """ Logs out the user """
        self.destroy_page()
        import MainPage
        MainPage.MainPage(self.master).login_page(1)

    def _class_attendance_btn_clicked(self):
        """ Can view the class attendance subject-vise """
        self.destroy_frame()
        attendance, students = views.get_class_attendance(self.data["class"])
        self._class_attendance_view(attendance, students)
    
    def _class_attendance_view(self, attendance, students):
        """ Create the view for class attendance.
            Attendance can be viewed subject-wise """

        subjects = list(attendance.keys())
        
        col = ["roll_no", "name"]
        for x in subjects:
            col.append(x)
        # Style
        s = ttk.Style()
        s.configure("heading.TLabel", font = ("Georgia", 30, "bold"), foreground = "red")

        ttk.Label(self.frame, text = self.data["class"]+" Class Attendance", style = "heading.TLabel").pack(anchor = "center", padx = 30, pady = 30)
        
        self.tree = ttk.Treeview(self.frame, selectmode = "extended", style = "Custom.Treeview")
        self.treesb = ttk.Scrollbar(self.frame, orient = "vertical", command = self.tree.yview)
        self.tree.configure(yscrollcommand = self.treesb.set)

        self.tree["columns"] = tuple(col)
        self.tree["show"] = "headings"

        for heading in col:
            self.tree.column(heading, width = 100, anchor = "c")
            if heading.find(" ") == -1:    
                self.tree.heading(heading, text = heading.upper())
            else:
                self.tree.heading(heading, text = heading.capitalize())
        
        self.tree.tag_configure("evenrow", foreground = "black", background = "#D3D3D3", font = ('Georgia',10))
        self.tree.tag_configure("oddrow", foreground = "black", background = "#FFFFFF", font = ('Georgia',10))

        # Inserting values into table
        r = list(students.keys())
        for x in r:
            if int(x)%2:
                tag = "oddrow"
            else:
                tag = "evenrow"
            
            values = list()
            values.append(x)
            values.append(students[x]["name"])
            for h in col[2:]:
                values.append(format(attendance[h][int(x)-1],"0.2f"))
            
            self.tree.insert("", "end", text = r, values = tuple(values), tag = tag)            

        self.tree.pack(padx = 20, pady = 20)

    def _view_attendance_btn_clicked(self):
        """ Can view the attendance of the subjects taught by the teacher"""
        self.destroy_frame()
        data = views.get_subject(self.data["u_id"])
        self.subject_attendance_view(data)
    
    def subject_attendance_view(self, data):
        """ Subject Attendnace View """
        classes = list(data["subjects"].keys())
        
        # Display Order : Subject(class)
        subjects = list()

        for c in classes:
            for s in data["subjects"][c]:
                sub = s + " (" + c + ")"
                subjects.append(sub)    
        #print(subjects)

        # Creating two frames
        self.select_subject_frame = ttk.Frame(self.frame)
        self.subject_attendance_frame = ttk.Frame(self.frame)

        # Packing the frames
        self.select_subject_frame.pack()
        self.subject_attendance_frame.pack()

        # Styles
        s = ttk.Style()
        s.configure("a.TLabel", font = ("Georgia", 12, "bold"), padx = 5, pady = 5)
        s.map("TCombobox", fieldbackground = [("disabled","grey")])
        s.configure("TCombobox", font = ("Arial", 10), pady = 10)

        # Creating widgets
        # self.select_subject_frame widgets
        ttk.Label(self.select_subject_frame, text = "Select Class : ", style = "a.TLabel").grid(row = 0, column = 0, sticky = "e", padx = 20, pady = 20)
        self.class_list = ttk.Combobox(self.select_subject_frame, values = classes, width = 40)
        #self.class_list.current(0)
        self.class_list.grid(row = 0, column = 1, padx = 20, pady = 20, sticky = "ne")
        ttk.Label(self.select_subject_frame, text = "Select Subject : ", style = "a.TLabel").grid(row = 0, column = 3, sticky = "e", padx = 20, pady = 20)
        self.subject_list = ttk.Combobox(self.select_subject_frame, state = "disabled", width = 40)
        self.subject_list.grid(row = 0, column = 4, padx = 20, pady = 20, sticky = "ne")
        
        self.class_list.bind("<<ComboboxSelected>>", lambda event : self._enable_list(data["subjects"][self.class_list.get()]))

        tk.Button(self.select_subject_frame, text = "GO", padx = 15, 
                        font = ("Georgia", 10, "bold"), background = "#06C5CA", foreground = "white", 
                        command = lambda : self.show_attendance(data,self.class_list.get(),
                                self.subject_list.get())).grid(row = 1, columnspan = 3, sticky = "e", pady = 10)

    def _mark_attendance_btn_clicked(self):
        self.destroy_frame()
        self.mark_attedance_view()
    
    def mark_attedance_view(self):
        # Styles
        s = ttk.Style()
        s.configure("a.TLabel", font = ("Georgia", 12, "bold"), padx = 5, pady = 5)
        s.map("TCombobox", fieldbackground = [("disabled","grey")])
        s.configure("TCombobox", font = ("Arial", 10), pady = 10)

        today = date.today()
        d1 = today.strftime("%Y-%m-%d")
        
        ttk.Label(self.frame,text = "Date :", style = "a.TLabel").grid(row = 0, column = 0, sticky = "e", padx = 20, pady = 20)
        date_txt = ttk.Entry(self.frame,text = str(d1))
        date_txt.insert('end', str(d1))
        date_txt.configure(state='disabled')
        date_txt.grid(row = 0, column = 1, padx = 20, pady = 20, sticky = "ne")

        
        list_lec = views.list_lec(self.data)
        data = views.get_subject(self.data["u_id"])
        classes = list(data["subjects"].keys())
        
        # Display Order : Subject(class)
        subjects = list()

        for c in classes:
            for s in data["subjects"][c]:
                sub = s + " (" + c + ")"
                subjects.append(sub)
            print(subjects)    
        
        ttk.Label(self.frame,text = "Select Class :" ,state = "disabled" ,style = "a.TLabel").grid(row = 0, column = 2, sticky = "e", padx = 20, pady = 20)
        self.class_list = ttk.Combobox(self.frame, values = classes, width = 40)
        self.class_list.grid(row = 0, column = 3, padx = 20, pady = 20, sticky = "ne")

        self.class_list.bind("<<ComboboxSelected>>", lambda event : self._enable_list(data["subjects"][self.class_list.get()]))

        ttk.Label(self.frame, text = "Select Subject : ", style = "a.TLabel").grid(row = 1, column = 0, sticky = "e", padx = 20, pady = 20)
        self.subject_list = ttk.Combobox(self.frame, state = "disabled", width = 40)
        self.subject_list.grid(row = 1, column = 1, padx = 20, pady = 20, sticky = "ne")

        tk.Button(self.frame, text = "GO", padx = 15, 
                        font = ("Georgia", 10, "bold"), background = "#06C5CA", foreground = "white", 
                        command = lambda : self.mark_att_face(data,self.class_list.get(),self.subject_list.get())).grid(row = 2, columnspan = 2, sticky = "e", pady = 10)

    def mark_att_face(self,data,class1,sub1):
        #print(self.data,data)
        #return
        """ Marking Attendace """
        import facialRecog
        obj = facialRecog.FacialRecog() #obj.uid contain present students uid
        #print(obj.uid)
        #uids_rolls = obj.detect_face()
        
        #get students uid of that class
        list_uid = views.get_class_uid(class1)
        #print(list_uid)
        uids_rolls = [] #contains all present students uid of selected class

        for i in obj.uid:
            if i in list_uid:
                uids_rolls.append(int(i))

        
        #uids_rolls = list(range(7,8))
        time = datetime.datetime.now()
        date = time.strftime("%Y-%m-%d")
        time1 = time.strftime("%H:%M:%S")
        dict1 = {
            "class1": class1,
            "subject" : sub1,
            "uids_rolls" : uids_rolls,
            "time" : time1,
            "date" : date,
            "sub_alot_id" : data['sub_alot_id']
        }
        views.mark_att(self.data,dict1)
        
        
        tk.messagebox.showinfo("Success","Attendance Marked Successfullly.....")

    def _enable_list(self, values):
        """ Enabling subject_list combobox """
        self.subject_list['state'] = "normal"
        self.subject_list['values'] = values

    def show_attendance(self, data, selected_class, subject):
        """ Displays the attendance of the selected class """
        children = list(self.subject_attendance_frame.children.values())
        for child in children:
            child.destroy()
        # Style
        s = ttk.Style()
        s.configure("TLabelframe.Label", font = ("Georgia", 16, "bold"), foreground = "red")

        att_details, student_details = views.get_attendance(data["sub_alot_id"], selected_class, subject, 0)
        #print(att_details)
        #print(student_details)

        col = ["Roll No.", "Name"]
        for c in list(att_details.keys()):
            col.append(c)

        self.att_label_frame = ttk.LabelFrame(self.subject_attendance_frame, text = subject + " - " + selected_class,)
        self.att_label_frame.configure(borderwidth = 30)
        self.att_label_frame.pack(padx = 30, pady = 30)

        self.tree = ttk.Treeview(self.att_label_frame, selectmode = "extended", style = "Custom.Treeview")
        self.treesb = ttk.Scrollbar(self.frame, orient = "vertical", command = self.tree.yview)
        self.tree.configure(yscrollcommand = self.treesb.set)

        self.tree["columns"] = tuple(col)
        self.tree["show"] = "headings"

        self.tree.tag_configure("evenrow", foreground = "black", background = "#D3D3D3", font = ('Georgia',10))
        self.tree.tag_configure("oddrow", foreground = "black", background = "#FFFFFF", font = ('Georgia',10))

        for c in col:
            self.tree.column(c, width = 90, anchor = "c")
            self.tree.heading(c, text = c.capitalize())
        
        for r in list(student_details.keys()):
            values = list()
            values.append(r)
            values.append(student_details[r]["name"])

            if int(r)%2:
                tag = "oddrow"
            else:
                tag = "evenrow"

            for c in col[2:]:
                values.append(format(att_details[c][int(r)-1],"0.2f"))
            self.tree.insert("", 'end', text = r, values = values, tag = tag)   


        #self.tree.insert("",'end',text="L",values=(1, "Harshita", "F", "phone_no",))
            

        self.tree.pack(padx = 10, pady = 10)

    def _edit_attendance_btn_clicked(self):
        """ Can view the attendance of the subjects taught by the teacher"""
        self.frame.destroy()
        self.frame = ttk.Frame(self.master)
        self.frame.pack()
        data = views.get_subject(self.data["u_id"])
        self.edit_attendance_form(data)
    
    def edit_attendance_form(self,data):
        classes = list(data["subjects"].keys())
        
        # Display Order : Subject(class)
        subjects = list()

        for c in classes:
            for s in data["subjects"][c]:
                sub = s + " (" + c + ")"
                subjects.append(sub)    
        #print(subjects)

        # Creating two frames
        self.select_subject_frame = ttk.Frame(self.frame)
        self.subject_attendance_frame = ttk.Frame(self.frame)

        # Packing the frames
        self.select_subject_frame.pack()
        self.subject_attendance_frame.pack()

        # Styles
        s = ttk.Style()
        s.configure("a.TLabel", font = ("Georgia", 12, "bold"), padx = 5, pady = 5)
        s.map("TCombobox", fieldbackground = [("disabled","grey")])
        s.configure("TCombobox", font = ("Arial", 10), pady = 10)
        s.configure('label.TLabel', font=('Trebuchet MS', 28), foreground="red", padding=2)

        # Creating widgets
        # self.select_subject_frame widgets
        ttk.Label(self.select_subject_frame,text = "Edit Attendance",style = "label.TLabel").grid(row = 0,columnspan = 4,padx = 20, pady = 20)
        
        ttk.Label(self.select_subject_frame, text = "Select Class : ", style = "a.TLabel").grid(row = 1, column = 0, sticky = "e", padx = 20, pady = 20)
        self.class_list = ttk.Combobox(self.select_subject_frame, values = classes, width = 40)
        #self.class_list.current(0)
        self.class_list.grid(row = 1, column = 1, padx = 20, pady = 20, sticky = "ne")
        ttk.Label(self.select_subject_frame, text = "Select Subject : ", style = "a.TLabel").grid(row = 1, column = 3, sticky = "e", padx = 20, pady = 20)
        self.subject_list = ttk.Combobox(self.select_subject_frame, state = "disabled", width = 40)
        self.subject_list.grid(row = 1, column = 4, padx = 20, pady = 20, sticky = "ne")
        
        ttk.Label(self.select_subject_frame,text="Month : ",style = "a.TLabel").grid(row = 2, column = 0, sticky = "e", padx = 20, pady = 20)
        self.month = ttk.Combobox(self.select_subject_frame,values=list(range(1,13)),width=20,state = "disabled")
        self.month.grid(row = 2, column = 1, sticky = "e", padx = 20, pady = 20)

        ttk.Label(self.select_subject_frame,text="Date : ",style = "a.TLabel").grid(row = 2, column = 3, sticky = "e", padx = 20, pady = 20)
        self.date = ttk.Combobox(self.select_subject_frame,state = "disabled")
        self.date.grid(row = 2, column = 4, sticky = "e", padx = 20, pady = 20)

        ttk.Label(self.select_subject_frame,text = "Year : ",style = "a.TLabel").grid(row = 3,column = 0,sticky = "e",padx =  20, pady = 20)
        self.year = ttk.Combobox(self.select_subject_frame,state = "disabled")
        self.year.grid(row = 3, column = 1, sticky = "e", padx = 20, pady = 20)

        ttk.Label(self.select_subject_frame,text = "Lecture : ",style = "a.TLabel").grid(row = 3,column = 3,sticky = "e",padx =  20, pady = 20)
        self.lecture = ttk.Combobox(self.select_subject_frame,state = "disabled")
        self.lecture.grid(row = 3, column = 4, sticky = "e", padx = 20, pady = 20)

        self.year.bind("<<ComboboxSelected>>",lambda event : self.enable_myform('year'))
        self.date.bind("<<ComboboxSelected>>",lambda event : self.enable_myform('date'))
        self.subject_list.bind("<<ComboboxSelected>>",lambda event : self.enable_myform('subject_list'))
        self.month.bind("<<ComboboxSelected>>",lambda event : self.enable_myform('month'))
        self.lecture.bind("<<ComboboxSelected>>",lambda event : self.enable_myform('lecture'))
        self.class_list.bind("<<ComboboxSelected>>", lambda event : self._enable_list(data["subjects"][self.class_list.get()]))

        self.b1 = tk.Button(self.select_subject_frame, text = "GO", padx = 15, 
                        font = ("Georgia", 10, "bold"), background = "#06C5CA", foreground = "white", 
                        command = lambda : self.edit_attendance(self.data),state="disabled")
        self.b1.grid(row = 4, columnspan = 3, sticky = "e", pady = 10)

    def enable_myform(self,parent):
        if parent == 'subject_list':
            self.month['state'] = "normal"
            self.month['values'] = list(range(1,13))
        elif parent == 'month':
            if int(self.month.get())%2 == 1 or int(self.month.get()) == 8:
                self.date['state'] = "normal"
                self.date['values'] = list(range(1,32))
            else:
                self.date['state'] = "normal"
                self.date['values'] = list(range(1,29))
        elif parent == 'year':
            self.lecture['state'] = "normal"
            self.lecture['values'] = [1,2,3]
        elif parent == 'date':
            self.year['state'] = "normal"
            now = datetime.datetime.now()
            list1 = list(range(now.year-1,now.year+2))
            self.year['values'] = list1
        elif parent == 'lecture':
            self.b1['state'] = "normal"

    def edit_attendance(self,data):
        #print(data,"\n\n\n\n")
        self.data['sub_alot_id'] = views.get_sub_alot_id(self.data["u_id"],self.class_list.get(),self.subject_list.get())
        print(self.data)

        try:
            print(self.uids)
            self.uids = []
            print(self.uids)
        except:
            pass
        class_list = self.class_list.get()
        subject_list = self.subject_list.get()
        month = self.month.get()
        year = self.year.get()
        date = self.date.get()
        lec = self.lecture.get()
        date1 = {
            "dd" : date,
            "mm" : month,
            "yy" : year
        }
        dat = views.edit_att_list(data,date1)
        #print(dat,"hiii",'\n\n')
        if dat == -1:
            tm.showerror("Error","No Attendance Marked....")
            return
        det = list(dat.values())
        uids = []
        for i in det:
            if i[0] == class_list and i[1] == subject_list:
                uids.extend(i[2])
                break

        if len(uids) == 0:
            tm.showerror("Error","No Attendance Marked....")
            return
        self.display_attendance(data,uids)

    def display_attendance(self,data,uids):
        #print(self.data,uids)
        children = list(self.subject_attendance_frame.children.values())
        for child in children:
            child.destroy()
        
        #get list of all class uids
        class_var = self.class_list.get()
        class_records = views.get_uids(class_var)
        self.uids = uids
        # Style
        s = ttk.Style()
        s.configure("TLabelframe.Label", font = ("Georgia", 16, "bold"), foreground = "red")

        col = ["Roll No.","Uid","Name","Present/Absent"]

        self.att_label_frame = ttk.LabelFrame(self.subject_attendance_frame, text = "Class : " + self.class_list.get() + " => " + "Subject : " + self.subject_list.get())
        self.att_label_frame.configure(borderwidth = 30)
        self.att_label_frame.pack(padx = 30, pady = 30)

        self.tree = ttk.Treeview(self.att_label_frame, selectmode = "extended", style = "Custom.Treeview")
        self.treesb = ttk.Scrollbar(self.frame, orient = "vertical", command = self.tree.yview)
        self.tree.configure(yscrollcommand = self.treesb.set)

        self.tree["columns"] = tuple(col)
        self.tree["show"] = "headings"

        self.tree.tag_configure("evenrow", foreground = "black", background = "#D3D3D3", font = ('Georgia',10))
        self.tree.tag_configure("oddrow", foreground = "black", background = "#FFFFFF", font = ('Georgia',10))

        for c in col:
            self.tree.column(c, width = 90, anchor = "c")
            self.tree.heading(c, text = c.capitalize())

        count = 0
        for rec in class_records:
            values = list()
            det = eval(rec[1])
            values.append(det['roll_no'])
            values.append(rec[0])
            values.append(det['name'])

            if int(det['roll_no']) in uids:
                values.append("Present")
            else:
                values.append("Absent")
            
            if count%2 == 0:
                tag = "evenrow"
            else:
                tag = "oddrow"
            count+=1
            self.tree.insert("", 'end',text = count, values = values,tag = tag)
        
        self.tree.bind("<Button-1>", self.click)
        self.tree.pack(padx = 10, pady = 10)

    def click(self,event):
        #print(self.data)
        item = self.tree.identify_row(event.y)
        #print(item)
        if item:
            info = self.tree.item(item, 'values')
            print(item,info[3])
            dt = str(self.year.get()) + '-' + str(self.month.get()) + '-' + str(self.date.get())
            sub_al_id = self.data['sub_alot_id']
            if info[3] == "Present":
                var = tk.messagebox.askyesno("Confirm", "Mark " + str(info[2]) + " as Absent?")
                #print(var)
                if var == False:
                    return
                print(info)
                #print(type(info[1]),info[1])
                self.uids.remove(int(info[0]))
                print("\n",self.uids,"\n")
            else:
                var = tk.messagebox.askyesno("Confirm", "Mark " + str(info[2]) + " as Present?")
                if var == False:
                    return
                self.uids.append(int(info[0]))
                print("\n",self.uids,"\n")
            views.update_att_record(self.data['sub_alot_id'],dt,self.class_list.get(),self.subject_list.get(),self.uids)
            self.display_attendance(self.data,self.uids)

    def list_lec(self,data):
        self.frame.destroy()

        style = ttk.Style()
        style.configure('label.TLabel', font=('Trebuchet MS', 28), foreground="red")
        #Frame for displaying lectures and Lab took by the teacher
        
        #views.list_lec(data)
        list1 = list(views.list_lec(self.data))
        print(list1)
        self.frame = tk.Frame(self.master)

        label1 = ttk.Label(self.frame,text = "       List of       \nLectures And Labs",style="label.TLabel",padding=2)
        label1.grid(row=0,columnspan = 2)
        self.tree = ttk.Treeview(self.frame,selectmode='browse')
        self.tree.grid(row=1,columnspan=2,sticky="s")

        self.vsb = ttk.Scrollbar(self.frame, orient="vertical", command=self.tree.yview)
        self.vsb.grid(row=1,column=2,sticky="ns")

        self.tree.tag_configure("evenrow", foreground = "black", background = "#D3D3D3", font = ('Georgia',10))
        self.tree.tag_configure("oddrow", foreground = "black", background = "#FFFFFF", font = ('Georgia',10))

        self.tree.configure(yscrollcommand=self.vsb.set)
        self.tree["columns"] =("1","2")
        self.tree["show"] = "headings"
        self.tree.column("1", width=100, anchor='c')
        self.tree.column("2", width=100, anchor='c')
        self.tree.heading("1",text="Class")
        self.tree.heading("2",text="Subject")

        #print(type(list(list1)),list(list1))
        
        count = 0
        for i in range(len(list1)):
            #self.arr_id.append(data[i][0])
            var1 = list1[i][0]
            for j in list1[i][1]:
                if count%2 == 0:
                    tag = "evenrow"
                else:
                    tag = "oddrow"
                self.tree.insert("",'end', values=(var1,j),tag = tag)
                count+=1                
            

        self.frame.pack()
    
    def edit_attendace(self,data):
        self.frame.destroy()
        #View and Editing Attendance
        
        style = ttk.Style()
        style.configure('label.TLabel', font=('Trebuchet MS', 28), foreground="red")
        style.configure('BW.TLabel', font=('Trebuchet MS', 20))
        style.configure("X.TLabel", font="Arial", size="30", anchor="center")

        self.frame = tk.Frame(self.master)

        label0 = ttk.Label(self.frame,text="View/Edit Attendance",style="label.TLabel")
        label0.grid(row=0)
        ttk.Label(self.frame, text="Form :", style="label.TLabel").grid(row=1, columnspan=2, padx=10, pady=30)
        
        label1 = ttk.Label(self.frame,text="Class : ",style="BW.TLabel")
        #label1.grid(row=2,column=0)
        label1.grid(row=2, column=0)
        
        tkvar = tk.StringVar(self.frame)
        list1 = list(views.list_lec(data))
        list2 = set()
        for i in list1:
            list2.add(i[0])
        tkvar.set(list1[0][0])
        popupMenu = tk.OptionMenu(self.frame, tkvar, *list2)
        popupMenu.grid(row = 2, column =1)
        
        self.frame.pack()
    
