#intro  to seaborn  
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
'''
#line plot
ata={"Days":[1,2,3,4,5],
      "NOP":[50,40,60,30,44]}

df=pd.DataFrame(ata)
#print(df)

sns.lineplot(data=ata,x="Days",y="NOP")
#hue="row of str other than x,y like gender here"
#style
#pallete=color

#sns.color_pallete="vidris"or "hot" or "Gnbu"
plt.show()'''

'''
#barplot
data=sns.load_dataset("tips")
#print(data)
sns.barplot(data=data,x='day',y="tip",estimator='sum')
plt.plot()
plt.show() 
'''

'''
#hist plot
data=sns.load_dataset("tips")
sns.histplot(data,x="day",hue="sex",kde=True,discrete=True)
bins=no of blocks
plt.show()
'''

'''
#scatter plot
data=sns.load_dataset("tips")
sns.scatterplot(data,x="total_bill",y="tip",hue="day",size="size",palette="hot")
plt.show()
'''


'''
#heatmap
data=sns.load_dataset("tips")
gp=data.groupby("day").agg({"tip":"mean"})
sns.heatmap(gp)
plt.show()
 '''
 
'''
#count plot

data=sns.load_dataset("tips")
sns.countplot(data,x="day")
plt.show()

'''

'''
#violen plot
data=sns.load_dataset("tips")
sns.violinplot(data,x="tip",hue="sex")
plt.show()
'''

'''
#pair plot
data=sns.load_dataset("tips")
sns.pairplot(data,hue="day",diag_kind="plot")
plt.show()
'''


'''
#strip plot
sns.stripplot(data,x="day",y="tip")
plt.show()
'''

'''
box plot

data=sns.load_dataset("tips")
sns.boxplot(data,x="tip",y="sex",orient="vertical",fliersize=3 )
#y="sex"
plt.show()
'''


'''
cat plot

data=sns.load_dataset("tips")
sns.catplot(data,x="tip",y="day",hue="sex",dodge=True,kind="bar")
plt.show()
'''

'''
styles and color in plots
sns.setstyle(style="ticks")

sns.palplot(sns.colorpalette("types"))
'''


'''multiple plot

data=sns.load_dataset("tips")
a=sns.FacetGrid(data,col="time",height=2)
a.map(sns.barplot,"day","tip")
plt.show()
'''

'''
relational plot

data=sns.load_dataset("tips")
sns.relplot(data,x="tip",y="total_bill",hue="sex",kind="line",col="day")
plt.show()
'''

'''
#swarm plot
data=sns.load_dataset("tips")
sns.swarmplot(data,x="day",y="total_bill",hue="sex")
#,jitter=0.3 strip me hota h isme nhi hota
#point overplot nhi hota h like scatter and strip
plt.show()
'''


'''
#kde plot
#kernel density estimation
data=sns.load_dataset("tips")
sns.kdeplot(data,x="total_bill",hue="day",multiple="fill")
#multiple="stack"
plt.show()
'''
