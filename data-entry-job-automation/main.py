import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

#-------------------------------------------------------------------------------
# Set up Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--user-data-dir=/Users/ultraviolet/Library/Application Support/Google/Chrome/Profile 1")
chrome_options.add_argument("--profile-directory=Profile 1")  # Change to "Profile 1" if needed
chrome_options.add_experimental_option("detach", True)

# Start Chrome with the logged-in profile
# driver = webdriver.Chrome(options=chrome_options)


#-------------------------------------------------------------------------------


header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}


responses=requests.get("https://appbrewery.github.io/Zillow-Clone/",headers=header)

data=responses.text
soup=BeautifulSoup(data,"html.parser")

all_link_elements=soup.select(".StyledPropertyCardDataWrapper a")
all_links=[link["href"] for link in all_link_elements]
print(f"There are {len(all_links)} individual listings in total.")
print(all_links)

all_address_elements=soup.select(".StyledPropertyCardDataWrapper address")
all_addresses=[address.get_text().replace("|","").strip() for address in all_address_elements]
print(f"\nAll the {len(all_addresses)} addresses look like this after cleaning\n")
print(all_addresses)

all_price_elements=soup.select(".PropertyCardWrapper span")
all_prices=[price.get_text().split()[0].replace("/mo", "").replace("+", "").strip() for price in all_price_elements if "$" in price.text]
print(f"There are {len(all_prices)} listing prices in total.")
print(all_prices)


#selenium section
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_options)

for n in range(len(all_links)):
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdil1j1w_H1AMhTqDymng3JnIcEb7iShgHTKTQTd5siqL83aA/viewform?usp=header")
    time.sleep(2)

    address=driver.find_element(by=By.XPATH,value="/html/body/div/div[3]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    price=driver.find_element(by=By.XPATH,value="/html/body/div/div[3]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    link=driver.find_element(by=By.XPATH,value="/html/body/div/div[3]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
    submit_button=driver.find_element(by=By.XPATH,value="/html/body/div/div[3]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span")

    address.send_keys(all_addresses[n])
    price.send_keys(all_prices[n])
    link.send_keys(all_links[n])
    submit_button.click()



