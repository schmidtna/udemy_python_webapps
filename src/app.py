import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.ikea.com/us/en/catalog/products/40268167/")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", {"id": "price1", "class": "packagePrice"})
string_price = element.text.strip() # "$109.00"

price_without_symbol = string_price[1:]

price = float(price_without_symbol)

if price < 200:
    print("The item is in budget, buy it!")
    print("The current price is {}.".format(string_price))
else:
    print("The item is too expensive, pass it up.")

#<span id="price1" class="packagePrice" style="width: 400px;">$109.00</span>

