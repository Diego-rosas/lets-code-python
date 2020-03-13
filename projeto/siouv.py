import selenium
from selenium import webdriver
from bs4 import BeautifulSoup

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(r'/chromedriver.exe')

site = 'http://www.google.com'

driver.get(site)



