# import matplotlib.pyplot as plt
# import numpy as np
# xpoints=np.arange(0,8,2)
# ypoints=np.arange(0,60,15)
# plt.plot(xpoints,ypoints,marker="*",mfc="yellow",mec="red")
# plt.show()

import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[10,20,25,30,50]
colors=['red','green','blue','purple','orange']
plt.scatter(x,y,c=colors,s=100)
plt.xlabel("X-axis label")
plt.ylabel("Y-axis label")
plt.title("scatter plot with different colors")
plt.grid(True)
plt.show()
