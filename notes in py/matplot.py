import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#to import charts in python
data1=["e01","e02","e03","e04","e05"]
data3=[34,35,36,33,37]

#plt.xlabel("emp_id")
#plt.ylabel("Age")
#plt.ylabel("Age",fontsize=20)

#plt.title("Ages of employees")
#plt.bar(data1,data3)
#plt.bar(data1,data3,color="black")
#or
#colorss=["red","blue","green","yellow","pink"]
#plt.bar(data1,data3,color=colorss)
# as color thre is width, edgecolor,ecolor,linewidth ,bottom and align and a lot click on
'''
ata = {
    "Date": [
        "2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04", "2023-01-05",
        "2023-01-06", "2023-01-07", "2023-01-08", "2023-01-09", "2023-01-10",
        "2023-01-11", "2023-01-12", "2023-01-13", "2023-01-14", "2023-01-15",
        "2023-01-16", "2023-01-17", "2023-01-18", "2023-01-19", "2023-01-20",
        "2023-01-21", "2023-01-22", "2023-01-23", "2023-01-24", "2023-01-25",
        "2023-01-26", "2023-01-27", "2023-01-28", "2023-01-29", "2023-01-30"
    ],
    "Category": [
        "Food", "Transport", "Entertainment", "Food", "Utilities",
        "Health", "Transport", "Entertainment", "Food", "Utilities",
        "Health", "Food", "Transport", "Entertainment", "Food",
        "Utilities", "Health", "Transport", "Entertainment", "Food",
        "Utilities", "Health", "Transport", "Entertainment", "Food",
        "Utilities", "Health", "Transport", "Entertainment", "Food"
    ],
    "Subcategory": [
        "Groceries", "Fuel", "Movies", "Dining Out", "Electricity",
        "Pharmacy", "Public Transport", "Concerts", "Snacks", "Water",
        "Gym Membership", "Takeout", "Taxi", "Streaming", "Meal Prep",
        "Internet", "Doctor Visit", "Car Maintenance", "Books", "Catering",
        "Gas", "Health Insurance", "Parking", "Video Games", "Bakery",
        "Trash Collection", "Supplements", "Bicycle Repair", "Sports Event", "Meal Kit"
    ],
    "Amount": [
        150.00, 50.00, 20.00, 75.00, 100.00,
        30.00, 15.00, 60.00, 25.00, 40.00,
        50.00, 45.00, 30.00, 15.00, 60.00,
        70.00, 120.00, 200.00, 25.00, 300.00,
        60.00, 150.00, 10.00, 40.00, 20.00,
        35.00, 45.00, 80.00, 100.00, 70.00
    ],
    "Mode": [
        "Credit Card", "Cash", "Debit Card", "Credit Card", "Bank Transfer",
        "Cash", "Debit Card", "Credit Card", "Cash", "Bank Transfer",
        "Debit Card", "Credit Card", "Cash", "Debit Card", "Credit Card",
        "Bank Transfer", "Cash", "Credit Card", "Debit Card", "Cash",
        "Bank Transfer", "Credit Card", "Cash", "Debit Card", "Credit Card",
        "Bank Transfer", "Cash", "Debit Card", "Credit Card", "Cash"
    ]
}
'''
#df = pd.DataFrame(ata)
#print(df)
#grouped_by=df.groupby("Mode")["Amount"].sum()
#print(grouped_by)
#plt.bar(df["Mode"],df["Amount"])
#plt.bar(grouped_by.index,grouped_by.values)
#plt.title("TRansfer amt")
#plt.show()


#lineplot
#x=["day1","day2","day3","day4","day5"]
#y=[360,420,250,230,400]
#y1=[400,300,350,300,250]

#plt.plot(x,y,marker="*",ls="--",color="red",label="week1")
#plt.plot(x,y1,marker="^",color="green",label="week2")
#plt.legend()
#add marker="design to add value,fillstyle,gapcolor,color, ls style,alpha can be used to make transparennt(0 to 1)"
#plt.show()

#plt.plot(df["Date"],df["Amount"])
#grou_by=df.groupby("Category")["Amount"].sum()
#plt.plot(grou_by.index,grou_by.values)

#plt.show()

#scatter plot
#x=np.random.rnadint(1,10,50)
#y=np.random.rnadint(1,10,50)
#plt.scatter(x,y)
#plt.colorbar()
#plt.show()

#pie chart
'''
brands=["Apple","Samsung","Nokia","Redmi","Poco"]
x=[50,30,10,80,60]
c=["red","blue","green","yellow","pink"]
ex=[0,0,0,0,0.1]
plt.pie(x,labels=brands,colors=c,explode=ex)
plt.show()
'''

#boxplot
#df.boxplot(list of int)

#histogram plot
#df.hist(list,bins= int)

#violen plot
#plt.violenplot(list,showmedians=True)

#stemplot
#plt.stem(list)

#stack plt
#one stack on another
#plt.stackplot(list[str],list[int],list2[int]...)
#baseline
#color
#label

'''
#step plot
plt.step
where
marker'''


'''
working with legends

plt.figure(figsize=[5,3])
loc=1 to 10 (location)
ncols=no  of colum in llegends
bbbox_to_anchor=(tuple of 2 number)(around 0-2)
'''


'''
subplot
plt.subplot(row ,column, chart number 1)
plt.subplot(row ,column, chart number 2)
plt.show()

plt.suptitile("str")=supertitle

'''


'''
saving graph as png
plt.savefig("str.extn") generaly photo
facecolor="color"(bg)
pad_inches = padding in inches
bbox_inches="tight","lose","etc"

'''