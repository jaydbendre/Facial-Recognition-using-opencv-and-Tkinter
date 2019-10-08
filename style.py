import tkinter as tk
from tkinter import ttk

# Defining styles
def style():
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
    style.configure("Custom.Treeview.Heading", foreground = "white", background = "black", font = ("Georgia",8))
    #style.element_create("X.TLabel","from","default")
    style.configure("X.TLabel", font = ("Comic Snas MS", 26, "bold"), foreground = "purple")