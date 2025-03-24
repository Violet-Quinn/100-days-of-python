from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count=driver.find_element (By.CSS_SELECTOR,value="#articlecount a")
# # for time in event_times:
# #     print(time.text)
#
# event_names=driver.find_elements(By.CSS_SELECTOR,value=".event-widget li a")
# # for name in event_names:
# #     print(name.text)
#
# events={}
# for n in range(len(event_names)):
#     events[n]={
#         "time":event_times[n].text,
#         "name":event_names[n].text
#     }
#
# print(events)
print(article_count.text)
# driver.close()
driver.quit()