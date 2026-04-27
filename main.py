import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
import time

st.title('Automating Cookie Clicker Game Project')
st.text('Hello,this is a practice project that I(Mohiuddin Mahady) did,thank you for trying it out')
st.link_button('Go to the OG Cookie Clicker game','https://orteil.dashnet.org/cookieclicker/')
#if button is clicked,then the app will start to work in a new window
if st.button('Now Start Automating Cookie Clicker'):
    driver=uc.Chrome()
    driver.get('https://orteil.dashnet.org/cookieclicker/')

    #here we will wait for the pop up of accepting cookies from the site
    got_it=WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,'.cc_btn.cc_btn_accept_all'))
    )
    #now we will click to accept the cookies from this site so the pop up doesnt mess with our code
    driver.execute_script("arguments[0].click();", got_it)
    time.sleep(2)

    #here we will wait for the pop up 'Select Language'
    WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,'langSelect-EN'))
    )
    #here we select the language english
    language=driver.find_element(By.ID,'langSelect-EN')
    language.click()
    time.sleep(1)
    #now we wait for the big cookie icon to load so we can click on it
    WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,'bigCookie'))
    )
    cookie_count=driver.find_element(By.ID,'cookies').text.split()[0]
    current_cookies=cookie_count.replace(',','')#here we replaced the comma with a blank in the integer
    import random
    while True:
        cookie=driver.find_element(By.ID,'bigCookie')
        cookie.click()
        products=driver.find_elements(By.CSS_SELECTOR,'.product.unlocked.enabled')
        if products:
            products[0].click()#now here we will click to buy granny/hand or etc to increase cookie production
        time.sleep(0.01)

    time.sleep(5)