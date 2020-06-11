#!/usr/bin/env python3
# coding=utf-8

#------------------------------------#
# Import the TK object from Tkinter
#------------------------------------#
from tkinter import Tk

#------------------------------------#
# Import the RiskSimGUI class
#------------------------------------#
from RiskSimGUI import RiskSimGUI

#------------------------------------#
# Launch the program
#------------------------------------#
if __name__ == "__main__":
		# Version of the program
		version = '1.4'
		# Create the window
		top = Tk()
		top.configure(bg='lightgrey') # Background of the window
		top.title("Risk Simulator") # Title of the window
		top.resizable(False, False) # Window not resizable
		# Make the window appear in the middle
		position_right = int(top.winfo_screenwidth()/2 - top.winfo_reqwidth()/2)
		position_down = int(top.winfo_screenheight()/2 - top.winfo_reqheight()/2)
		top.geometry("+{}+{}".format(position_right, position_down))
		# Fill the window
		RiskSimGUI(top, version)
		# Start the loop
		top.mainloop()
