from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')  # Runs Chrome in headless mode
options.add_argument('--no-sandbox')  # Bypass OS security model, required in some environments
options.add_argument('--disable-dev-shm-usage')  # Overcome limited resource problems
options.add_argument('--disable-gpu')  # Applicable to headless chrome since Chrome 61

driver = webdriver.Chrome(options=options)

driver.get("https://www.google.com")
driver.implicitly_wait(10)
driver.quit()

# Test with Firefox