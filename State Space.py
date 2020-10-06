"""
State space modeling of shower.
Control shower nozzle flowrate and temperature
MManipulate shower hot and cold water flowrates.
HOt and cold water temperatures are disturbance.
"""

import numpy as np
import random

set_t_out = 25  # C
t_out = 0  # C
mean_t_hot = 30  # C
t_hot_var = 10  # C
mean_t_cold = 20  # C
t_cold_var = 10  # C

set_v_out = 1  # m3/min
v_out = 0  # m3/min
v_hot = 0  # m3/min
v_cold = 0  # m3/min

list_v_out = []  # list of v out over time
list_t_out = []  # list of t out over time

# Simulate
steps = 100  # number of steps
for i in range(steps):  # Simulate for x steps
    print("Update {0}".format(i))  # write

    # Update disturbance
    err_t_hot = t_hot_var * (random.random() - 0.5)  # get change
    t_hot = mean_t_hot + err_t_hot  # update disturbance
    err_t_cold = t_cold_var * (random.random() - 0.5)  # get change
    t_cold = mean_t_cold + err_t_cold  # update disturbance

    # Get error and apply disturbance
    try:
        err_t_out = set_t_out - t_out + v_hot / v_out * err_t_hot + v_cold / v_out * err_t_cold  # get error
    except ZeroDivisionError:
        err_t_out = set_t_out - t_out  # get error without disturbance
    err_v_out = set_v_out - v_out  # get error

    # Control
    delta_v_cold = (v_out * err_t_out - (t_hot + t_out) * err_v_out) / (t_cold - t_hot)  # control cold
    delta_v_hot = err_v_out - delta_v_cold  # control hot

    # Update
    v_cold += delta_v_cold  # update
    v_hot += delta_v_hot  # update

    v_out = v_cold + v_hot  # update
    t_out = (v_hot * t_hot + v_cold * t_cold) / v_out  # update

    # Add to list
    list_v_out.append(v_out)  # append to list
    list_t_out.append(t_out)  # append to list

    # Write
    print("T_cold: {0}, T_hot: {1}, T_out: {2}.".format(t_cold, t_hot, t_out))  # write
    print("V_cold: {0}, V_hot: {1}, V_out: {2}.".format(v_cold, v_hot, v_out))  # write)
    print("")  # add space

# Update results
std_v_out = np.std(list_v_out)  # standard deviation
std_t_out = np.std(list_t_out)  # standard deviation

print("T_out std: {0}, V_out std: {1}".format(std_t_out, std_v_out))  # write