from selenium import webdriver

url = "https://www.nytimes.com/"

driver = webdriver.Chrome("./chromedriver.exe")
driver.get(url)
elements = driver.find_elements_by_class_name("e1lsht870")

titles = [a.text for a in elements if (a.text != "")]

print(titles)