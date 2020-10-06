"""
This will run a Kalman filter.

This project is for a motorized car.
You can measure the velocity of the car, but
you cannot measure its exact position.
"""

import numpy as np  # needed for matrix library


state = 0.0  # initial position
error = 1.0  # measured initial error
R = 1.0  # measured error covariance in y
Q = 0.25  # measured error covariance in x
veloc = 1.0  # velocity of car
delta_time = 1.0

for i in range(100):  # iterate

    # Predict
    aprior_state = state + veloc * delta_time  # a priori state
    control_var = aprior_state + R * np.random.rand() - R/2  # get measured position
    aprior_error = error + Q  # a priori error

    # Update
    kal_filter = aprior_error/(aprior_error + R)  # get filter
    state = aprior_state + kal_filter * (control_var - aprior_state)  # update state
    error = (1 - kal_filter) * aprior_error  # update error

    # Write
    print("Iter {0}: State {1}, Error {2}.".format(i, state, error))  # write
