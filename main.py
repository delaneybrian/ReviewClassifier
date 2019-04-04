from scraper import get_and_clean_review_data
from numerizer import create_tfidf_representation

bar_start_page = "http://mlg.ucd.ie/modules/yalp/bars_list.html"
restaurant_start_page = "http://mlg.ucd.ie/modules/yalp/restaurants_list.html"

def __main__():
    cleaned_bar_data = get_and_clean_review_data(bar_start_page)
    cleaned_restaurant_data = get_and_clean_review_data(restaurant_start_page)
    create_tfidf_representation(cleaned_bar_data)

__main__()