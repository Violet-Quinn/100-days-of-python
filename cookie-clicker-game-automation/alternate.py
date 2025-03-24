#failed
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize WebDriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

# Store the cookie element once
cookie = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "cookie")))

# Building details (ID and max limit)
buildings = {
    "buyTime machine": 10,
    "buyPortal": 10,
    "buyAlchemy lab": 25,
    "buyShipment": 20,
    "buyMine": 7,
    "buyFactory": 10,
    "buyGrandma": 17,
    "buyCursor": 21,
}

game_end = time.time() + 60 * 5  # Run for 5 minutes
timeout = time.time() + 5

while time.time() < game_end:
    cookie.click()

    if time.time() > timeout:
        for building_id, limit in buildings.items():
            try:
                building = driver.find_element(By.ID, building_id)
                amount_text = building.find_element(By.CLASS_NAME, "amount").get_attribute("textContent")

                amount = int(amount_text) if amount_text.isdigit() else 0
                if amount < limit:
                    building.click()
                    timeout = time.time() + 5  # Reset timeout only on successful purchase

            except Exception:  # Catch NoSuchElementException, StaleElementReferenceException, etc.
                continue

# Get final cookies per second
cookie_per_s = driver.find_element(By.ID, "cps").text
print(f"Cookies per second: {cookie_per_s}")

# Optionally close the driver
driver.quit()
