
import tkinter as tk
#!/usr/bin/env python3
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter.filedialog import askopenfilename, asksaveasfilename, askdirectory
from tkinter import filedialog
from tkinter import Tk, Frame, Button, BOTH, SUNKEN
from tkinter.colorchooser import askcolor
import os, sys, subprocess

import pyautogui as pag
import pyperclip as pc
import runpy
import glob
import time


from tkinter.scrolledtext import ScrolledText 

from NB1 import *
from NB2 import *
from NB3 import *

from codestrings import *

class LbTx(tk.Frame):
    def __init__(self, parent):
        super().__init__()
        self.path = os.getcwd()
        self.parent = parent
        self.notebook = ttk.Notebook(self.parent)
        self.notebook.grid(row=0, column=0)
        self.f1 = ttk.Frame(self.notebook, width=1900, height=1080)
        self.f1.grid(row=0, column=1)
       
        self.notebook.add(self.f1, text="TAB1")
        self.fram = tk.Frame(self.f1, width=100, height=20)
        self.fram.grid(row=0, column=0)
        self.e1= tk.Entry(self.f1, width=60, bd=8, bg= "seashell")
        self.e1.grid(row=0, column=1, columnspan = 3)
        self.e1.insert(tk.END, self.path)
        self.f2 = ttk.Frame(self.notebook)
        self.notebook.add(self.f2, text='2')
        self.txt2 = ScrolledText(self.f2, height=55, width=100)

        self.txt2.grid(row=0, column=1)
        self.txt2.grid_rowconfigure(0, weight=1)
        self.txt2.grid_columnconfigure(1, weight=1)
        self.txt2.insert("1.0", tk.END)

               
        self.fr_buttons = tk.Frame(self.f2, relief=tk.RAISED)
        self.btn_open = tk.Button(self.fr_buttons, text="Open", command=lambda:self.open_file(self.txt2))
        self.btn_open.grid(row=1, column=0)
        self.btn_save = tk.Button(self.fr_buttons, text="Save As...", command=lambda:self.save_file(self.txt2))
        self.btn_save.grid(row=2, column=0)
        self.btn_clear = tk.Button(self.fr_buttons, text="Clear", command=lambda:self.clear(self.txt2))
        self.btn_clear.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
        self.btn_grab = tk.Button(self.fr_buttons, text="Grab", command=lambda:self.ggtxt(self.txt2))
        self.btn_grab.grid(row=4, column=0)

        self.btn_grab2 = tk.Button(self.fr_buttons, text="Grab Tab", command=lambda:self.ggtxt(self.txt2))
        self.btn_grab2.grid(row=6, column=0)
        self.ftcolor2 = tk.Button(self.fr_buttons, text="change FGcolor", command=lambda:self.changeFg(self.txt2))
        self.ftcolor2.grid(row=8, column=0)
        self.btcolor2 = tk.Button(self.fr_buttons, text="change BGcolor", command=lambda:self.changeBg(self.txt2))
        self.btcolor2.grid(row=10, column=0)
        self.label1 = tk.Label(self.fr_buttons, text ='Find').grid(row=11, column=0)

        self.edit = tk.Entry(self.fr_buttons, width=15,bd=12,bg="wheat")
        self.edit.grid(row=12, column=0)
