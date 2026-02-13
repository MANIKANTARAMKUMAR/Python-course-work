import pandas as pd
data={'product' :["lolipop","chocolate","lolipop","biscut"],
      'brand':["candyman","cadbury","candyman","parle"],
      "price":[120,200,120,500],
      "stock":[10,30,4,38]
}
df=pd.DataFrame(data)
print(df)