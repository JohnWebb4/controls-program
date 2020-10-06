""""
Defines a PID class and executes a program to test it
"""

import numpy as np


class Pid:
    def __init__(self, p, tau_i, tau_d, tau_f):
        """
        Initialize PID
        """
        # Define variables
        self.p = p
        self.tau_i = tau_i
        self.tau_d = tau_d
        self.tau_f = tau_f

        # Define variables
        self.integral_sum = 0  # initialize sum
        self.prev_value = None  # set previous value

    def pid(self, value):
        """
        Update pid for value
        :param value: Value to control
        :return: Result
        """
        # Update
        self.integral_sum += value  # update value

        # Control
        cont_value = self.p * value + self.integral_sum * self.tau_i + self.tau_d / self.tau_f * np.exp()

        # Return
        return cont_value  # return value


if __name__ == '__main__':  # if main
    print("Running PID Demo...")  # write