##        self.edit.focus_set()
        self.find1 = tk.Button(self.fr_buttons, text ='Find')
        self.find1.grid(row=13,column=0)
        self.label2 = tk.Label(self.fr_buttons, text = "Replace With ").grid(row=14, column=0)
 
        self.edit2 = tk.Entry(self.fr_buttons, width=15,bd=12, bg = "seashell")
        self.edit2.grid(row=15, column=0)
        self.edit2.focus_set()
         
        self.replace1 = tk.Button(self.fr_buttons, text = 'FindNReplace')
        self.replace1.grid(row=16, column=0)

        
        self.fr_buttons.grid(row=0, column=0, sticky="ns")
        self.find1.config(command = lambda : self.find(self.txt2, self.edit.get()))
        self.replace1.config(command = lambda : self.findNreplace(self.txt2, self.edit.get() ,self.edit2.get()))
        #################################################################Frame 3################################################################
        self.f3 = ttk.Frame(self.notebook)
        self.notebook.add(self.f3, text='3')
        self.txt3 = ScrolledText(self.f3, height=55, width=100)

        self.txt3.grid(row=0, column=1)
        self.txt3.grid_rowconfigure(0, weight=1)
        self.txt3.grid_columnconfigure(1, weight=1)
        self.txt3.insert("1.0", tk.END)
        self.fr_buttons = tk.Frame(self.f3, relief=tk.RAISED)
        self.btn_open = tk.Button(self.fr_buttons, text="Open", command=lambda:self.open_file(self.txt3))
        self.btn_open.grid(row=1, column=0)
        self.btn_save = tk.Button(self.fr_buttons, text="Save As...", command=lambda:self.save_file(self.txt3))
        self.btn_save.grid(row=2, column=0)
        self.btn_clear = tk.Button(self.fr_buttons, text="Clear", command=lambda:self.clear(self.txt3))
        self.btn_clear.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
        

        self.btn_grab2 = tk.Button(self.fr_buttons, text="Grab", command=lambda:self.ggtxt(self.txt3))
        self.btn_grab2.grid(row=6, column=0)
        self.ftcolor2 = tk.Button(self.fr_buttons, text="change FGcolor", command=lambda:self.changeFg(self.txt3))
        self.ftcolor2.grid(row=8, column=0)
        self.btcolor2 = tk.Button(self.fr_buttons, text="change BGcolor", command=lambda:self.changeBg(self.txt3))
        self.btcolor2.grid(row=10, column=0)
        self.fr_buttons.grid(row=0, column=0, sticky="ns")

        #################################################################################################################################################

        self.f4 = ttk.Frame(self.notebook)
        self.notebook.add(self.f4, text='4')
        self.txt4 = ScrolledText(self.f4, height=55, width=100)

        self.txt4.grid(row=0, column=1)
        self.txt4.grid_rowconfigure(0, weight=1)
        self.txt4.grid_columnconfigure(1, weight=1)
        self.txt4.insert("1.0", tk.END)
        self.fr_buttons = tk.Frame(self.f4, relief=tk.RAISED)
        self.btn_open = tk.Button(self.fr_buttons, text="Open", command=lambda:self.open_file(self.txt4))
        self.btn_open.grid(row=1, column=0)
        self.btn_save = tk.Button(self.fr_buttons, text="Save As...", command=lambda:self.save_file(self.txt4))
        self.btn_save.grid(row=2, column=0)
        self.btn_clear = tk.Button(self.fr_buttons, text="Clear", command=lambda:self.clear(self.txt4))
        self.btn_clear.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
        self.btn_grab = tk.Button(self.fr_buttons, text="Grab", command=lambda:self.ggtxt(self.txt4))
        self.btn_grab.grid(row=4, column=0)

        
        self.ftcolor2 = tk.Button(self.fr_buttons, text="change FGcolor", command=lambda:self.changeFg(self.txt4))
        self.ftcolor2.grid(row=8, column=0)
        self.btcolor2 = tk.Button(self.fr_buttons, text="change BGcolor", command=lambda:self.changeBg(self.txt4))
        self.btcolor2.grid(row=10, column=0)
        self.fr_buttons.grid(row=0, column=0, sticky="ns")

              ########################################################################################
        self.f5 = ttk.Frame(self.notebook)
        self.notebook.add(self.f5, text='5')
        self.txt5 = ScrolledText(self.f5, height=55, width=100)

        self.txt5.grid(row=0, column=1)
        self.txt5.grid_rowconfigure(0, weight=1)
        self.txt5.grid_columnconfigure(1, weight=1)
        self.txt5.insert("1.0", tk.END)

        self.fr_buttons = ttk.Frame(self.f5, relief=tk.RAISED)
        self.btn_open = tk.Button(self.fr_buttons, text="Open", command=lambda:self.open_file(self.txt5))
        self.btn_open.grid(row=1, column=0)
        self.btn_save = tk.Button(self.fr_buttons, text="Save As...", command=lambda:self.save_file(self.txt5))
        self.btn_save.grid(row=2, column=0)
        self.btn_clear = tk.Button(self.fr_buttons, text="Clear", command=lambda:self.clear(self.txt5))
        self.btn_clear.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
        self.btn_grab = tk.Button(self.fr_buttons, text="Grab", command=lambda:self.ggtxt(self.txt5))
        self.btn_grab.grid(row=4, column=0)

       
        self.ftcolor5 = tk.Button(self.fr_buttons, text="change FGcolor", command=lambda:self.changeFg(self.txt5))
        self.ftcolor5.grid(row=8, column=0)
        self.btcolor5 = tk.Button(self.fr_buttons, text="change BGcolor", command=lambda:self.changeBg(self.txt5))
        self.btcolor5.grid(row=10, column=0)
        self.fr_buttons.grid(row=0, column=0, sticky="ns")




        ########################################################################################





        f6 = ttk.Frame(self.notebook)
        self.notebook.add(f6, text='6')
        self.txt6 = ScrolledText(f6, height=66, width=100)

        self.txt6.grid(row=0, column=1)
        self.txt6.grid_rowconfigure(0, weight=1)
        self.txt6.grid_columnconfigure(1, weight=1)
        self.txt6.insert("1.0", tk.END)

       


        self.fr_buttons = ttk.Frame(f6, relief=tk.RAISED)
        self.btn_open = tk.Button(self.fr_buttons, text="Open", command=lambda:self.open_file(self.txt6))
        self.btn_open.grid(row=1, column=0)
        self.btn_save = tk.Button(self.fr_buttons, text="Save As...", command=lambda:self.save_file(self.txt6))
        self.btn_save.grid(row=2, column=0)
        self.btn_clear = tk.Button(self.fr_buttons, text="Clear", command=lambda:self.clear(self.txt6))
        self.btn_clear.grid(row=3, column=0, sticky="ew", padx=6, pady=6)
        self.btn_grab = tk.Button(self.fr_buttons, text="Grab", command=lambda:self.ggtxt(self.txt6))
        self.btn_grab.grid(row=4, column=0)
        self.ftcolor6 = tk.Button(self.fr_buttons, text="change FGcolor")
        self.ftcolor6.grid(row=8, column=0)
        self.btcolor6 = tk.Button(self.fr_buttons, text="change BGcolor", command=lambda:self.changeBg(self.txt6))
        self.btcolor6.grid(row=10, column=0)
        self.fr_buttons.grid(row=0, column=0, sticky="ns")



        ########################################################################################





        f7 = ttk.Frame(self.notebook)
        self.notebook.add(f7, text='7')
        self.txt7 = ScrolledText(f7, height=77, width=100)

        self.txt7.grid(row=0, column=1)
        self.txt7.grid_rowconfigure(0, weight=1)
        self.txt7.grid_columnconfigure(1, weight=1)
        self.txt7.insert("1.0", tk.END)
        self.fr_buttons = ttk.Frame(f7, relief=tk.RAISED)
        self.btn_open = tk.Button(self.fr_buttons, text="Open", command=lambda:self.open_file(self.txt7))
        self.btn_open.grid(row=1, column=0)
        self.btn_save = tk.Button(self.fr_buttons, text="Save As...", command=lambda:self.save_file(self.txt7))
        self.btn_save.grid(row=2, column=0)
        self.btn_clear = tk.Button(self.fr_buttons, text="Clear", command=lambda:self.clear(self.txt7))
        self.btn_clear.grid(row=3, column=0, sticky="ew", padx=6, pady=6)
        self.btn_grab = tk.Button(self.fr_buttons, text="Grab", command=lambda:self.ggtxt(self.txt7))
        self.btn_grab.grid(row=4, column=0)

       
        self.ftcolor = tk.Button(self.fr_buttons, text="change FGcolor")
        self.ftcolor.grid(row=8, column=0)
        self.btcolor = tk.Button(self.fr_buttons, text="change BGcolor", command=lambda:self.changeBg(self.txt7))
        self.btcolor.grid(row=10, column=0)
        self.fr_buttons.grid(row=0, column=0, sticky="ns")



        ########################################################################################



        f8 = ttk.Frame(self.notebook)
        self.notebook.add(f8, text='8')
        self.txt8 = ScrolledText(f8, height=88, width=100)

        self.txt8.grid(row=0, column=1)
        self.txt8.grid_rowconfigure(0, weight=1)
        self.txt8.grid_columnconfigure(1, weight=1)
        self.txt8.insert("1.0", tk.END)
        self.fr_buttons = ttk.Frame(f8, relief=tk.RAISED)
        self.btn_open = tk.Button(self.fr_buttons, text="Open", command=lambda:self.open_file(self.txt8))
        self.btn_open.grid(row=1, column=0)
        self.btn_save = tk.Button(self.fr_buttons, text="Save As...", command=lambda:self.save_file(self.txt8))
        self.btn_save.grid(row=2, column=0)
        self.btn_clear = tk.Button(self.fr_buttons, text="Clear", command=lambda:self.clear(self.txt8))
        self.btn_clear.grid(row=3, column=0, sticky="ew", padx=6, pady=6)
        self.btn_grab = tk.Button(self.fr_buttons, text="Grab", command=lambda:self.ggtxt(self.txt8))
        self.btn_grab.grid(row=4, column=0)

       
        self.ftcolor = tk.Button(self.fr_buttons, text="change FGcolor")
        self.ftcolor.grid(row=8, column=0)
        self.btcolor = tk.Button(self.fr_buttons, text="change BGcolor", command=lambda:self.changeBg(self.txt8))
        self.btcolor.grid(row=10, column=0)
        self.fr_buttons.grid(row=0, column=0, sticky="ns")


  


        ########################################################################################
        f9 = ttk.Frame(self.notebook)
        self.notebook.add(f9, text='9')
        self.txt9 = ScrolledText(f9, height=99, width=100)

        self.txt9.grid(row=0, column=1)
        self.txt9.grid_rowconfigure(0, weight=1)
        self.txt9.grid_columnconfigure(1, weight=1)
        self.txt9.insert("1.0", tk.END)
        self.fr_buttons = ttk.Frame(f9, relief=tk.RAISED)
        self.btn_open = tk.Button(self.fr_buttons, text="Open", command=lambda:self.open_file(self.txt9))
        self.btn_open.grid(row=1, column=0)
        self.btn_save = tk.Button(self.fr_buttons, text="Save As...", command=lambda:self.save_file(self.txt9))
        self.btn_save.grid(row=2, column=0)
        self.btn_clear = tk.Button(self.fr_buttons, text="Clear", command=lambda:self.clear(self.txt9))
        self.btn_clear.grid(row=3, column=0, sticky="ew", padx=6, pady=6)
        self.btn_grab = tk.Button(self.fr_buttons, text="Grab", command=lambda:self.ggtxt(self.txt9))
        self.btn_grab.grid(row=4, column=0)

       
        self.ftcolor = tk.Button(self.fr_buttons, text="change FGcolor")
        self.ftcolor.grid(row=8, column=0)
        self.btcolor = tk.Button(self.fr_buttons, text="change BGcolor", command=lambda:self.changeBg(self.txt9))
        self.btcolor.grid(row=10, column=0)
        self.fr_buttons.grid(row=0, column=0, sticky="ns")


    
            
        ########################################################################################




        f10 = ttk.Frame(self.notebook)
        self.notebook.add(f10, text='10')
        self.txt10 = ScrolledText(f10, height=1010, width=100)

        self.txt10.grid(row=0, column=1)
        self.txt10.grid_rowconfigure(0, weight=1)
        self.txt10.grid_columnconfigure(1, weight=1)
        self.txt10.insert("1.0", tk.END)
        self.fr_buttons = ttk.Frame(f10, relief=tk.RAISED)
        self.btn_open = tk.Button(self.fr_buttons, text="Open", command=lambda:self.open_file(self.txt10))
        self.btn_open.grid(row=1, column=0)
        self.btn_save = tk.Button(self.fr_buttons, text="Save As...", command=lambda:self.save_file(self.txt10))
        self.btn_save.grid(row=2, column=0)
        self.btn_clear = tk.Button(self.fr_buttons, text="Clear", command=lambda:self.clear(self.txt10))
        self.btn_clear.grid(row=3, column=0, sticky="ew", padx=6, pady=6)
        self.btn_grab = tk.Button(self.fr_buttons, text="Grab", command=lambda:self.ggtxt(self.txt10))
        self.btn_grab.grid(row=4, column=0)

       
        self.ftcolor = tk.Button(self.fr_buttons, text="change FGcolor")
        self.ftcolor.grid(row=8, column=0)
        self.btcolor = tk.Button(self.fr_buttons, text="change BGcolor", command=lambda:self.changeBg(self.txt10))
        self.btcolor.grid(row=10, column=0)
        self.fr_buttons.grid(row=0, column=0, sticky="ns")

 

        ########################################################################################
        f11 = ttk.Frame(self.notebook)
        self.notebook.add(f11, text='11')
        self.txt11 = ScrolledText(f11, height=1111, width=110)

        self.txt11.grid(row=0, column=1)
        self.txt11.grid_rowconfigure(0, weight=1)
        self.txt11.grid_columnconfigure(1, weight=1)
        self.txt11.insert("1.0", n5)
        self.fr_buttons = ttk.Frame(f11, relief=tk.RAISED)
        self.btn_open = tk.Button(self.fr_buttons, text="Open", command=lambda:self.open_file(self.txt11))
        self.btn_open.grid(row=1, column=0)
        self.btn_save = tk.Button(self.fr_buttons, text="Save As...", command=lambda:self.save_file(self.txt11))
        self.btn_save.grid(row=2, column=0)
        self.btn_clear = tk.Button(self.fr_buttons, text="Clear", command=lambda:self.clear(self.txt11))
        self.btn_clear.grid(row=3, column=0, sticky="ew", padx=6, pady=6)
        self.btn_grab = tk.Button(self.fr_buttons, text="Grab", command=lambda:self.ggtxt(self.txt11))
        self.btn_grab.grid(row=4, column=0)

       
        self.ftcolor = tk.Button(self.fr_buttons, text="change FGcolor", command=lambda:self.changeFg(self.txt11))
        self.ftcolor.grid(row=8, column=0)
        self.btcolor = tk.Button(self.fr_buttons, text="change BGcolor", command=lambda:self.changeBg(self.txt11))
        self.btcolor.grid(row=10, column=0)
        self.fr_buttons.grid(row=0, column=0, sticky="ns")

       


        ########################################################################################


        f12 = ttk.Frame(self.notebook)
        self.notebook.add(f12, text='12')
        self.txt12 = ScrolledText(f12, height=1212, width=120)

        self.txt12.grid(row=0, column=1)
        self.txt12.grid_rowconfigure(0, weight=1)
        self.txt12.grid_columnconfigure(1, weight=1)
        self.txt12.insert("1.0", n6)
        self.fr_buttons = ttk.Frame(f12, relief=tk.RAISED)
        self.btn_open = tk.Button(self.fr_buttons, text="Open", command=lambda:self.open_file(self.txt12))
        self.btn_open.grid(row=1, column=0)
        self.btn_save = tk.Button(self.fr_buttons, text="Save As...", command=lambda:self.save_file(self.txt12))
        self.btn_save.grid(row=2, column=0)
        self.btn_clear = tk.Button(self.fr_buttons, text="Clear", command=lambda:self.clear(self.txt12))
        self.btn_clear.grid(row=3, column=0, sticky="ew", padx=6, pady=6)
        self.btn_grab = tk.Button(self.fr_buttons, text="Grab", command=lambda:self.ggtxt(self.txt12))
        self.btn_grab.grid(row=4, column=0)

       
        self.ftcolor = tk.Button(self.fr_buttons, text="change FGcolor", command=lambda:self.changeFg(self.txt12))
        self.ftcolor.grid(row=8, column=0)
        self.btcolor = tk.Button(self.fr_buttons, text="change BGcolor", command=lambda:self.changeBg(self.txt12))
        self.btcolor.grid(row=10, column=0)
        self.fr_buttons.grid(row=0, column=0, sticky="ns")
        

      


        ########################################################################################

        f13 = ttk.Frame(self.notebook)
        self.notebook.add(f13, text='13')
        self.txt13 = ScrolledText(f13, height=1212, width=120)

        self.txt13.grid(row=0, column=1)
        self.txt13.grid_rowconfigure(0, weight=1)
        self.txt13.grid_columnconfigure(1, weight=1)
        self.txt13.insert("1.0", tk.END)
        self.fr_buttons = ttk.Frame(f13, relief=tk.RAISED)
        self.btn_open = tk.Button(self.fr_buttons, text="Open", command=lambda:self.open_file(self.txt13))
        self.btn_open.grid(row=1, column=0)
        self.btn_save = tk.Button(self.fr_buttons, text="Save As...", command=lambda:self.save_file(self.txt13))
        self.btn_save.grid(row=2, column=0)
        self.btn_clear = tk.Button(self.fr_buttons, text="Clear", command=lambda:self.clear(self.txt13))
        self.btn_clear.grid(row=3, column=0, sticky="ew", padx=6, pady=6)
        self.btn_grab = tk.Button(self.fr_buttons, text="Grab", command=lambda:self.ggtxt(self.txt13))
        self.btn_grab.grid(row=4, column=0)

       
        self.ftcolor = tk.Button(self.fr_buttons, text="change FGcolor", command=lambda:self.changeFg(self.txt13))
        self.ftcolor.grid(row=8, column=0)
        self.btcolor = tk.Button(self.fr_buttons, text="change BGcolor", command=lambda:self.changeBg(self.txt13))
        self.btcolor.grid(row=10, column=0)
        self.fr_buttons.grid(row=0, column=0, sticky="ns")






        

        f14 = ttk.Frame(self.notebook)
        self.notebook.add(f14, text='14')
        self.txt14 = ScrolledText(f14, height=1212, width=120)

        self.txt14.grid(row=0, column=1)
        self.txt14.grid_rowconfigure(0, weight=1)
        self.txt14.grid_columnconfigure(1, weight=1)
        self.txt14.insert("1.0", n10)
        self.fr_buttons = ttk.Frame(f14, relief=tk.RAISED)
        self.btn_open = tk.Button(self.fr_buttons, text="Open", command=lambda:self.open_file(self.txt14))
        self.btn_open.grid(row=1, column=0)
        self.btn_save = tk.Button(self.fr_buttons, text="Save As...", command=lambda:self.save_file(self.txt14))
        self.btn_save.grid(row=2, column=0)
        self.btn_clear = tk.Button(self.fr_buttons, text="Clear", command=lambda:self.clear(self.txt14))
        self.btn_clear.grid(row=3, column=0, sticky="ew", padx=6, pady=6)
        self.btn_grab = tk.Button(self.fr_buttons, text="Grab", command=lambda:self.ggtxt(self.txt14))
        self.btn_grab.grid(row=4, column=0)

       
        self.ftcolor = tk.Button(self.fr_buttons, text="change FGcolor", command=lambda:self.changeFg(self.txe14))
        self.ftcolor.grid(row=8, column=0)
        self.btcolor = tk.Button(self.fr_buttons, text="change BGcolor", command=lambda:self.changeBg(self.txt14))
        self.btcolor.grid(row=10, column=0)
        self.fr_buttons.grid(row=0, column=0, sticky="ns")
        
        

        f15 = ttk.Frame(self.notebook)
        self.notebook.add(f15, text='15')
        self.txt15 = ScrolledText(f15, height=1212, width=120)

        self.txt15.grid(row=0, column=1)
        self.txt15.grid_rowconfigure(0, weight=1)
        self.txt15.grid_columnconfigure(1, weight=1)
        self.txt15.insert("1.0", tk.END)
        self.fr_buttons = ttk.Frame(f15,relief=tk.RAISED)
        self.btn_open = tk.Button(self.fr_buttons, text="Open", command=lambda:self.open_file(self.txt15))
        self.btn_open.grid(row=1, column=0)
        self.btn_save = tk.Button(self.fr_buttons, text="Save As...", command=lambda:self.save_file(self.txt15))
        self.btn_save.grid(row=2, column=0)
        self.btn_clear = tk.Button(self.fr_buttons, text="Clear", command=lambda:self.clear(self.txt15))
        self.btn_clear.grid(row=3, column=0, sticky="ew", padx=6, pady=6)
        self.btn_grab = tk.Button(self.fr_buttons, text="Grab", command=lambda:self.ggtxt(self.txt15))
        self.btn_grab.grid(row=4, column=0)

       
        self.ftcolor = tk.Button(self.fr_buttons, text="change FGcolor" ,command=lambda:self.changeFg(self.txt15))
        self.ftcolor.grid(row=8, column=0)
        self.btcolor = tk.Button(self.fr_buttons, text="change BGcolor", command=lambda:self.changeBg(self.txt15))
        self.btcolor.grid(row=10, column=0)
        self.fr_buttons.grid(row=0, column=0, sticky="ns")
        

      

      

         

        f16 = ttk.Frame(self.notebook)
        self.notebook.add(f16, text='16')
        self.txt16 = ScrolledText(f16, height=1212, width=120)

        self.txt16.grid(row=0, column=1)
        self.txt16.grid_rowconfigure(0, weight=1)
        self.txt16.grid_columnconfigure(1, weight=1)
        self.txt16.insert("1.0", tk.END)
        self.fr_buttons = ttk.Frame(f16, relief=tk.RAISED)
        self.btn_open = tk.Button(self.fr_buttons, text="Open", command=lambda:self.open_file(self.txt16))
        self.btn_open.grid(row=1, column=0)
        self.btn_save = tk.Button(self.fr_buttons, text="Save As...", command=lambda:self.save_file(self.txt16))
        self.btn_save.grid(row=2, column=0)
        self.btn_clear = tk.Button(self.fr_buttons, text="Clear", command=lambda:self.clear(self.txt16))
        self.btn_clear.grid(row=3, column=0, sticky="ew", padx=6, pady=6)
        self.btn_grab = tk.Button(self.fr_buttons, text="Grab", command=lambda:self.ggtxt(self.txt16))
        self.btn_grab.grid(row=4, column=0)

       
        self.ftcolor = tk.Button(self.fr_buttons, text="change FGcolor" ,command=lambda:self.changeFg(self.txt16))
        self.ftcolor.grid(row=8, column=0)
        self.btcolor = tk.Button(self.fr_buttons, text="change BGcolor", command=lambda:self.changeBg(self.txt16))
        self.btcolor.grid(row=10, column=0)
        self.fr_buttons.grid(row=0, column=0, sticky="ns")
        

      

        

        f17 = ttk.Frame(self.notebook)
        self.notebook.add(f17, text='17')
        self.txt17 = ScrolledText(f17, height=1212, width=120)

        self.txt17.grid(row=0, column=1)
        self.txt17.grid_rowconfigure(0, weight=1)
        self.txt17.grid_columnconfigure(1, weight=1)
        self.txt17.insert("1.0", tk.END)
        self.fr_buttons = ttk.Frame(f12, relief=tk.RAISED)
        self.btn_open = tk.Button(self.fr_buttons, text="Open", command=lambda:self.open_file(self.txt17))
        self.btn_open.grid(row=1, column=0)
        self.btn_save = tk.Button(self.fr_buttons, text="Save As...", command=lambda:self.save_file(self.txt17))
        self.btn_save.grid(row=2, column=0)
        self.btn_clear = tk.Button(self.fr_buttons, text="Clear", command=lambda:self.clear(self.txt17))
        self.btn_clear.grid(row=3, column=0, sticky="ew", padx=6, pady=6)
        self.btn_grab = tk.Button(self.fr_buttons, text="Grab", command=lambda:self.ggtxt(self.txt17))
        self.btn_grab.grid(row=4, column=0)

       
        self.ftcolor = tk.Button(self.fr_buttons, text="change FGcolor", command=lambda:self.changeFg(self.tx17))
        self.ftcolor.grid(row=8, column=0)
        self.btcolor = tk.Button(self.fr_buttons, text="change BGcolor", command=lambda:self.changeBg(self.txt17))
        self.btcolor.grid(row=10, column=0)
        self.fr_buttons.grid(row=0, column=0, sticky="ns")
        

      


        

        f18 = ttk.Frame(self.notebook)
        self.notebook.add(f18, text='18')
        self.txt18 = ScrolledText(f18, height=1212, width=120)

        self.txt18.grid(row=0, column=1)
        self.txt18.grid_rowconfigure(0, weight=1)
        self.txt18.grid_columnconfigure(1, weight=1)
        self.txt18.insert("1.0", tk.END)
        self.fr_buttons = ttk.Frame(f18, relief=tk.RAISED)
        self.btn_open = tk.Button(self.fr_buttons, text="Open", command=lambda:self.open_file(self.txt18))
        self.btn_open.grid(row=1, column=0)
        self.btn_save = tk.Button(self.fr_buttons, text="Save As...", command=lambda:self.save_file(self.txt18))
        self.btn_save.grid(row=2, column=0)
        self.btn_clear = tk.Button(self.fr_buttons, text="Clear", command=lambda:self.clear(self.txt18))
        self.btn_clear.grid(row=3, column=0, sticky="ew", padx=6, pady=6)
        self.btn_grab = tk.Button(self.fr_buttons, text="Grab", command=lambda:self.ggtxt(self.txt18))
        self.btn_grab.grid(row=4, column=0)

       
        self.ftcolor = tk.Button(self.fr_buttons, text="change FGcolor",command=lambda:self.changeFg(self.txt18))
        self.ftcolor.grid(row=8, column=0)
        self.btcolor = tk.Button(self.fr_buttons, text="change BGcolor", command=lambda:self.changeBg(self.txt18))
        self.btcolor.grid(row=10, column=0)
        self.fr_buttons.grid(row=0, column=0, sticky="ns")



        f19 = ttk.Frame(self.notebook)
        self.notebook.add(f19, text='19')
        self.txt19 = ScrolledText(f19, height=1212, width=120)

        self.txt19.grid(row=0, column=1)
        self.txt19.grid_rowconfigure(0, weight=1)
        self.txt19.grid_columnconfigure(1, weight=1)
        self.txt19.insert("1.0", n7)
        self.fr_buttons = ttk.Frame(f19, relief=tk.RAISED)
        self.btn_open = tk.Button(self.fr_buttons, text="Open", command=lambda:self.open_file(self.txt19))
        self.btn_open.grid(row=1, column=0)
        self.btn_save = tk.Button(self.fr_buttons, text="Save As...", command=lambda:self.save_file(self.txt19))
        self.btn_save.grid(row=2, column=0)
        self.btn_clear = tk.Button(self.fr_buttons, text="Clear", command=lambda:self.clear(self.txt19))
        self.btn_clear.grid(row=3, column=0, sticky="ew", padx=6, pady=6)
        self.btn_grab = tk.Button(self.fr_buttons, text="Grab", command=lambda:self.ggtxt(self.txt19))
        self.btn_grab.grid(row=4, column=0)

       
        self.ftcolor = tk.Button(self.fr_buttons, text="change FGcolor",command=lambda:self.changeFg(self.txt19))
        self.ftcolor.grid(row=8, column=0)
        self.btcolor = tk.Button(self.fr_buttons, text="change BGcolor", command=lambda:self.changeBg(self.txt19))
        self.btcolor.grid(row=10, column=0)
        self.fr_buttons.grid(row=0, column=0, sticky="ns")
        

      

        f20 = ttk.Frame(self.notebook)
        self.notebook.add(f20, text='20')
        self.txt20 = ScrolledText(f20, height=1212, width=120)

        self.txt20.grid(row=0, column=1)
        self.txt20.grid_rowconfigure(0, weight=1)
        self.txt20.grid_columnconfigure(1, weight=1)
        self.txt20.insert("1.0", tk.END)
        self.fr_buttons = ttk.Frame(f20, relief=tk.RAISED)
        self.btn_open = tk.Button(self.fr_buttons, text="Open", command=lambda:self.open_file(self.txt20))
        self.btn_open.grid(row=1, column=0)
        self.btn_save = tk.Button(self.fr_buttons, text="Save As...", command=lambda:self.save_file(self.txt20))
        self.btn_save.grid(row=2, column=0)
        self.btn_clear = tk.Button(self.fr_buttons, text="Clear", command=lambda:self.clear(self.txt20))
        self.btn_clear.grid(row=3, column=0, sticky="ew", padx=6, pady=6)
        self.btn_grab = tk.Button(self.fr_buttons, text="Grab", command=lambda:self.ggtxt(self.txt20))
        self.btn_grab.grid(row=4, column=0)

       
        self.ftcolor = tk.Button(self.fr_buttons, text="change FGcolor",command=lambda:self.changeFg(self.txt20))
        self.ftcolor.grid(row=8, column=0)
        self.btcolor = tk.Button(self.fr_buttons, text="change BGcolor", command=lambda:self.changeBg(self.txt20))
        self.btcolor.grid(row=10, column=0)
        self.fr_buttons.grid(row=0, column=0, sticky="ns")
      
        self.fr_buttons.grid(row=0, column=0, sticky="ns")
        
        f21 = ttk.Frame(self.notebook)
        self.notebook.add(f21, text='201')
        self.nb1= NB1(f21)

        f22 = ttk.Frame(self.notebook)
        self.notebook.add(f22, text='212')
        self.nb1= NB1(f22)

        f23 = ttk.Frame(self.notebook)
        self.notebook.add(f23, text='220')
        self.nb1= NB2(f23)

        f24 = ttk.Frame(self.notebook)
        self.notebook.add(f24, text='240')
        self.nb1= NB3(f24)

        self.lb = tk.Listbox(self.f1, bg='cyan2',bd=12, width=35, height=55, exportselection=False, selectmode=tk.SINGLE)
        self.lb.grid(row=1, column=2)
        self.lb.focus()
        self.lb.configure(selectmode="")
        self.lb.bind("<Double-Button-1>", self.listing)
        self.lb.bind("<<ListboxSelect>>", self.showcontent)
        self.lb.bind("<Double-Button-2>", lambda event : self.run(self.path))
        self.lb.bind('<<ListboxSelect>>', lambda event: self.listing(event))
        self.curtxt = None
        self.x = self.lb.curselection()
        self.tx = ScrolledText(self.f1,
                      bg='white',
                      bd=12,
                      relief=GROOVE,
                      height=50,
                      width=100,
                      font='TkFixedFont',)
        self.tx.grid(row = 1, column=5)
        
        self.flist2 = []
        self.flist = os.listdir(self.path)
        self.lb.insert(tk.END, self.flist)
        for self.item in self.flist:
            if self.item.endswith(".py"):
                self.flist2.append(self.item)

                self.lb.insert(tk.END, self.item)
         
                self.lb.focus()
              
      
        self.side_frame_btns()

    def listing(self,event=None):
        x = event.widget
        try:
            x = int(self.lb.curselection()[0])
            file = self.lb.get(x)
        except IndexError:
         
            v=(self.lb.get(x))
            v =  self.lb.curselection()[0]
            file = self.lb.get(v)
           
        with open(file, "r") as file:
            content = file.read()
            self.tx.delete("1.0", tk.END)
            self.tx.insert(tk.END, content)
            self.curtxt = content
            return self.curtxt


    def showcontent(self,x, event=None):
        for i in self.lb.curselection():
            file = self.lb.get(i)
            with open(file, "r") as file:
                file = file.read()
                self.tx.delete("1.0", tk.END)
                self.tx.insert(tk.END, file)

            return





    def run(self, path, event=None,):
        self.path = path
        self.file = self.lb.get(ANCHOR)
        filetorun = self.path + '/' + self.file
        runpy.run_path(filetorun)
        return
    def open(self):
        '''Open a file for editing.'''
        self.filepath = askopenfilename(
            filetypes=[('All Files', '*.*')]
        )
        if not self.filepath:
            return
        self.tx.delete(1.0, tk.END)
        with open(self.filepath, 'r') as input_file:
            text = input_file.read()
            self.tx.insert(tk.END, text)


    def save(self):
        '''Save the current file as a new file.'''
        self.filepath = asksaveasfilename(
        defaultextension='txt',
        filetypes=[('All Files', '*.*')],)
        for file in self.filepath:
            if not file_(self.path):
                return
        with open(self.filepath, 'w') as output_file:
            text = self.tx.get(1.0, tk.END)
            output_file.write(text)
      

    def newdirlist(self):
      
        self.e1.delete(0, END)
        self.path = askdirectory()
        os.chdir(self.path)
        self.flist = os.listdir(self.path)
        self.lb.delete(0, tk.END)
        self.e1.insert(END, self.path)
        for self.item in self.flist:

            self.lb.insert(tk.END, self.item)
            
        return self.flist, self.path

    def clear(self, textwidget):
        self.textwidget = textwidget
        self.textwidget.delete("1.0", tk.END)
    def cleare1(self):
        self.e1.delete(0, END)
    def side_frame_btns(self):

        self.fr_btn = tk.Frame(self.fram, relief=tk.RAISED, bd=12)
        self.fr_btn.grid(row=2, column=0, sticky='ns')
        btn_open = tk.Button(self.fr_btn, text='Open', bd=8, command= lambda:self.open())
        btn_save = tk.Button(self.fr_btn, text='Save As...',bd=8, command= lambda:self.save())
        btn14 = tk.Button(self.fr_btn, text="get dir", bd=8, command=lambda : self.newdirlist())
       
        btn_open.grid(row=3, column=0)
        btn_save.grid(row=4, column=0)
       
        btn14.grid(row=5, column=0)
        btn15 = tk.Button(self.fr_btn, text='Run', bd=8, command= lambda : self.run(self.path))
        btn15.grid(row=6,column=0)
        btn16 = tk.Button(self.fr_btn, text='clear path display', bd=8, command= lambda : self.cleare1())
        btn16.grid(row=7,column=0)

    def binding(self):
        self.lb.bind("<Double-Button-1>", self.listing)
        self.lb.bind("<<ListboxSelect>>", lambda event : self.showcontent(event))
        self.lb.bind("<Double-Button-2>", lambda event : self.run(event))
  
    def changeBg(self,textwidget):
        (triple, hexstr) = askcolor()
        if hexstr:
            textwidget.config(bg=hexstr)


    def changeFg(self,textwidget):
        (triple, hexstr) = askcolor()
        if hexstr:
            textwidget.config(fg=hexstr)


    def command(self):
        pass


    def open_file(self,textwidget):
        '''Open a file for editing.'''
        filepath = askopenfilename(
            filetypes=[('All Files', '*.*')]
        )
        if not filepath:
            return
        textwidget.delete(1.0, tk.END)
        with open(filepath, 'r') as input_file:
            text = input_file.read()
            textwidget.insert(tk.END, text)
       
    def save_file(self,textwidget):
        '''Save the current file as a new file.'''
        filepath = asksaveasfilename(
            defaultextension='py',
            filetypes=[('All Files', '*.*')],
        )
        if not filepath:
            return
        with open(filepath, 'w') as output_file:
            text = textwidget.get(1.0, tk.END)
            output_file.write(text)

    def fname1(self):
        filepath1 = askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if not filepath:
            return
        text3.delete("1.0", tk.END)
        with open(filepath, "r") as input_file:
            text2 = input_file.readlines()
            text2.insert(tk.END, text)
            return filepath2



    def fname2(self):
        filepath2 = askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if not filepath:
            return
        text.delete("1.0", tk.END)
        with open(filepath, "r") as input_file:
            text2 = input_file.readlines()
            text2.insert(tk.END, text)
            return filepath2


    def ggtxt(self, textwidget):
        gettxt = self.tx.get("1.0", tk.END)
        textwidget.insert(tk.END, gettxt)

   


       
    def edit2(self, name):
        runpy.run_path(path_name="name")
    def find(self, textwidget,entrywidget):
     
    # remove tag 'found' from index 1 to END
        textwidget.tag_remove('found', '1.0', END)
        self.entry = entrywidget
  
     
        if (self.entry):
            idx = '1.0'
            while 1:
                # searches for desired string from index 1
                idx = textwidget.search(self.entry, idx, nocase = 1,
                                stopindex = END)
                 
                if not idx: break
                 
                # last index sum of current index and
                # length of text
                lastidx = '% s+% dc' % (idx, len(self.entry))
                 
     
                # overwrite 'Found' at idx
                textwidget.tag_add('found', idx, lastidx)
                idx = lastidx
 
        # mark located string as red
         
        textwidget.tag_config('found', foreground ='blue')
       


    

    def findNreplace(self,textwidget,entry1,entry2):
         
        # remove tag 'found' from index 1 to END
        textwidget.tag_remove('found', '1.0', END)
         
        # returns to widget currently in focus
        self.fin = entry1
        self.repl = entry2
         
        if (self.fin and self.repl):
            idx = '1.0'
            while 1:
                # searches for desired string from index 1
                idx = textwidget.search(self.fin, idx, nocase = 1,
                                stopindex = END)
                print(idx)
                if not idx: break
                 
                # last index sum of current index and
                # length of text
                lastidx = '% s+% dc' % (idx, len(self.fin))
     
                textwidget.delete(idx, lastidx)
                textwidget.insert(idx, self.repl)
     
                lastidx = '% s+% dc' % (idx, len(self.repl))
                 
                # overwrite 'Found' at idx
                textwidget.tag_add('found', idx, lastidx)
                idx = lastidx
     
            # mark located string as red
            textwidget.tag_config('found', foreground ='green', background = 'yellow')
            
                     
   
      
def main():
    parent = tk.Tk()
    app=LbTx(parent)
    parent.mainloop()


if __name__== '__main__':
    main()
