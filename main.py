import requests
from bs4 import BeautifulSoup
import re

start_page = "http://mlg.ucd.ie/modules/yalp/bars_list.html"
base_address = "http://mlg.ucd.ie/modules/yalp/"

def get_page(url):
    try:
        r = requests.get(url)
        if(r.status_code == 200):
            return r.content
        else:
            return None
    except Exception as e:
        print("Error Scraping {0} : {1}".format(url, e))


def scrape_location_links(soup):
    location_links = soup.find_all('a')

    full_location_links = []
    for location_link in location_links:
        full_location_link = base_address + location_link['href']
        full_location_links.append(full_location_link)

    return full_location_links

def scrape_reviews_for_location_link(location_link):
    content = get_page(location_link)
    soup = BeautifulSoup(content, features='html.parser')

    reviews = soup.find_all('div', 'review')
    for review in reviews:
        extract_review_data(review)

def extract_review_data(review_soup):
    review_text = review_soup.find('p', 'text').getText()
    review_score_img = review_soup.find('img')

    review_score = extract_review_score_from_image(review_score_img)
    review_class = num_stars_to_postive_or_negative(review_score)

    print(review_class, review_text)

def extract_review_score_from_image(review_score_img):
    return re.findall(r'stars-([0-9]).png', review_score_img['src'])[0]

def num_stars_to_postive_or_negative(num_stars):
    num_stars = int(num_stars)
    if(num_stars > 0 and num_stars <= 3):
        return 0
    elif(num_stars > 3 and num_stars <= 5):
        return 1
    else:
        raise Exception("Invalid Review Rating")

content = get_page(start_page)
soup = BeautifulSoup(content, features='html.parser')
location_links = scrape_location_links(soup)

for location_link in location_links:
    scrape_reviews_for_location_link(location_link)
