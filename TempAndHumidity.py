from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA
import matplotlib.pyplot as plt

dataFromPi = [ # Object
    {
        "temperature": 23, # Temp data from Raspberry Pi object
        "humidity": "60%", # Humidity data fra Raspberry Pi object
        "timeStamp": "year-month-day hh:mm:ss" # Get current time (from Raspberry Pi - all the data should come from 1 source)
    },
    {
        "temperature": 26, 
        "humidity": "73%",
        "timeStamp": "year-month-day hh:mm:ss"
    },
    {
        "temperature": 22, 
        "humidity": "58%",
        "timeStamp": "year-month-day hh:mm:ss"
    },
]

host = host_subplot(111, axes_class=AA.Axes)
plt.subplots_adjust(right=0.75)

par1 = host.twinx()
par2 = host.twinx()

offset = 60
new_fixed_axis = par2.get_grid_helper().new_fixed_axis
par2.axis["right"] = new_fixed_axis(loc="right", axes=par2,
                                        offset=(offset, 0))

par2.axis["right"].toggle(all=True)

host.set_xlim(0, 2)
host.set_ylim(0, 2)

host.set_xlabel("Time")
host.set_ylabel("Temperature")
par1.set_ylabel("Temperature")
par2.set_ylabel("Humidity")

p1, = host.plot([0, 1, 2], [0, 1, 2], label="Temperature") 
p2, = par1.plot([0, 1, 2], [0, 3, 2], label="Humidity") 

par1.set_ylim(0, 4)
par2.set_ylim(1, 65)

host.legend()

host.axis["left"].label.set_color(p1.get_color())
par1.axis["right"].label.set_color(p2.get_color())
par2.axis["right"].label.set_color(p3.get_color())

plt.draw()
plt.show()

#plt.savefig("Test")