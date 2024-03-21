from selenium import webdriver

browser = webdriver.Chrome('D:/develop/chromedriver.exe')
browser.get('http://localhost:8000')

assert 'Django' in browser.page_source