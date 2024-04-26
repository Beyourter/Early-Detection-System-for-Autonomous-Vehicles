import tkinter as tk
from tkinter import ttk
import time

import clearance
import getOutput
import runFile
import updateXML
import modNet

# Define variables
speed_value = [20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
density_menu_list = ["Single Car", "Low", "Medium", "High"]
location_list = modNet.get_route()
lane_list = ['0', '1', '2', '3']
start_time = 5
end_time = 250


def sim_sumo():  # configure simulation files and running SUMO simulation file
    speed = int(speed_combobox.get()) / 3.6
    density = density_combobox.get()
    location = location_combobox.get()
    lane = lane_combobox.get()

    print("Traffic speed: " + str(speed_combobox.get()) + " km/hr")

    if density == "Low":
        spawn_rate = 1000
    elif density == "Medium":
        spawn_rate = 2000
    elif density == "High":
        spawn_rate = 3000
    else:
        spawn_rate = 0

    print("Accident lane: " + str(lane))
    # print("Start time: " + str(start_time))
    # print("End time: " + str(end_time))
    print("Traffic density: " + str(spawn_rate) + " cars per hour")
    # notice_distance = clearance.cal_dist(speed, spawn_rate)
    print("Clearance distance: " + str(clearance.notice_distance(speed)) + " m")
    tau = clearance.cal_tau_2(speed)
    print("TAU: " + str(tau) + " s")

    updateXML.modify(location, lane, start_time, end_time, spawn_rate, clearance.cal_tau_2(speed))
    modNet.modify_speed(speed)

    time.sleep(2)

    print("Opening SUMO...")

    runFile.open_sumo()


def gen_output():  # generate output from the SUMO output files and display on the command line
    getOutput.get_output()


# Start Here
root = tk.Tk()

# Root window
root.title("EDS")
root.option_add("*tearOff", False)
root.resizable()
root.columnconfigure(0, weight=4)


# Create a style and setting up theme
style = ttk.Style(root)
root.tk.call("source", "forest-light.tcl")
style.theme_use("forest-light")

# Frame
frame = ttk.Frame(root)
frame.pack()

# Frame 1

report_input_frame = ttk.LabelFrame(frame, text="Accident Report", width=300)
report_input_frame.grid(row=0, column=0, sticky=tk.EW, padx=10, pady=5)

location_label = ttk.Label(report_input_frame, text="Location: ", width=10)
location_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
location_combobox = ttk.Combobox(report_input_frame, values=location_list, width=20)
location_combobox.current(2)
location_combobox.grid(row=0, column=1, padx=10, pady=5, sticky=tk.E)

lane_label = ttk.Label(report_input_frame, text="Lane: ")
lane_label.grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
lane_combobox = ttk.Combobox(report_input_frame, values=lane_list)
lane_combobox.current(0)
lane_combobox.grid(row=1, column=1, padx=10, pady=5, sticky=tk.E)

# Frame 2

traffic_input_frame = ttk.LabelFrame(frame, text="Traffic Conditions", width=300)
traffic_input_frame.grid(row=1, column=0, sticky=tk.EW, padx=10, pady=5)

speed_label = ttk.Label(traffic_input_frame, text="Speed (kph): ", width=10)
speed_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
speed_combobox = ttk.Combobox(traffic_input_frame, values=speed_value, width=20)
speed_combobox.current(4)
speed_combobox.grid(row=0, column=1, padx=10, pady=5, sticky=tk.E)

density_label = ttk.Label(traffic_input_frame, text="Density: ")
density_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
density_combobox = ttk.Combobox(traffic_input_frame, values=density_menu_list)
density_combobox.current(0)
density_combobox.grid(row=1, column=1, padx=10, pady=5, sticky=tk.E)

# Simulation button

simulate_button = ttk.Button(frame, text="Simulate", command=sim_sumo, width=20)
simulate_button.grid(row=3, column=0, padx=10, pady=10)

# Generate Output button

simulate_button = ttk.Button(frame, text="Generate Output", command=gen_output, width=20)
simulate_button.grid(row=4, column=0, padx=10, pady=10)


root.update()

root.mainloop()
