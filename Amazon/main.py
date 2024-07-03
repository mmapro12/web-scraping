import requests
from bs4 import BeautifulSoup
from classes import AmazonItemController


header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0"
}

website = "https://www.amazon.com.tr"
page = "https://www.amazon.com.tr/gp/bestsellers?ref_=nav_cs_bestsellers"
response = requests.get(page, headers=header)

if str(response.status_code) != "200":
    quit(f"Problem in server: {response.status_code}")

html = response.content
soup = BeautifulSoup(html, "lxml")

items = soup.find_all("li", {"class": "a-carousel-card"})
all_links = []
for item in items:
    item_url = item.div.contents[1].div.a.get("href")
    all_links.append(website+item_url)



header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0"
}
ControlPanel = AmazonItemController()

for link in all_links:

    link_response = requests.get(link, headers=header)
    link_soup = BeautifulSoup(link_response.content, "lxml")

    name = link_soup.find("span", {"id": "productTitle"}).text
    description = link_soup.find("div", {"id": "feature-bullets"}).find("ul").contents

    try:
        price = link_soup.find("div", {"id": "corePrice_feature_div"}).div.div.span.span.text

    except AttributeError:
        price = "No In Stock"


    brand = link_soup.find("a", {"id": "bylineInfo"}).text
    item_link = link

    ControlPanel.add_item(name, description, price, brand, link)


