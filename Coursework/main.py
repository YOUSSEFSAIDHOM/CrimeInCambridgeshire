from IPython import display
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Initializing the lists for the Data fetches, Cambridge 2020 and 2019

DataFetch_Cambs_2020 = [None] * 12
DataFetch_Cambs_2019 = [None] * 12

# Using iteration to fill in the data fetches from the csv files
months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

for month in range(len(months)):
    DataFetch_Cambs_2020[month] = len(pd.read_csv(Path(f'2020-{month+1:02}/2020-{month+1:02}-cambridgeshire-outcomes.csv')))
    DataFetch_Cambs_2019[month] = len(pd.read_csv(Path(f'2019-{month+1:02}/2019-{month+1:02}-cambridgeshire-outcomes.csv')))

crimes_2020 = [DataFetch_Cambs_2020[i] for i in range(12)]
crimes_2019 = [DataFetch_Cambs_2019[i] for i in range(12)]

x = np.arange(len(months))
width = 0.25
multiplier = 0

fig, ax = plt.subplots(layout='constrained')

persian_red = "#B4CDED"
verdigris = "#344966"
bg_color = "#efe6dd"

rects1 = ax.bar(x - width/2, crimes_2019, width, color=verdigris, label="2019")
rects2 = ax.bar(x + width/2, crimes_2020, width, color=persian_red,label="2020")

#ax.bar_label(rects1, padding=3)
#ax.bar_label(rects2, padding=3)

fig.patch.set_facecolor(bg_color) 
ax.set_facecolor(bg_color)

ax.set_ylabel("Crimes Reported")
ax.set_title("Crimes in Cambridgeshire, 2019 vs 2020")
ax.set_xticks(x, months)
ax.legend(loc="upper left", ncols=2)
ax.set_ylim(2000, max(max(crimes_2019), max(crimes_2020)) + 1000)
plt.show()
