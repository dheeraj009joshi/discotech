import time
from selenium import webdriver

import csv
eventslinks = []
with open() as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        eventslinks.append(row)
        line_count += 1
    print(f'Processed {line_count} lines.')

driver = webdriver.Chrome(executable_path=r'') 
eventsInfo = []
for link in eventslinks:
    driver.get(link['link'])
    eventimage = driver.find_elements_by_css_selector('.col-sm-4.event-image-wrapper.form-group')[0].find_element_by_tag_name('a').get_attribute('href')
    eventtitle = driver.find_elements_by_css_selector(".event-title")[0].text
    placename = driver.find_elements_by_css_selector(".col-sm-8.form-group")[0].find_elements_by_tag_name('a')[0].text
    cityname = driver.find_elements_by_css_selector(".col-sm-8.form-group")[0].find_elements_by_tag_name('a')[1].text
    eventstartdate = driver.find_elements_by_css_selector(".col-sm-8.form-group")[0].find_element_by_tag_name('h4').text
    try:
        eventDescripton = driver.find_elements_by_css_selector(".card.form-group.clearfix")[1].text
    except:
        eventDescripton = ''
    eventInfo = {
     'eventimage': eventimage,
     'eventtitle': eventtitle,
     'placename': placename,
     'cityname': cityname,
     'eventstartdate': eventstartdate,
     'eventDescripton': eventDescripton
    }
    eventsInfo.append(eventInfo)
    
len(eventsInfo)

outfile2 = open('./dis-events-final.csv','w')
writer=csv.writer(outfile2)
writer.writerow(['eventimage', 'eventtitle','placename',  'cityname','eventstartdate', 'eventDescripton' ])
for eve in eventsInfo:
    writer.writerow(eve)
import pandas as pd  
csvdata = pd.DataFrame(eventsInfo) 
csvdata.to_csv(r'C:\Users\MSPL\Desktop\python files\dis-events-final.csv') 
