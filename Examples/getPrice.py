import bs4, requests

def getPrice(productURL):
    res = requests.get(productURL)

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#a-autoid-7-announce > span.a-color-base > span')
    return elems[0].text.strip() 

price = getPrice('https://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994/')
print('The price is ' + price)
