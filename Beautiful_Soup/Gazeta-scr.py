from selenium import webdriver
from bs4 import BeautifulSoup
#import pandas as pd
comments = []
driver = webdriver.Firefox(executable_path='./geckodriver')
driver.get("site_adress")

content = driver.page_source
#content = open("Gazeta.html", "r")
#content = open("Training.html","r")
soup = BeautifulSoup(content,'html.parser')

#result = soup.prettify()

#print(soup.find_all())
for link in soup.find_all("div", class_ = 'comment'):
        print(link.text)