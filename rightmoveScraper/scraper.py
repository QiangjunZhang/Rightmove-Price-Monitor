from rightmoveScraper import scraperDAO as db
import bs4 as bs
import urllib.request
import urllib
import numpy as np
import re
import datetime
import random
import time
non_decimal = re.compile(r'[^\d.]+')


def pre_soup(*args):
    webs = [w for w in args]
    sauces = [urllib.request.urlopen(web).read() for web in webs]
    soups = [bs.BeautifulSoup(sauce, 'lxml') for sauce in sauces]
    return soups


def get_count(soup):
    count = soup.find('span', {'class': 'searchHeader-resultCount'}).text
    count = non_decimal.sub('', count)
    return int(count)


def get_price(soup):
    prices = soup.find_all('div', {'class': 'propertyCard-priceValue'})
    prices = [non_decimal.sub('', price.text) for price in prices]
    prices = list(filter(None, prices))
    prices = [int(price) for price in prices]
    return np.mean(prices), len(prices), prices


def get_totalpages(soup):
    pages = soup.find_all('Page')
    return pages


def get_block(soup):
    blocks = soup.find_all('div', {"class": "l-searchResult is-list"})
    return blocks


def get_info(block):

    propertyId = block.get('id')
    propertyId = int(non_decimal.sub('', propertyId))

    status = block.find('span', {"class": "propertyCard-contactsAddedOrReduced"}).text

    address = block.find('address', {"class": "propertyCard-address"}).text.replace('\n', '').replace("'", "\"")

    price = block.find('div', {"class": "propertyCard-priceValue"}).text
    price = non_decimal.sub('',price)
    price = int(price) if price else 0

    agent = block.find('span', {"class": "propertyCard-branchSummary-branchName"}).text

    numOfBeds = block.find('h2', {"class": "propertyCard-title"}).text
    numOfBeds = non_decimal.sub('', numOfBeds)
    numOfBeds = int(numOfBeds) if numOfBeds else 0

    return propertyId, status, address, agent, numOfBeds, price


if __name__ == '__main__':
    db.create_table()
    target_web = 'https://www.rightmove.co.uk/property-for-sale/find.html?locationIdentifier=POSTCODE' \
                 '%5E514951&radius=3.0&sortType=10&index=0&propertyTypes=&includeSSTC=true&mustHave=' \
                 '&dontShow=&furnishTypes=&keywords='
    soups = pre_soup(target_web)
    total_num = get_count(soups[0])

    for index in range(total_num // 24 + 1):
        if index == 42:
            break
        nextPage = target_web.replace('index=0', f'index={index*24}')
        soups = pre_soup(nextPage)
        blocks = get_block(soups[0])
        info = [get_info(block) for block in blocks]
        db.add_data_entry(info)

    print(db.get_total_num())
    db.close_connection()
