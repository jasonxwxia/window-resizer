from tkinter import *
from tkinter.ttk import *
import subprocess


class app(Tk):
	def __init__(self):
		super().__init__()
		self.geometry("700x400")
		self.configure(bg="white")
		frm = Frame(self, padding=10)
		frm.grid(column=0, row=0, sticky=(N,W,E,S))
		
	

App = app()
App.mainloop()
