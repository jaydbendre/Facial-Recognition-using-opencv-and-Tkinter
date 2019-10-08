from tkinter import ttk
from tkinter import messagebox as tm
import views
import tkinter as tk
import ast
import datetime
from datetime import date


##Subject Teacher GUI Here
class Teacher(tk.Frame):
    def __init__(self,master,data):
        tk.Frame.__init__(self, master)
        print(data)
        self.master = master
        self.data = data
        self.data["details"] = ast.literal_eval(self.data["details"])

        # Configuring
        #tk.attributes("-fullscreen",True)
        self.master.geometry("{0}x{1}+0+0".format(self.master.winfo_screenwidth()-10, self.master.winfo_screenheight()-10))
        self.master.title("Attendance Management System")
        #self.master.configure(background = "red")

        #creating Side Nabvar
        style = ttk.Style()
        style.configure("BW.TLabel", foreground="white", background="black")
        style.configure("B.TButton", foreground="black", bg="black", activebackground="grey")
        style.configure('label.TLabel', font=('Trebuchet MS', 28), foreground="red", padding=2)

        self.toolbar = tk.Frame(self.master, bg="black")
        logo = tk.Button(self.toolbar, bg='#000000', fg='#ffffff', activebackground="black", activeforeground="white",
                         relief='flat', text='Attendance System')
        logo.pack(side="top", padx=15, pady=20)
        
        btext =  self.data["details"]["name"].capitalize() + "\n" + views.role_id.get(self.data["role_id"]).capitalize()
        b1 = tk.Button(self.toolbar, bg='#000000', fg='#ffffff', activebackground="black", activeforeground="white",
                       relief='flat', text = btext)
        b1.pack(side="top", padx=15, pady=20)

        b2 = tk.Button(self.toolbar, bg='#000000', fg='#ffffff', activebackground="black", activeforeground="white",
                       relief='flat', text='Lab &\nLectures',command = lambda:self.list_lec(data))
        b2.pack(side="top", padx=15, pady=20)
        b = tk.Button(self.toolbar, bg='#000000', fg='#ffffff', activebackground="black", activeforeground="white",
                       relief='flat', text='View\nAttendance',command = self._view_attendance_btn_clicked)
        b.pack(side="top", padx=15, pady=20)
        b3 = tk.Button(self.toolbar, bg='#000000', fg='#ffffff', activebackground="black", activeforeground="white",
                       relief='flat', text='Edit\nAttendance',command = self._edit_attendance_btn_clicked)
        b3.pack(side="top", padx=15, pady=20)
        b4 = tk.Button(self.toolbar, bg = "black", fg = "white",relief = "flat", font = ("Georgia", "12", "bold"), text='Mark\nAttendance',command = self.mark_attendance)
        b4.pack(side="top", padx=15, pady=20)

        b5 = tk.Button(self.toolbar, bg = "black", fg = "white",relief = "flat", font = ("Georgia", "12", "bold"), text='Log\nOut',
            command = self.log_out)
        b5.pack(side="top", padx=15, pady=20)
        self.toolbar.pack(side="left", fill="y")


        # Creating Frame
        self.frame = tk.Frame(self.master)

        # Label
        #ttk.Label(self.frame, text = "Welcome\n" + data['name'].capitalize() + "!",style = "label.TLabel").pack()
        ttk.Label(self.frame, text = "Welcome\n"+self.data["details"]["name"].capitalize()+"!", font = ("Georgia", 30, "bold"), 
                foreground = "red").pack(anchor = "center")

        # Creating page layout
        self.frame.pack()

    def _view_attendance_btn_clicked(self):
        """ Can view the attendance of the subjects taught by the teacher"""
        self.frame.destroy()
        self.frame = ttk.Frame(self.master)
        self.frame.pack()
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
                        command = lambda : self.show_attendance(data,self.class_list.get(),self.subject_list.get())).grid(row = 1, columnspan = 3, sticky = "e", pady = 10)
        
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

    def _enable_list(self, values):
        """ Enabling subject_list combobox """
        self.subject_list['state'] = "normal"
        self.subject_list['values'] = values

    def show_attendance(self, data, selected_class, subject):
        #print(data,selected_class,subject)
        """ Displays the attendance of the selected class """
        children = list(self.subject_attendance_frame.children.values())
        for child in children:
            child.destroy()
        # Style
        s = ttk.Style()
        s.configure("TLabelframe.Label", font = ("Georgia", 16, "bold"), foreground = "red")

        try:
            #data["sub_alot_id"] = 3
            att_details,student_details = views.get_attendance(data["sub_alot_id"], selected_class, subject, 0)
        except:
            tm.showerror("Error","No Attendance Marked on that Day..")
            return
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
            print(values)    
            self.tree.insert("", 'end', text = r, values = values, tag = tag)   


        #self.tree.insert("",'end',text="L",values=(1, "Harshita", "F", "phone_no",))
            
        #self.tree.bind("<Button-1>", self.click)
        self.tree.pack(padx = 10, pady = 10)

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

    def mark_attendance(self):
        self.frame.destroy()
        self.frame = ttk.Frame(self.master)
        self.frame.pack()

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

    def log_out(self):
        """
        children = list(self.subject_attendance_frame.children.values())
        for child in children:
            child.destroy()
        """
        self.frame.destroy()
        self.toolbar.destroy()
        import MainPage
        MainPage.MainPage(self.master)._login_btn_clicked()

"""
data = {
    'name' : 'Vignesh',
    'details': "{'name' : 'Vignesh', 'roll_no' : '3', 'dept_id' : '1', 'gender' : 'M'}",
    "u_id": 3,
    "class":"D1",
    "email_id":"Vignesh@gmail.com",
    "password":"Vignesh",
    'role_id' : 2,
    'u_id' : 3
}
master=tk.Tk()
Teacher(master,data)
master.mainloop()

var = '{\"14:28:28\" : [\'D1\', \'JPL\',[1,2,3,4,5,6,7,8,9]]}'
var1 = eval(var)
var2 = (list(var1.values())[0])
print(type(var2[2]))
"""