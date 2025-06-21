import pandas as pd

data = {
    "Name": ["John", "Peter", "Lisa"],
    "Age": [25, 28, 31],
    "Salary": [300000, 25000.10, 10000]
}

df = pd.DataFrame(data)
#print(df)

data2=pd.read_csv("hotel_booking.csv")
#print(data2)

data3=pd.read_excel("fsi-2010.xlsx")
#print(data3)


#Exploring data{
#data.head(value in number)
#data.tail(valu ein no)
#data.info()
#data.describe()= gives stats
#data.isnull()
#data.isnull.sum()
#}

#Handling Duplicate values
#data.duplicated() = row wise
#data["row"].duplicated() 
#data["row"].duplicated().sum
#data.drop_duplicates("row") = for column



#Working with missing data
#data.isnull().sum()
#data.isnull().dropna() drop null value
#data.replace(np.nan("3000"))
#data["salary "].replace(np.nan("3000"))


#data.fillna(method = "bfill") = bilateral fill
#data.fillna(method = "ffill") 
#jab uper ka valueniche aur niche ka value upar chahiye



#column transformation

#df.loc[(df["previous row data"] condition(==0,>20)),"new row name"]="value in column"
#on different condition give different value then
#print(df.head(10))

#data["new row"]=data["prvious data1"]+data["previous data 2"]

data1={"emp_id":["e01","e02","e03","e04","e05"],
       "Names":["Ram","Shyam","Ram","Ravi","Manu"],
       "Age":[34,35,36,33,37]}

data2={"emp_id":["e01","e02","e03","e04","e05"],
       "salary":[45000,35000,35000,53000,64000]
}
data3={"emp_id":["e07","e08","e09","e10","e11"],
       "Names":["Rm","Sm","am","avi","annu"],
       "Age":[34,35,36,33,37]}
df1=pd.DataFrame(data1)
df2=pd.DataFrame(data2)
df3=pd.DataFrame(data3)
#print(df1)
#print(df2)

#print(pd.merge(df1,df2,on="emp_id"))
  
#print(pd.merge(left= df1,right=df2,on="emp_id",how="left"))

#print(pd.concat([df1,df3]))



#comparing dataframes

#dataframe.copy()
#df1.compare(df2)
#df1.compare(df2,align_axis=0)
#df1.compare(df2,keep_equal=True)
#df1.compare(df2,keep_shape=True)



#Pivoting and melting dfs

#df.pivot("row1","row2","row3")
#df.pivot(index="row1",column="row2",value=["row3","row4"])

#print(pd,,melt(df,id_vars=["row2"],value_vars="row3"))
#row ka name change krke new row bnega

#print(pd,,melt(df,id_vars=["row2"],value_vars="row3",var_name="House&Grades",value_name="values"))

