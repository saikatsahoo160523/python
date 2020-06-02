from matplotlib import pyplot as plt
from matplotlib import style

style.use("ggplot")

x = [10,20,30]
y = [5,10,15]

x1 = [13,56,39]
y1 = [4,19,143]


plt.plot(x,y,'g',label='line one',linewidth=5)
plt.plot(x1,y1,'r',label='line two',linewidth=3)


plt.title("info")
plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.legend()

plt.grid(True,color="k")

plt.show()

