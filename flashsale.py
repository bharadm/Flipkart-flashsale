import bs4 as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from urllib.request import Request, urlopen
from datetime import datetime as dt
#https://www.flipkart.com/account/login?ret=/

def  flash_sale_link() :
    #flash sale link
    flash_sale_link_ = str(input())
    driver.get(flash_sale_link_)
    #button click
    print("Flash sale ")
    #elem = driver.find_element_by_css_selector("_2AkmmA._2Npkh4._2MWPVK")
    try:
        element=WebDriverWait(driver,time_of_sale()).until(EC.presence_of_element_located((By.XPATH,"//*[@id="+contains+"]/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div/ul/li[2]/form/button")))
    except TimeoutException:
        print("Enter your details ")
    finally:                                           
        elem = driver.find_element_by_css_selector("._2AkmmA._2Npkh4._2kuvG8._7UHT_c")
        elem.click()
    #waitForLoad(str("//*[@id="+contains+"]/div/div[1]/div/div[1]/div[3]/div/h3/span[2]"),driver)
    
def waitForLoad(inputXPath, browser):
    try:
        Wait = WebDriverWait(browser, 5)
        Wait.until(EC.presence_of_element_located((By.XPATH, inputXPath)))
    except TimeoutException:
        print("loading took time")

def time_of_sale():
    _month= int(input("Flash sale month :"))
    _day= int(input("Flash sale day :"))           
    _hr= int(input("Flash sale Hour : "))
    _min= int(input("Flash sale Min : "))
    _sec= int(input("Flash sale Sec : "))
    now= dt.now()
    d1= dt(now.year,now.month,now.day,now.hour,now.minute,now.second)
    print(d1)
    d2= dt(now.year,_month,_day,_hr,_min,_sec)
    print(d2)
    print(str((d2-d1).total_seconds()))
    return (d2-d1).total_seconds()                   

#source code
delay=3    
#print(datetime.time(datetime.now()))
driver = webdriver.Chrome("C:/Users/Bharadwaj/Downloads/chromedriver.exe")
driver.get("https://www.flipkart.com/account/login?ret=/")

contains="container"
flash_sale_link()
