import requests
from bs4 import BeautifulSoup

def scrape_newegg(url, headers):
    """Scrape product information (name, price) from newegg page
    
    Keyword arguments:
    url -- url of product page
    headers -- user agent of user

    Return:
    title -- product title
    price -- current price of product
    """

    response = requests.get(url, headers=headers)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")

    ## Locate Item Info (title, price)
    title = soup.find("h1", class_="product-title").get_text()
    price = soup.find("div", class_="price-current").get_text()
    
    return(title, price)

        