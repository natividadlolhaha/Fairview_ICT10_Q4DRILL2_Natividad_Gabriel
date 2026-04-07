from pyscript import document
import numpy as np
import matplotlib.pyplot as plt

def sample_numpy(event):
    document.getElementById('output').innerHTML = " "

    days = np.array(['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun'])
    nuggetseaten = np.array([10, 5, 8, 12, 20, 15, 6])  # you can change these numbers

    plt.plot(days, nuggetseaten)
    plt.title("Chicken Nuggets Eaten Per Day")

    plt.show()