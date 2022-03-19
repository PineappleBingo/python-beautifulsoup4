from bs4 import BeautifulSoup
import requests

url = "https://www.newegg.com/gigabyte-geforce-rtx-3080-ti-gv-n308tgaming-oc-12gd/p/N82E16814932436?Item=N82E16814932436&cm_sp=Homepage_TRENDINGNOW-_-P2_14-932-436-_-03182022"

result = requests.get(url)
# print(result.text)

doc = BeautifulSoup(result.text, "html.parser")
# print(doc.prettify())

prices = doc.find_all(text="$")
# print(prices)
parent = prices[0].parent
# print(parent)
strong = parent.find("strong")
print(strong.string)