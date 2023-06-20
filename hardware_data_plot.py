import pandas as pd
import matplotlib.pyplot as plt
hardware_data = pd.read_csv("2023-06-13-survey.csv")
for column in hardware_data.columns:
    print("LOOP WORKS")
    plt.figure()
    plt.title(column)
    plt.hist(hardware_data[column], bins = 10)
    plt.show()