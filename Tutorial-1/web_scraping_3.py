from bs4 import BeautifulSoup
import requests

url = "https://coinmarketcap.com/"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

tbody = doc.tbody
trs = tbody.contents
# print("len:", len(trs))

# print("Parent:", trs[0].parent.name)
# print(list(trs[0].next_siblings))

# print(trs[0].descendant)
# print(list(trs[0].descendants))
# print((trs[0].contents))
# print(list(trs[0].children))

prices = {}
for tr in trs[:10]:
    name, price = tr.contents[2:4]    
    fixed_name = name.p.string
    fixed_price = price.a.string

    prices[fixed_name] = fixed_price

print(prices)