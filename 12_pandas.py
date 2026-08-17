# ======================================================
# READING OR IMPORTING FILES (excel, csv, json)
# ======================================================
import pandas as pd

df = pd.read_csv(r"C:\Users\VIJAY K G\Downloads\employees_500_rows.csv")
# df = pd.read_excel()
# df = pd.read_json()
print(df)

# ============
# SAVE FILES
# ============

import pandas as pd
data = {"name": ['ram','nam','shyam'],
        "age": [21,24,27],
        "salary": [35000,43000,28000]}

df = pd.DataFrame(data)
print(df)

df.to_csv("output.csv",index = False)
# df.to_excel()
# df.to_json()
print(df)

# ====================
# BASIC INFORMATION
# ====================

import pandas as pd
data = {"name": ['ram','nam','shyam'],
        "age": [21,24,27],
        "salary": [35000,43000,28000]}

df = pd.DataFrame(data)

print(df)
print(df.head())
print(df.tail())
print(df.info())
print(df.shape)
print(df.columns)
print(df.describe())

# ===================
# SELECTING COLUMNS
# ===================

import pandas as pd
data = {"name": ['ram','nam','shyam'],
        "age": [21,24,27],
        "salary": [35000,43000,28000]}  

df = pd.DataFrame(data)

print(df["name"])
print(df[["name","salary"]])

# ===================
# UPDATING COLUMNS
# ===================

# ADD COLUMN

import pandas as pd
data = {"name": ['ram','nam','shyam'],
        "age": [21,24,27],
        "salary": [35000,43000,28000]}  

df = pd.DataFrame(data)
df ["bonus"] = df["salary"] * 0.1
print(df)

# ADD USING INSERT FOR POSITION

import pandas as pd
data = {"name": ['ram','nam','shyam'],
        "age": [21,24,27],
        "salary": [35000,43000,28000]}  

df = pd.DataFrame(data)
df.insert(0,"emp_id",[1,2,3])
print(df)

# SPECIFIC VALUE UPDATE

import pandas as pd
data = {"name": ['ram','nam','shyam'],
        "age": [21,24,27],
        "salary": [35000,43000,28000]}  

df = pd.DataFrame(data)
print(df)

df.loc[0,"salary"] = 40000
print(df)

# UPDATE WHOLE COLUMN

import pandas as pd
data = {"name": ['ram','nam','shyam'],
        "age": [21,24,27],
        "salary": [35000,43000,28000]}  

df = pd.DataFrame(data)
print(df)

df["salary"] = df["salary"] * 1.05
print(df)

# REMOVE COLUMN

import pandas as pd
data = {"name": ['ram','nam','shyam'],
        "age": [21,24,27],
        "salary": [35000,43000,28000]}  

df = pd.DataFrame(data)
print(df)

df.drop(columns = ["salary"],inplace = True)
print(df)

# REMOVE DUPLICATES

import pandas as pd
df = pd.read_excel(r"C:\Users\VIJAY K G\Downloads\Raw Data Excel Practice.xlsx")
print("\n Duplicated rows", df.duplicated().sum())

df = df.drop_duplicates()
print(df)

# ========================
# HANDLING MISSING DATA
# ========================

# BLANK ROWS

import pandas as pd
df = pd.read_excel(r"C:\Users\VIJAY K G\Downloads\Raw Data Excel Practice.xlsx")
# df = pd.isnull(df)
df = pd.isnull(df).sum()
print(df)

# REMOVE NONE VALUE

import pandas as pd
df = pd.read_excel(r"C:\Users\VIJAY K G\Downloads\Raw Data Excel Practice.xlsx")
print("\ntotal rows: " ,df.count())

df.dropna(inplace=True)
print(df)

# REPLACE OR FILL NONE VALUES FRO STRINGS

import pandas as pd
df = pd.read_excel(r"C:\Users\VIJAY K G\Downloads\Raw Data Excel Practice.xlsx")
df.fillna("unknown", inplace=True)
print(df)

# # REPLACE FOR NUMARIC VALUE

# import pandas as pd
# df = pd.read_excel(r"C:\Users\VIJAY K G\Downloads\Raw Data Excel Practice.xlsx")
# df["age"].fillna(df["age"].mean(), inplace=True)
# print(df)

# REMOVE DUPLICATE, REPLACE NULL VALUE WITH "UNKOWN" AND SAVED IN EXCEL FILE

