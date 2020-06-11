#!/usr/bin/env python3
# coding=utf-8

#------------------------------------#
# Import the IntVar object
#------------------------------------#
from tkinter import IntVar

#------------------------------------#
# Define RiskArmy class
#------------------------------------#
class RiskArmy(object):
		def __init__(self, **kwargs):
				# Create variables to save the army components
				self.infantry = IntVar()
				self.archery = IntVar()
				self.cavalry = IntVar()
				self.artillery = IntVar()
				# Parse the initializers
				for key, value in kwargs.items():
						if self.__check(value):
								if key in ["inf","infantry"]:
										self.infantry.set(value)
								elif key in ["arc","archery"]:
										self.archery.set(value)
								elif key in ["cav","cavalry"]:
										self.cavalry.set(value)
								elif key in ["art","artillery"]:
										self.artillery.set(value)
								else:
										raise Exception("Unrecognized parameter: " + key)
						else:
								raise Exception("The value " + value + " passed with " + key + " is invalid.")

		def __check(self,n):
				if type(n) is not int:
						return False
				elif n < 0:
						return False
				else:
						return True

		def get_infantry(self):
				return self.infantry.get()

		def get_archery(self):
				return self.archery.get()

		def get_cavalry(self):
				return self.cavalry.get()

		def get_artillery(self):
				return self.artillery.get()

		def set_infantry(self, n):
				if self.__check(n):
						self.infantry.set(n)
				else:
						raise Exception("The value " + n + " passed is invalid.")

		def set_archery(self, n):
				if self.__check(n):
						self.archery.set(n)
				else:
						raise Exception("The value " + n + " passed is invalid.")

		def set_cavalry(self, n):
				if self.__check(n):
						self.cavalry.set(n)
				else:
						raise Exception("The value " + n + " passed is invalid.")

		def set_artillery(self, n):
				if self.__check(n):
						self.artillery.set(n)
				else:
						raise Exception("The value " + n + " passed is invalid.")

		def absorb_damage(self, dmg):
				 if  not self.__check(dmg):
						 raise Exception("The value " + dmg + " passed is invalid.")
				 else:
						 if dmg <= self.infantry.get():
								 self.infantry.set(self.infantry.get() - dmg)
						 else:
								 dmg -= self.infantry.get()
								 self.infantry.set(0)
								 if dmg <= self.archery.get():
										 self.archery.set(self.archery.get() - dmg)
								 else:
										 dmg -= self.archery.get()
										 self.archery.set(0)
										 if dmg <= self.cavalry.get():
												 self.cavalry.set(self.cavalry.get() - dmg)
										 else:
												 dmg -= self.cavalry.get()
												 self.cavalry.set(0)
												 if dmg <= self.artillery.get():
														 self.artillery.set(self.artillery.get() - dmg)
												 else:
														 self.artillery.set(0)

		def is_alive(self):
				n = self.infantry.get() + self.archery.get() + self.cavalry.get() + self.artillery.get()
				if n > 0:
						return True
				else:
						return False

		def get_total_size(self):
				return self.infantry.get() + self.archery.get() + self.cavalry.get() + self.artillery.get()

		def copy(self):
				return RiskArmy(inf=self.infantry.get(), arc=self.archery.get(), cav=self.cavalry.get(),
								art=self.artillery.get())
