'''
1. formula bar 
adding formula to cell

2.ctrl+ t 
table

3.doubl click on row to autoset

4.autofill
ctrl+scroll

5. flash fill
eg full name to firstname and lastname
auto options come click enter

6. text tp column
select whole row 
data -> ttext to column ->choose format ->finish

7.data validation
select whole row->data->data validation -> Allow? ->data etc....

8.data connnectors
from web
data->getdata->other sources->from web->url with a table ->select 1 or multiple table->ok
from queries and conn -> table name-> ... ->load to ->ok

from mysql
download odbc mysql driver
data->getdata->other sources->from

9.conditional formatting
hignlight
top/bottom 
data bars 
color scales

10. basic formatting

11. data filtering
ctrl+shift+l  

12. null values in excel

select row + f5 -> special->ctrl+-
or 
find and selct->go to special ->blanks-> ctrl+f5 ->entire rows or etc


niche wali value bahrne ke liye 
special->blanks->formulae:=niche wala cell->ctrl+enter
agr niche kch nhi value 0
or directly value daldo

13.  for duplicate values
select primary key row ->data->datatool ->delete duplicates

14.trim(cell)
for extra space

15. fixing column format
home->number->currency etc

16.text function
a) =CONCATENATE(cell,cell," ",cell,....)
b)=LOWER(cell)
c)=UPPER(CELL)
D)=Proper(cell)
e)=len(cell)
f)=left(cell,char no (default=1))
g)=right(cell,charno)
h)=mid(cell,start ,char no)
i)=find("x",cell)
j)=search("x", cell)
k)=replace(cell,start,charno,text/num)
l)=substitute(cell,"text","text",no of times)

17) if, and & or
=if(condition, for true,for false)
=if(and(condition1,codn2,...),for trrue,for false)
=if(or(condition1,codn2,...),for trrue,for false)

18.date time fnc
=today()
date
=now()
time and date
=day(cell with date)
=month(cell with date)
=year('')
=date(year,month,date)
=hour(cell with time)
=minute(cell with time )
=second('')


to add or remove date
=cell with date +/- no of days
to add or remove month
=edate(cell,no of month to add)
to add or remove year
=edate(cell,year to month)

19.sum,count,countif,countifs,summif,sumifs
=sum([row])
=sumif([row1],"text"/criteria,[row to sum])     for single comdiition
=sumifs([row to sum],[row1],creteria for row 1,[row2],criteria for row2)
=count([row])
=countif([row],criteria)
=countifs([row1],criteria,[row2],criteria)


20.xlookup
=xlookup(cell,[row1],[row2])

21.power query
get dta->excel

22.cleaning and transformation
replace value(null to blank or str or number)
remove row(blank rows)
fill->down

23.text tools in pq
split column->by delimetre
add column->custom column->new column name +formulae
format->....

24.number tools
right click on row->remove errors or add
stardard->...->tranform
statistic->...
scientific->...
rounding->...
datetime tools->
date->....
time->...
duration->...
add column->conditional column->...

25.combining multiple data
get data ->get 2 file 
content->combine files

26.data modelling(impppppppppp)
developer->com add in 
or 
file->option->addins->comaddins->mspowerpivot
pivot->manage->diagram view

27.importt data into powerpivot
file->options->customize ribbon ->enable developer->addins->comaddins->power pivot->ok
manage->from other sources
or
slect multiple data 
import to power query -> select multiple ->transform->close and load to..->
table->add this data to data model
data->model

28.cardinality and filter direction
pivottable->from datamodel->

29.hierachy in excel
create hierachy in diagram in ddata model

30.pivot tables
31.slicer
32.buttons
shape->right click->link->options

33.macros
on developer in options
'''
