from bs4 import BeautifulSoup
import requests

url = "https://coinmarketcap.com/"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

tbody = doc.tbody
trs = tbody.contents

# print("Parent:", trs[0].parent.name)
# print(list(trs[0].next_siblings))

# print(trs[0].descendant)
# print(list(trs[0].descendants))
# print((trs[0].contents))
# print(list(trs[0].children))

for tr in trs:
    coin_name = tr.contents[0]
    print(coin_name)

