import pandas as pd 
import numpy as np 
import requests 
import bs4 
import os 
import random

"""
This function would be to extract all the links from a certain page on goodreads 
"""
def extract_book_number(n): 
    max_number = 3_500_000_000
    return random.sample(range(1, max_number), n)
    

"""
This function would be used to extract information about a books, which includes 
- title, author, rating, genre, synonpsis, year published, number of reviews
"""
def get_product_info(text): 
    raw_html = bs4.BeautifulSoup(text, features = "lxml")
    

def scrape(k):
    ...


