import pandas as pd
product_prices =pd.Series([120,200,230,500],
                          index=['lolipop','chocolate','icecream','biscut'])
'''print (product_prices)
a=product_prices.mean()
print(a)'''
b=product_prices.median()
print(b)
'''c=product_prices.mode()
print(c)'''
print(product_prices.sum())
print (product_prices.min())
print(product_prices.max())
print(product_prices.head(-6))