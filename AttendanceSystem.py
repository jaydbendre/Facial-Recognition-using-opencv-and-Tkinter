import MainPage as mp
import tkinter as tk
import tkinter.ttk as ttk

# Creating object and displaying the window
def call_main_window():
    master = tk.Tk()
    
    style = ttk.Style()
    style.element_create("Custom.Treeheading.border", "from", "default")
    style.layout("Custom.Treeview.Heading", [
                ("Custom.Treeheading.cell", {'sticky': 'nswe'}),
                ("Custom.Treeheading.border", {'sticky':'nswe', 'children': [
                    ("Custom.Treeheading.padding", {'sticky':'nswe', 'children': [
                        ("Custom.Treeheading.image", {'side':'right', 'sticky':''}),
                        ("Custom.Treeheading.text", {'sticky':'we'})
                    ]})
                ]}),
            ])
    style.configure("Custom.Treeview.Heading", foreground = "white", background = "black", font = ("Georgia",12))
    style.configure("Custom.Treeview", rowheight = 30)
    
    """
        These are tags for odd and even rows.
        Put these lines where the treeview widget is used.
        And at the time of inserting the values, specify the tag name
        self.tree.tag_configure("evenrow", foreground = "black", background = "#FFFACD", font = ('Georgia',8))
        self.tree.tag_configure("oddrow", foreground = "white", background = "#FF0000", font = ('Georgia',8))
    """    
    mp.MainPage(master)
    master.mainloop()

call_main_window()