import pandas as pd
import numpy as np

# data = {"Name":["Aditya","Parth","Harsh"],
#         "Age":["21","23","21"],
#         "Salary":[30000,32000,25000]
#         }
# df = pd.DataFrame(data)
# print(df)

# dat = pd.read_csv("a.csv")  # order file like execel file ya fr csv file read with the help of pd
# print(dat)

# =========================== exploring data in pandas ========================

# data = pd.read_excel("Book1.xlsx") 
# print(data)
# print(data.head(10))  # ya file mai sa start in ki 10 value da dega har column mai sa value da dega
# print(data.tail(10))  # ya file mai sa nicha sa  10 value ko   da dega har column mai sa value da dega
# print(data.info())      # is sa file ki under ki value k data type bata hai.. 
# data.describe()         # ya file ki numerical value mai sa kucj=h data lakr deta hai.. 
# print(data.isnull().sum())    # ya null value ko count kerta hai ki kitni value null hai humeri file mai..


# =============================== Handle a duplicate values in pandas ==========================

# data = pd.read_excel("adi.xlsx") 
# print(data)
# print(data["id"].duplicated().sum())  # isa to check a duplicate hai ya nhi 
# print(data.drop_duplicates("id"))       # or isa duplicate o delete kiya ja sakta hai.. 

# ===================================== Working with missing data in pandas ==========================================

# data = pd.read_csv("a.csv") 
# print(data)
# print(data.isnull().sum())           
# print(data.dropna())                     # isa null value ko delete kiya ja sakta hai....
# print(data.replace(np.nan,"Chutiya"))    # isa null value ko fill kr sakta hai... 

# ============================= Column Transformation in pandas part 1 ====================================  43:21 breal / pause video

# data = pd.read_excel("Adi.xlsx") 
# print(data)
# data.loc[(data["Bonus"]==0),"GetBonus"]="no Bonus"   # perticular lucation pr check krna or add on kerna
# data.loc[(data["Bonus" ] > 0), "GetBonus"] = "Bonus"
# print(data)

# data = pd.read_excel("Practice.xlsx") 
# print(data)
# print()
# data["FullData"] = data["Fname"] +" "+ data["Lname"]   # add extra column in table
# print(data)

# ============================= Column Transformation in pandas part 2 ====================================  

# data = pd.read_excel("Practice.xlsx") 
# print(data)
# print()
# data["Bonus"] = (data["salary"]/100)*20  # add on extra column in the table
# print(data)

# data = {"Months":["January","February","March","April","May","June"]}
# print(data)
# a = pd.DataFrame(data)
# print(a)
# print()
# def extract(value):
#     return value[0:3]  # ya string ki value ko leta hai.. 
# a["Short_Month"] = a["Months"].map(extract)
# print(a)

# ================================= Group By in Pandas ===================================

# data = pd.read_excel("Emp.xlsx") 
# print(data)
# print()
# gp = data.groupby(["Depart","Gender"]).agg({"EEID":"count"})
# print(gp)

# ============================= Merge , Join and Concatenate in pandas ===========================

# data1 = {"Emp Id":["E01","E02","E03","E04","E05","E06"],
#          "Name":["Rave","Rahul","Harash","Manoj","Jaadu","Vishal"],
#          "Age":[25,32,26,28,27,21]}

# data2 = {"Emp Id":["E01","E02","E03","E04","E05","E06"],
#          "Salary":[40000,25000,20000,50000,30000,35000]}

# df1 = pd.DataFrame(data1)
# df2 = pd.DataFrame(data2)
# print(df1)
# print()
# print(df2)
# print()
# print(pd.merge(df1,df2,on="Emp Id"))   # merge on the basis of Emp id
# print(pd.concat([df1,df2]))

# ============================== Pandas | Compare Data Frames ========================================

# dict = {"Fruits":["Mango","Apples","Banana","Papaya"],
#         "Price":[100,150,50,40],
#         "Quantity":[15,10,10,3]}

# df1 = pd.DataFrame(dict)
# print(df1)
# print()
# df2 = df1.copy()

# df2.loc[0,"Price"]=80
# df2.loc[1,"Price"]=190
# df2.loc[2,"Price"]=30
# df2.loc[3,"Price"]=50
# df2.loc[0,"Quantity"]=20
# df2.loc[1,"Quantity"]=11
# df2.loc[2,"Quantity"]=18
# df2.loc[3,"Quantity"]=5
# print(df2)
# print()
# print(df1.compare(df2))

# ================================== Pivoting and Melting Data Frame in Pandas =====================================

# dict = {"Keys":["k1","k2","k1","k2"],
#         "Name":["Rahul","Namita","Anita","Arjun"],
#         "House":["red","green","blue","red"]}

# df = pd.DataFrame(dict)
# print(df)
# print()
# pivot_df = df.pivot_table(index='Keys', columns='Name', values='House', aggfunc='first')
# print(pivot_df)
# print(df.pivot_table("Keys","Name","House","first"))

# dict = {"Name":["Rahul","Namita","Anita","Arjun"],
#         "House":["red","green","blue","red"],
#         "Age":[22,23,28,20]}

# df = pd.DataFrame(dict)
# print(df)
# print()
# print(pd.melt(df,id_vars=["Name"],value_vars=["House"]))