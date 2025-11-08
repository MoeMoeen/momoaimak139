import pandas as pd


data = {
    "name": ["Alice", "Bob", "Charlie", "Diana"],
    "age": [25, 30, 35, 40],
    "city": ["London", "Paris", "Berlin", "Rome"]
}

df = pd.DataFrame(data)
print("df is:\n", df)

print("df['name'] is:\n", df["name"])

df_filtered = df[df["age"] > 30]
print("\ndf filtered where age > 30 is:\n", df_filtered)

print("\ndf.loc[1] is:\n", df.loc[1])
print("\ndf.iloc[2] is:\n", df.iloc[2])

#       name  age    city
# 0    Alice   25  London
# 1      Bob   30   Paris
# 2  Charlie   35  Berlin
# 3    Diana   40    Rome



# books=pd.DataFrame({
# "title": ["Harry Potter", "Anne of Green Gables", "The birth of a killer"],
# "price": [98000, 76000, 89000],
# "author": ["J.K. Rowling", "L.M. Montgomery", "Darren Shan"]
# }, index=["b1", "b2", "b3"])

# print(books)

# print("*"*40)

# # result_loc = books.loc[["title"]]

# result_iloc= books.iloc[ [0, 2] , [2]]

# print("\nResult using loc:")
# # print(result_loc)

# print("\nResult using iloc:")
# print(result_iloc)

data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data, index=['x', 'y', 'z'])
print(f"\ndf is:\n{df}")
# df is:
#    A  B
# x  1  4
# y  2  5
# z  3  6

# 1. Select the row labeled 'y' and the column labeled 'B'
value = df.loc['y', 'B']
print(f"\nvalue is: {value}")
# Result: 5

# 2. Select rows from 'x' to 'z' (inclusive) and columns 'A' and 'B'
subset = df.loc['x':'z', ['A', 'B']]
print(f"\nsubset is:\n{subset}")
# Result: the entire DataFrame


df = pd.DataFrame({
    "product": ["A", "B", "C", "D"],
    "price":   [10, 15, 7, 25],
    "quantity":[3, 4, 10, 2]
})
print("df is:\n", df)


df["revenue"] = df["price"] * df["quantity"]
print(df)
total_revenue = df["revenue"].sum()
print(f"\nTotal revenue is: {total_revenue}")

def discount(p):
    if p > 10:
        return p * 0.9
    else:
        return p

df["discounted_price"] = df["price"].apply(discount)
print("\ndf is:\n", df)

df["brand"] = ['X', 'Y', 'X', 'Z']
print("df is:\n", df)

df = df.assign(
    cost = df["price"] * 0.6,                      # assume cost = 60% of price
    profit = df["revenue"] - (df["price"] * df["quantity"] * 0.6)
)
print("df is:\n", df)

print("df['price'] > 10 is:\n", df["price"] > 10)
df_high_price = df[df["price"] > 10]
print("\ndf with price > 10 is:\n", df_high_price)

my_series = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
# my_series = pd.Series([10, 20, 30])
print("my_series is:\n", my_series)

df[df["product"].isin(["A", "C"])]
print("\ndf with products A and C is:\n", df[df["product"].isin(["A", "C"])])


df["category"] = ["Food", "Food", "Toy", "Toy"]
print("df is:\n", df)
grouped = df.groupby("category")["revenue"].sum()
print("\nTotal revenue by category is:\n", grouped)
grouped = df.groupby("category")["revenue"].agg(['sum', 'mean'])
print("\nTotal and average revenue by category is:\n", grouped)
grouped = df.groupby("category")["revenue"].mean()
print("\nAverage revenue by category is:\n", grouped)

grouped = df.groupby("category").agg(
    total_revenue=("revenue", "sum"),
    avg_price=("price", "mean"),
    total_quantity=("quantity", "sum")
).reset_index()

print("\nGrouped df is:\n", grouped)