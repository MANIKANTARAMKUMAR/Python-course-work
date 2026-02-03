import pandas as pd

prices=[2999, 15999, 52999, 4999, 1999]
products=["Wireless Earbuds", "Smartphone", "Laptop", "Smartwatch", "Bluetooth Speaker"]

product_prices = pd.Series(prices,index=products)
print(product_prices)


print("Mean:", product_prices.mean())


print("Sum:", product_prices.sum())


print("Max:", product_prices.max())


print("Min:", product_prices.min())


print("Head (First 3 Elements):\n", product_prices.head(2))


print("Tail (Last 2 Elements):\n", product_prices.tail(3))


print("Apply (Adding 18% GST):\n", product_prices.apply(lambda x: f'₹{x+(x*0.18)}'))


print("Map (Formatting as Currency):\n", product_prices.map(lambda x: f"₹{x}.00"))


print("Sort by Values:\n", product_prices.sort_values())


print("Sort by Index:\n", product_prices.sort_index())


print(product_prices.sort_index(ascending=False))


print("Value Counts:\n", product_prices.value_counts())


data = {
"Product": ["Wireless Earbuds", "Smartphone", "Laptop", "Smartwatch", "Bluetooth Speaker"],
"Brand": ["SoundMax", "TechNova", "ByteCore", "TimeTrack", "EchoBoom"],
"Price": [2999, 15999, 52999, 4999,5678],
"Stock": [50, 30, 20, 40,60],
"BestSeller":[True,False,False,True,True]
}
df = pd.DataFrame(data)
print(df)



print("Shape of DataFrame:", df.shape)

print("Columns in DataFrame:", df.columns)