import pandas as pd
df = pd.read_excel(r"C:\Users\VIJAY K G\Downloads\Raw Data Excel Practice.xlsx")
df = df.drop_duplicates()
df.fillna("unknown", inplace=True)
print(df)

df.to_excel("raw_data_output.xlsx", index=False)
print(df)

# INTERPOLATION (AUTO FILL THE VALUES ON THE BASIS OF TRENDS OR SERIES

import pandas as pd
data = {"time": [1,2,3,None,5,6,None,8]}
df = pd.DataFrame(data)
df["time"] = df["time"].interpolate(method="linear")
print(df)

# =============
# FILTERING 
# =============

import pandas as pd

df = pd.read_excel(r"C:\Users\VIJAY K G\Downloads\Raw Data Excel Practice.xlsx")
print("\nsales more than 75000")
high_salary = df[df["Sales"] > 75000]
print(high_salary)

print("\nsales more than 75000 and order date more than 2025-01-01")
high_salary = df[(df["Sales"] > 75000) & (df["Order_Date"] > "2025-01-01")]
print(high_salary)

print("\nsales more than 75000 or order date more than 2025-01-01")
high_salary = df[(df["Sales"] > 75000) | (df["Order_Date"] > "2025-01-01")]
print(high_salary)

# =============
# SORTING 
# =============

import pandas as pd

df = pd.read_excel(r"C:\Users\VIJAY K G\Downloads\Raw Data Excel Practice.xlsx")
df = df.drop_duplicates()
df.fillna("unknown", inplace=True)

# df.sort_values(by="Sales", ascending=True, inplace=True)
# print(df)

df.sort_values(by=["Customer_Name","Sales"], ascending = [True,True], inplace=True)
print(df)

# ======================
# AGGREGATE FUNCTIONS
# ======================

import pandas as pd

df = pd.read_excel(r"C:\Users\VIJAY K G\Downloads\Raw Data Excel Practice.xlsx")
df = df.drop_duplicates()
df.fillna("unknown", inplace=True)

# avg_sales = df["Sales"].sum()
# avg_sales = df["Sales"].count()
# avg_sales = df["Sales"].max()
# avg_sales = df["Sales"].min()
# avg_sales = df["Sales"].std()

avg_sales = df["Sales"].mean()
print("Avg_Sales :", avg_sales)


# =============
# GROUPS 
# =============

import pandas as pd

df = pd.read_csv(r"C:\Users\VIJAY K G\Downloads\Sales Dataset.csv")
# df = pd.isnull(df).sum()

df.fillna(0,inplace=True)
# print(df.columns)

grouped = df.groupby("Ship Mode") ["Sales"].mean()
print(grouped)

grouped = df.groupby(["Ship Mode","Region"]) ["Sales"].mean()
print(grouped)


# ======================
# MERGING AND JOINING
# ======================

import pandas as pd

df1 = pd.DataFrame({"ID": [1, 2, 3, 4],
    "Name": ["Ram", "Shyam", "John", "Raj"]})

df2 = pd.DataFrame({"ID": [2, 3, 4, 5],
    "Salary": [25000, 30000, 35000, 40000]})


# Inner Join
inner_join = pd.merge(df1, df2, on="ID", how="inner")
print("\nINNER_JOIN:", inner_join)

# Left Join
left_join = pd.merge(df1, df2, on="ID", how="left")
print("\nLEFT_JOIN:",left_join)

# Right Join
right_join = pd.merge(df1, df2, on="ID", how="right")
print("\nRIGHT_JOIN:",right_join)

# Outer Join
outer_join = pd.merge(df1, df2, on="ID", how="outer")
print("\nOUTER_JOIN:",outer_join)

# Cross Join
cross_join = pd.merge(df1, df2, how="cross")
print("\nCROSS_JOIN:",cross_join)

# =================================
# CONCATINATE (adding two tables)
# =================================

import pandas as pd

df1 = pd.DataFrame({"ID": [1, 2, 3, 4],
    "Name": ["Ram", "Shyam", "John", "Raj"]})

df2 = pd.DataFrame({"ID": [2, 3, 4, 5],
    "Salary": [25000, 30000, 35000, 40000]})

df_concate = pd.concat([df1, df2], axis=0, ignore_index=True)
print(df_concate)

df_concate = pd.concat([df1, df2], axis=1, ignore_index=True)
print(df_concate)
