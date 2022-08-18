import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path=r'chromedriver.exe') 
driver.maximize_window()
driver.get('https://app.discotech.me/los-angeles/venues')
venues = driver.find_elements_by_css_selector(".thumbnail.venue-tile.card.hoverable")

venueLinks = []

for venue in venues:
    venueLinks.append(venue.find_element_by_tag_name('a').get_attribute('href'))
    

eventlinks = []
for venueLink in venueLinks:
    driver = webdriver.Chrome(executable_path=r'chromedriver.exe') 
    driver.get(venueLink)
    try:
        driver.execute_script("window.scrollBy(0,250)")
        i = 1
        while(i >= 0):
            driver.find_element_by_id("show-more").click()
            print(driver.find_element_by_id("show-more").text)
            driver.execute_script("window.scrollBy(0,100)")
            time.sleep(10)
            if driver.find_element_by_id("show-more").text == 'No More':
                break
    except:
        print(venueLink)
    
    events = driver.find_elements_by_css_selector('.event-box.tile-view')
    for event in events:
        eventlinks.append(event.find_element_by_tag_name('a').get_attribute('href'))
    
    print(len(eventlinks))
    driver.close()
eventlinks[2]

import csv

outfile = open(r'C:\Users\MSPL\Desktop\python files\dis-events.csv','w')
writer=csv.writer(outfile)
writer.writerow(['link'])
for eve in eventlinks:
    writer.writerow([eve])

