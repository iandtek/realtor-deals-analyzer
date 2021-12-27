import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from pprint import pprint
import json
import time

base_url = "https://www.realtor.ca/map#ZoomLevel=4&Center=47.349129%2C-104.034233&LatitudeMax=65.93476&LongitudeMax=-34.42486&LatitudeMin=18.86870&LongitudeMin=-173.64361&view=list&Sort=1-A&PropertyTypeGroupID=2&PropertySearchTypeId=8&TransactionTypeId=2&PriceMax=1000000&UnitRange=5-0&Currency=CAD"

if __name__ == "__main__":
    driver = uc.Chrome()

    current_page = 1

    def get_links_of_current_page():
        listing_links_anchors = driver.find_elements(By.CLASS_NAME, "listingDetailsLink")
        return [elem.get_attribute('href') for elem in listing_links_anchors]

    def open_links(links):
        for link in links:
            driver.execute_script(f"window.open('{link}', '{link}');")

    def go_to_page(page):
        driver.get(base_url + "&CurrentPage=" + str(page))
        driver.refresh()

    def get_number_of_listings():
        time.sleep(5)
        return int(driver.find_element(By.ID, "listViewResultsNumVal").text)

    def scrape_listing(listing_url):
        driver.get(listing_url)
        driver.refresh()
        time.sleep(5)

        summary_items = driver.find_elements(By.CLASS_NAME, "propertyDetailsSectionContentSubCon")
        
        summary = {}

        for summary_item in summary_items:
            summary[summary_item.find_element(By.CLASS_NAME, "propertyDetailsSectionContentLabel").text] = summary_item.find_element(By.CLASS_NAME, "propertyDetailsSectionContentValue").text

        return {
            'url': listing_url,
            'address': driver.find_element(By.ID, "listingAddress").text.replace('\n', ", "),
            'price': driver.find_element(By.ID, "listingPrice").text,
            'description': driver.find_element(By.ID, "propertyDescriptionCon").text, 
            'summary': summary,
        }

    # get all listing links

    links = []

    driver.get(base_url)

    number_of_listings = get_number_of_listings()

    last_page = number_of_listings // 12
    print(last_page)
    if last_page > 50:
        last_page = 50
    while current_page <= last_page:
        print("Waiting for page to load...")
        time.sleep(5)
        print("getting links from page...")
        links.extend(get_links_of_current_page())
        try:
            print("Going to next page...")
            current_page += 1
            go_to_page(current_page)
        except Exception as e:
            print(e)
            break
        pprint(links)
        print("current_page", current_page, "last_page", last_page)

        with open('data.json', 'w') as f:
            json.dump(links, f, indent=4)

    properties = []

    for link in links:
        properties.append(scrape_listing(link))

        with open('properties.json', 'w') as f:
            json.dump(properties, f, indent=4)