import pandas as pd
import requests
from bs4 import BeautifulSoup


URL = 'https://timely-sunshine-e821b3.netlify.app/'


# Loading the WebPage in Memory using requests library
page = requests.get(URL)

# Check the Status Code of the Page
page.status_code

htmlCode = page.text
print(htmlCode)

soup = BeautifulSoup(htmlCode, 'html.parser')
print(soup)

content = soup.find_all('div', attrs={'class' : 'a'})
for i in content:
  print("Div:{a}",i,end='\n\n\n\n\n')

content = soup.find('div', attrs={'class' : 'name'})
text = content.text
print(text)

content = soup.find('div', attrs={'class' : 'price'})
text = content.text.strip()
print(text)

content = soup.find('div', attrs={'class' : 'image'})
print(content)


img_tag = content.find('img')
print(img_tag)


img_src = img_tag['src']
print(img_src)

items = soup.find_all('div', class_='a')

# Lists to store extracted data
names = []
prices = []
images = []

# Loop through each item and extract details
for item in items:
    name = item.find('div', class_='name').text.strip()
    price = item.find('div', class_='price').text.strip()
    image_tag = item.find('div', class_='image').find('img')
    image_src = image_tag['src'] if image_tag else None  # Extract src attribute

    # Append data to lists
    names.append(name)
    prices.append(price)
    images.append(image_src)

# Print results
print("Names:", names)
print("Prices:", prices)
print("Images:", images)


df = pd.DataFrame({'Product_Name' : names,'MRP' : prices, 'Image_SRC': images})
df

# saving the dataframe
df.to_csv('productdetails.csv', header=True, index=False)


