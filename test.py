from selenium import webdriver

# Указываем полный путь к geckodriver.exe на вашем ПК.
driver = webdriver.Chrome('C:\\Users\\sakunov.a\\Downloads\\drivers\\chromedriver.exe')
driver.get("http://www.google.com")