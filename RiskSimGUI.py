#!/usr/bin/env python3
# coding=utf-8

#------------------------------------#
# Import Tkinter
#------------------------------------#
import tkinter as tk

#------------------------------------#
# Import the RiskArmy class
#------------------------------------#
from RiskArmy import RiskArmy

#------------------------------------#
# Import the simulation function
#------------------------------------#
from simulation import simulation

#------------------------------------#
# Define RiskSimGUI class
#------------------------------------#
class RiskSimGUI(object):
    def __init__(self, window, version=None):
        # Save window object
        self.window = window
        # Get version
        self.version=version
        # Define fonts
        self.main_font = 'Helvetica 16 bold'
        self.big_font = 'Helvetica 16'
        self.title_font = 'Helvetica 14 bold'
        self.text_font = 'Helvetica 14'
        # Create initial armies
        self.attacker = RiskArmy()
        self.defender = RiskArmy()
        # Set number of simulations
        self.n_simulations = tk.IntVar()
        self.n_simulations.set(1000)
        # Create statistical variables
        self.att_fraction = tk.DoubleVar()
        self.def_fraction = tk.DoubleVar()
        self.avg_rounds = tk.DoubleVar()
        # Create frames
        self.top_frame = self.__frame_description()
        self.upper_frame = self.__frame_armies()
        self.middle_frame = self.__frame_simulator()
        self.lower_frame = self.__frame_results_container()
        self.inner_frame = self.__frame_results_init()
        self.bottom_frame = self.__frame_utils()

    def __frame_description(self):
        # Create frame
        frame = tk.Frame(self.window)
        frame.pack(fill="both", expand=True)
        # Fill frame
        subtitle = tk.Label(frame, text="Risk Europe Battle Simulator",
                anchor="n", font=self.main_font)
        description_txt="Please, enter the number of units in the attacker\nand defender armies and press 'Begin calculation'."
        description = tk.Label(frame, text=description_txt, font=self.big_font)
        subtitle.pack(fill="both", expand=True, side="top")
        description.pack(fill="both", expand=True, side="bottom")
        # Return the frame
        return frame

    def __frame_armies(self):
        # Create parent frame
        frame = tk.Frame(self.window, highlightbackground="black",
                highlightthickness=2, bg="lightgray")
        frame.pack(fill="both", expand=True)
        # Create the label at the top
        title = tk.Label(frame, text="Initial armies",
                font=self.main_font, bg="lightgray")
        title.pack(side="top")
        # Create left frame (attacker)
        left_frame = tk.Frame(frame, highlightbackground="red",
                highlightthickness=2, bg="lightgray")
        left_frame.pack(side="left", expand=True, fill="both")
        # Create right frame (defender)
        right_frame = tk.Frame(frame, highlightbackground="blue",
                highlightthickness=2, bg="lightgray")
        right_frame.pack(side="right", expand=True, fill="both")
        # Fill attacker's frame
        left_label = tk.Label(left_frame, text="Attacker army", anchor="n",
                font=self.title_font, bg="lightgray", fg="red")
        att_inf_label = tk.Label(left_frame, text="Infantry units: ", anchor="n",
                font=self.text_font, bg="lightgray")
        att_arc_label = tk.Label(left_frame, text="Archery units: ", anchor="n",
                font=self.text_font, bg="lightgray")
        att_cav_label = tk.Label(left_frame, text="Cavalry units: ", anchor="n",
                font=self.text_font, bg="lightgray")
        att_art_label = tk.Label(left_frame, text="Artillery units: ", anchor="n",
                font=self.text_font, bg="lightgray")
        att_inf_entry = tk.Entry(left_frame, textvariable=self.attacker.infantry,
                width=4, font=self.text_font)
        att_arc_entry = tk.Entry(left_frame, textvariable=self.attacker.archery,
                width=4, font=self.text_font)
        att_cav_entry = tk.Entry(left_frame, textvariable=self.attacker.cavalry,
                width=4, font=self.text_font)
        att_art_entry = tk.Entry(left_frame, textvariable=self.attacker.artillery,
                width=4, font=self.text_font)
        # Show stuff on attacker's frame
        left_label.grid(column=0, row=0, columnspan=2)
        att_inf_label.grid(column=0, row=1, sticky="n")
        att_inf_entry.grid(column=1, row=1, sticky="n")
        att_arc_label.grid(column=0, row=2, sticky="n")
        att_arc_entry.grid(column=1, row=2, sticky="n")
        att_cav_label.grid(column=0, row=3, sticky="n")
        att_cav_entry.grid(column=1, row=3, sticky="n")
        att_art_label.grid(column=0, row=4, sticky="n")
        att_art_entry.grid(column=1, row=4, sticky="n")
        # Fill defender's frame
        right_label = tk.Label(right_frame, text="Defender army", anchor="n",
                font=self.title_font, bg="lightgray", fg="blue")
        def_inf_label = tk.Label(right_frame, text="Infantry units: ", anchor="n",
                font=self.text_font, bg="lightgray")
        def_arc_label = tk.Label(right_frame, text="Archery units: ", anchor="n",
                font=self.text_font, bg="lightgray")
        def_cav_label = tk.Label(right_frame, text="Cavalry units: ", anchor="n",
                font=self.text_font, bg="lightgray")
        def_art_label = tk.Label(right_frame, text="Artillery units: ", anchor="n",
                font=self.text_font, bg="lightgray")
        def_inf_entry = tk.Entry(right_frame, textvariable=self.defender.infantry,
                width=4, font=self.text_font)
        def_arc_entry = tk.Entry(right_frame, textvariable=self.defender.archery,
                width=4, font=self.text_font)
        def_cav_entry = tk.Entry(right_frame, textvariable=self.defender.cavalry,
                width=4, font=self.text_font)
        def_art_entry = tk.Entry(right_frame, textvariable=self.defender.artillery,
                width=4, font=self.text_font)
        # Show stuff on defender's frame
        right_label.grid(column=0, row=0, columnspan=2)
        def_inf_label.grid(column=0, row=1)
        def_inf_entry.grid(column=1, row=1)
        def_arc_label.grid(column=0, row=2)
        def_arc_entry.grid(column=1, row=2)
        def_cav_label.grid(column=0, row=3)
        def_cav_entry.grid(column=1, row=3)
        def_art_label.grid(column=0, row=4)
        def_art_entry.grid(column=1, row=4)
        # Return the frame
        return frame

    def __frame_simulator(self):
        # create the frame
        frame = tk.Frame(self.window, highlightbackground="black",
                highlightthickness=2, bg="lightgray")
        frame.pack(fill="both", expand=True)
        # Fill the frame
        calculate_button = tk.Button(frame, text="Begin calculation", bg="lightgray",
                command=self.__button_calculate, font=self.text_font)
        n_sim_label = tk.Label(frame, text="Number of simulations per calculation: ",
                font=self.text_font, bg="lightgray")
        n_sim_entry = tk.Entry(frame, textvariable=self.n_simulations, font=self.text_font,
                width=7)
        # Show stuff in the frame
        calculate_button.pack(side="top", expand=True, fill="both", padx=3)
        n_sim_label.pack(side="left", padx=3)
        n_sim_entry.pack(side="right", padx=3)
        # Return the frame
        return frame

    def __frame_results_container(self):
        # Create the frame
        frame = tk.Frame(self.window, highlightbackground="black", highlightthickness=2,
                bg="lightgray")
        frame.pack(fill="both", expand=True)
        # Create the label at the top
        title = tk.Label(frame, text="Battle results", font=self.main_font, bg="lightgray")
        title.pack(side="top", expand=True, fill="both")
        # Return the frame
        return frame

    def __frame_results_init(self):
        # Create the frame
        frame = tk.Frame(self.lower_frame, bg="lightgray")
        frame.pack(fill="both", expand=True)
        # Create the text
        no_data = tk.Label(frame, text="[NO DATA]", font=self.text_font, anchor="n",
                bg="lightgray", pady=33)
        no_data.pack()
        # Return the frame
        return frame

    def __frame_results_filled(self):
        # Create the frame
        frame = tk.Frame(self.lower_frame, bg="lightgray")
        frame.pack(fill="both", expand=True)
        # Create the text of the summary
        line_1 = "Out of " + str(self.n_simulations.get()) + " simulations:"
        line_2 = "The attacker won " + str(self.att_fraction.get()) + "% of the battles."
        line_3 = "The defender won " + str(self.def_fraction.get()) + "% of the battles."
        line_4 = "In an average of " + str(self.avg_rounds.get()) + " rounds."
        # Create the summary
        label_l1 = tk.Label(frame, text=line_1, font=self.text_font, anchor="w",
                padx=6, bg="lightgray")
        label_l2 = tk.Label(frame, text=line_2, font=self.text_font, anchor="w",
                padx=20, bg="lightgray")
        label_l3 = tk.Label(frame, text=line_3, font=self.text_font, anchor="w",
                padx=20, bg="lightgray")
        label_l4 = tk.Label(frame, text=line_4, font=self.text_font, anchor="w",
                padx=6, bg="lightgray")
        # Show the summary
        label_l4.pack(side="bottom",  fill="x")
        label_l3.pack(side="bottom",  fill="x")
        label_l2.pack(side="bottom",  fill="x")
        label_l1.pack(side="bottom",  fill="x")
        # Return the frame
        return frame

    def __frame_utils(self):
        # Create the frame
        frame = tk.Frame(self.window)
        frame.pack(fill="both", expand=True)
        # Create the buttons
        button_reset = tk.Button(frame, text="Reset", command= self.__button_reset,
                font=self.text_font)
        button_exit = tk.Button(frame, text="Exit", command=self.__button_exit,
                font=self.text_font)
        if self.version:
            ver_label = tk.Label(frame, text='v'+self.version, font=self.text_font, anchor=tk.CENTER)
            ver_label.pack(side="left")
        button_exit.pack(fill="x", side="right")
        button_reset.pack(fill="x", side="right")



    def __button_reset(self):
        # Reset the number of simulations
        self.n_simulations.set(1000)
        # Reset the initial armies
        self.attacker.set_infantry(0)
        self.attacker.set_archery(0)
        self.attacker.set_cavalry(0)
        self.attacker.set_artillery(0)
        self.defender.set_infantry(0)
        self.defender.set_archery(0)
        self.defender.set_cavalry(0)
        self.defender.set_artillery(0)
        # Reset the result frame
        self.inner_frame.destroy()
        self.inner_frame = self.__frame_results_init()


    def __button_calculate(self):
        # Perform simulation
        sim = simulation(self.n_simulations.get(), self.attacker, self.defender)
        self.avg_rounds.set(sim['rounds_avg'])
        self.att_fraction.set(sim['attacker_win_fraction']*100)
        self.def_fraction.set(sim['defender_win_fraction']*100)
        # Redraw the result inner frame
        self.inner_frame.destroy()
        self.inner_frame = self.__frame_results_filled()

    def __button_exit(self):
        self.window.destroy()
