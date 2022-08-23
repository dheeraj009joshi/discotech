import csv
import pandas as pd
import time
from tkinter import *
from selenium.webdriver.common.by import By
import csv
from tkinter import filedialog as fd
import tkinter as tk
from tkinter import Button, ttk
from selenium import webdriver

from function_get_google_detail import get_details
cl = None
root = Tk()
Url=Variable()

# def get_place_detail(placename):

def scrape_discotech():
    try:
        driver = webdriver.Chrome('chromedriver.exe') 
    except:
        driver = webdriver.Chrome('chromedriver') 
    driver.maximize_window()
    driver.get(f'{Url.get()}')
    venues = driver.find_elements(By.CSS_SELECTOR,".thumbnail.venue-tile.card.hoverable")

    venueLinks = []

    i=1
    while(i >= 0):
        driver.find_element(By.ID,"show-more").click()
        print(driver.find_element(By.ID,"show-more").text)
        driver.execute_script("window.scrollBy(0,100)")
        time.sleep(1)
        if driver.find_element(By.ID,"show-more").text == 'No More':
            break
       
    urls=driver.find_elements(By.XPATH,'//*[@id="results"]/div/div/div/a')
    for url in urls:
        venueLinks.append(url.get_attribute("href"))
    df=pd.DataFrame({
        "urls":venueLinks
    })
    df.to_csv(str(Url.get()).split("/")[-2]+"_urls.csv")
def scrapr_details():
    eventslinks = []
    with open(f"{f}") as csv_file:
        csv_reader=csv.reader(csv_file)
        next(csv_reader, None)
        for row in csv_reader:
            eventslinks.append(row[1])
        print(f'Processed {len(eventslinks)} lines.')

    try:
        driver = webdriver.Chrome('chromedriver.exe') 
    except:
        driver = webdriver.Chrome('chromedriver')
    eventsInfo = []
    for link in eventslinks:
        driver.get(link)
        eventimage = driver.find_elements(By.CSS_SELECTOR,'.col-sm-4.event-image-wrapper.form-group')[0].find_element(By.TAG_NAME,'a').get_attribute('href')
        eventtitle = driver.find_elements(By.CSS_SELECTOR,".event-title")[0].text
        placename = driver.find_elements(By.CSS_SELECTOR,".col-sm-8.form-group")[0].find_elements(By.TAG_NAME,'a')[0].text
        cityname = driver.find_elements(By.CSS_SELECTOR,".col-sm-8.form-group")[0].find_elements(By.TAG_NAME,'a')[1].text
        eventstartdate = driver.find_elements(By.CSS_SELECTOR,".col-sm-8.form-group")[0].find_element(By.TAG_NAME,'h4').text
        try:
            eventDescripton = driver.find_elements(By.CSS_SELECTOR,".card.form-group.clearfix").text
        except:
            eventDescripton = ''
        eventInfo = {
        'eventimage': eventimage,
        'eventtitle': eventtitle,
        'placename': placename,
        'cityname': cityname,
        'eventstartdate': eventstartdate,
        'eventDescripton':link +" " +eventDescripton
        }
        eventsInfo.append(eventInfo)
        
    len(eventsInfo)

    outfile2 = open(f'./{str(Url.get()).split("/")[-2]}.csv','w')
    writer=csv.writer(outfile2)
    writer.writerow(['eventimage', 'eventtitle','placename',  'cityname','eventstartdate', 'eventDescripton' ])
    for eve in eventsInfo:
        writer.writerow(eve)
    import pandas as pd  
    csvdata = pd.DataFrame(eventsInfo) 
    csvdata.to_csv(f'{str(Url.get()).split("/")[-2]}.csv') 
    place_add=[]
    place_type=[]
    for i in placename:
        print(f'getting info for : {i}')
        place_d=get_details(i)
        place_add.append(place_d["Address"])
        place_type.append(place_d["Types"])
    df_detail=pd.DataFrame({
        "PlaceName":placename,
        "Address":place_add,
        "PlaceType":place_type
    })
    df_detail.to_csv(f'{str(Url.get()).split("/")[-2]}_places.csv')
def select_file():
    global f
    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        )
    f=filename
    print(f)
root.geometry('500x500')
root.title("Scrape Events from google")
label_1 = Label(root, text=" Enter The Url ",font=('calibre',10, 'bold'))
label_1.place(x=90,y=90) 
label_22 = Label(root, text="Get the Urls ",font=('calibre',10, 'bold'))
label_22.place(x=90,y=130)
label_=Label(root ,text=" ",font=('calibre',10, 'bold'))
label_2 = Label(root, text=" Select the url file ",font=('calibre',10, 'bold'))
label_2.place(x=90,y=170)
    
    
Entry_1=Entry(root, font=('arial', 15), textvariable=Url, width=15).place(x=250,y=90)
button=Button(root, text ="Start",bg='brown',fg='white', command = scrape_discotech).place(x=250,y=130)
open_button_1 = ttk.Button(root,text='Open a File',command=select_file).place(x=220,y=170)

Button(root, text='Submit',width=20,bg='brown',fg='white',command=scrapr_details).place(x=220,y=250)

root.mainloop()
