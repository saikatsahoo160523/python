from matplotlib import pyplot as plt
from matplotlib import style

style.use("ggplot")

x = [10,20,30]
y = [5,10,15]

x1 = [13,56,39]
y1 = [4,19,143]


plt.bar(x,y,color='g',label='line one')
plt.bar(x1,y1,color='r',label='line two')


plt.title("info")
plt.xlabel("yrs")
plt.ylabel("revenue")

plt.legend()

# plt.grid(True,color="k")

plt.show()

