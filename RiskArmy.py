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
        # Check that the variable "n" is an integer.
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
        # Absorve damage caused to this army by killing units.
        # The units are killed from the less valuable to the most valuable.
        # The actual order is: infantry < archery < cavalry < artillery
        if  not self.__check(dmg):
            raise Exception("The value " + dmg + " passed is invalid.")
        else:
            # Check whether the damage can be fully absoved by infantry.
            if dmg <= self.infantry.get():
                # If the damage is lower than the infantry, kill some infantry.
                self.infantry.set(self.infantry.get() - dmg)
            # If the damage cannot be absorved only with infantry, propagate it.
            else:
                # Get the remaining damage after having killed all the infantry.
                dmg -= self.infantry.get()
                # Actually kill all the infantry (set it to 0).
                self.infantry.set(0)
                # Check whether the damage can be fully absorved by archery.
                if dmg <= self.archery.get():
                    # If the damage is lower than the archery, kill some archery.
                    self.archery.set(self.archery.get() - dmg)
                # If the damage cannot be absorved only with archery, propagate it.
                else:
                    # Get the remaining damage after having killed all the archery.
                    dmg -= self.archery.get()
                    # Actually kill all the archery (set it to 0).
                    self.archery.set(0)
                    # Check whether the damage can be fully absorved by cavalry.
                    if dmg <= self.cavalry.get():
                        # If the damage is lower than the cavalry, kill some cavalry.
                        self.cavalry.set(self.cavalry.get() - dmg)
                    # If the damage cannot be absorved only with cavalry, propagate it.
                    else:
                        # Get the remaining damage after having killed all the cavalry.
                        dmg -= self.cavalry.get()
                        # Actually kill all the cavalry (set it to 0).
                        self.cavalry.set(0)
                        # Check whether the damage can be fully absorved by artillery.
                        if dmg <= self.artillery.get():
                            # If the damage is lower than the artillery, kill some artillery.
                            self.artillery.set(self.artillery.get() - dmg)
                        # If the damage cannot be absorved only with artillery, it means that the army has been destroyed.
                        else:
                             # Actually kill the artillery (set it to 0).
                             self.artillery.set(0)

    def is_alive(self):
        # Check whether an army is alive (whether it has remaining units).
        n = self.infantry.get() + self.archery.get() + self.cavalry.get() + self.artillery.get()
        if n > 0:
            return True
        else:
            return False

    def get_total_size(self):
        # Get the total size of the army.
        return self.infantry.get() + self.archery.get() + self.cavalry.get() + self.artillery.get()

    def copy(self):
        # Copy this class.
        return RiskArmy(inf=self.infantry.get(), arc=self.archery.get(), cav=self.cavalry.get(),
                art=self.artillery.get())
