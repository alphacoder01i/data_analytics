import num as np
import statistics as stat

arr=np.array([10,20,30,40])


#.shape=(rows,columns)
#.size=(no of elements)
#.ndim=(no of dimension)
#.dtype=(datatype)
#type()
#.astype=change type of array
#len()=no of nested value
#.subtract(a,b)=a-b
#.add(a,b)
#.divide(a/b)
#.multiply(a,b)
#.pow(x,y)
#.exp(x)
#.sqrt(x)

#combinig and spliting array(for arrays)
#if we add 2 list it will join  the value but in array it will add the value to best this  
#.concatenate is used
# we can use axis to get the  way of concatenation i want

#.hstack([list]) horizontal concat
#.vstack([list]) vertical concat

#.array_split(array name ,no of arrays)
#adding /removing element

#.append(x,y) append at last
#if its 2d it converts it in 1d then insert
#.insert(array,index,value)
#.delete(array,value in [])

#search,sort,filter

#.sort =ascending
#.where(condition) = for search
#searchsorted(array,value to search)= gives index workif sorted

#filter
ar=np.array([20,30,40,50])
fa=[True,False,False,True]
new=ar[fa]
print(new)

fa=ar>35
new=ar[fa]
print(new)

#aggregating function
#.sum=add all value
#.min=give min
#.max= giv max
#.mean=give mean
#.cumsum =cummulative sum 
ar=np.array([20,30,40,50])
print(np.cumsum(ar))
#output:- [ 20  50  90 140]

#.cumprod
print(np.cumprod(ar))
#output:- [     20     600   24000 1200000]
product_unit_price=np.array([20,30,40,50])
no_of_products=np.array([20,10,5,4])
print(np.cumprod([product_unit_price,no_of_products],axis=0))


#statitical function of numpy
#.mean
#.median
# no mode function in numpy so import statistics
#stats.mode
#np.std()=standard deviation
#np.var =(std).pow((2))
#np.corrcoef([list])= coeffecient of corelation
#-1 =proportional relationship
#1= inversely proportional relationship
#0 =no relation
#eg=
price=[300,100,350,150,200]
sales=[10,20,7,17,3]
print(np.corrcoef([price,sales]))
#output:-[[ 1.         -0.66621445][-0.66621445  1.        ]]