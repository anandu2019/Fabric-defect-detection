# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 16:06:57 2020

@author: LENOVO
"""
import tkinter as tk
import os

class App:
    def __init__(self, master):
        master.geometry("300x200")
        fm = Frame(master)
        Button(fm, text='Top').pack(side=TOP, expand=YES)
        Button(fm, text='Center').pack(side=TOP, expand=YES)
        Button(fm, text='Bottom').pack(side=TOP, expand=YES)
        fm.pack(fill=BOTH, expand=YES)

        
root = tk.Tk()
root.option_add('*font', ('verdana', 12, 'bold'))
root.title("Pack - Example 6a")
display = App(root)
root.mainloop()