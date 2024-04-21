from selenium import webdriver

# Test with Chrome
driver = webdriver.Chrome()
driver.get("https://www.google.com")
driver.implicitly_wait(10)
driver.quit()

# Test with Firefox