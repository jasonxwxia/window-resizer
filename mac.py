# TODO: Add functionality for Linux and Windows, Have Processes constantly updating every time a new visible process starts

from tkinter import *
from tkinter.ttk import *
import subprocess
import platform


class app(Tk):
	def __init__(self):
		super().__init__()
		self.geometry("700x400")
		self.title(f"Window Resizer for {platform.system()}")
		#self.configure(bg="white")
		frm = Frame(self, padding=10)
		frm.grid(column=0, row=0, sticky=(N,W,E,S))
		self.grid_columnconfigure(1, weight=1)
		self.grid_columnconfigure(0, weight=1)
		
		

		disptitle = Label(self, text="Window Resizer", font=("Helvetica",40)) 
		disptitle.grid(row=1, column=0, columnspan=2)
		
		omtitle = Label(self, text="\nSelect a Process", font=("Helvetica")) 
		omtitle.grid(row=2, column=0)
		processes = []
		
		oselected = StringVar(self)
		oselected.set("-")
		processom = OptionMenu(self, oselected, *processes)
		processom.grid(row=3, column=0)

		if platform.system() == "Darwin":
			script = '''
			tell application "System Events"
				set visibleProcesses to name of every process whose background only is false
			end tell
			return visibleProcesses
			'''	
			result = subprocess.run(["osascript", "-e", script], capture_output=True, text=True)
			processes = result.stdout.split(", ")
			
			for process in processes:
				processom["menu"].add_command(label=process, command=lambda v=process: oselected.set(v))
			#[p.strip() for p in result.stdout.split(",")]		
							
	
		elif platform.system() == "Linux":
			print("linux")

		elif platform.system() == "Windows":
			print("windows")

App = app()
App.mainloop()
