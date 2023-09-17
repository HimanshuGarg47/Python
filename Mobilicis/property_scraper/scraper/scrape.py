# scraper_app/scrape.py

import os
import django
from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime
from scraper.models import Property
from selenium.webdriver.chrome.service import Service

# service = Service()
# options = webdriver.ChromeOptions()

# Set up Django environment
def scraping():
    # os.environ.setdefault("DJANGO_SETTINGS_MODULE", "property_scraper.settings")
    # django.setup()
    #os.environ['PATH'] += '/mnt/d/Downloads/chromedriver_win32'
    # Configure Selenium WebDriver (you may need to download the appropriate driver)
    # service = Service()
    # options = webdriver.ChromeOptions()
    driver = webdriver.Chrome() #service=service, options=options)

    # Define cities and their respective localities
    cities_and_localities = [
        {"city": "Hyderabad", "locality": "Banajara Hills"},
        # Add more cities and localities here
    ]

    # Scrape data from 99acres.com
    for item in cities_and_localities:
        city = item["city"]
        locality = item["locality"]
        url = f"https://www.99acres.com/search/property/buy/{city.lower()}-all?city=38&preference=S&area_unit=1&res_com=R"
        print(f"url => {url}")
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        print(f'soup => {soup}')
        # Loop through property listings
        for listing in soup.find_all('div', class_='projectTuple__cardWrap  '):
            property_name = listing.find('a', id_='srp_tuple_property_title').text.strip()
            property_cost = listing.find('td', id='srp_tuple_price').text.strip()
            property_type = listing.find('td', class_='propType').text.strip()
            property_area = listing.find('td', id_='srp_tuple_primary_area').text.strip()
            property_link = listing.find('a', class_='projectTuple__projectName')['href']

            # Save data to the database
            Property.objects.create(
                name=property_name,
                cost=property_cost,
                property_type=property_type,
                area=property_area,
                locality=locality,
                city=city,
                property_link=property_link
            )

    # Quit the Selenium WebDriver
    driver.quit()
