# To display employees of different depts in pie chart
import matplotlib.pyplot as plt


# Take percentage of employees of 4 depts
slices= [50,20,15,15]
depts= ['sales' , 'production' , 'hr', 'finance']

cols= ['magenta', 'cyan', 'brown' , 'gold']



#create a pie chart
plt.pie(slices, labels= depts, colors = cols , startangle=90 , explode=(0,0.2,0,0), shadow = True, autopct= '%.1f%%')

#set company title
plt.title('WIPRO ')

# show legend
plt.legend()


#display the pie chart
plt.show()