import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# Selenium WebDriver fixture for Chrome
@pytest.fixture(scope="function")
def chrome_driver():
    # Chrome WebDriver options
    service = Service("/usr/local/bin/chromedriver")
    options = Options()
    options.add_argument('--no-sandbox')  # Required in some environments
    options.add_argument('--disable-dev-shm-usage')  # Overcome resource limitations
    # Uncomment the following for headless mode
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')

    # Initialize Chrome WebDriver
    driver = webdriver.Chrome(service=service, options=options)
    
    yield driver  # Yield the driver instance for use in tests
    
    # Cleanup code
    driver.quit()  # Close the driver after the test is done

# A simple test case using the WebDriver fixture
def test_google(chrome_driver):
    chrome_driver.get("https://www.google.com")
    chrome_driver.implicitly_wait(10)  # Wait time for page to load
    
    # Verify that the Google page loaded correctly
    assert "Google" in chrome_driver.title, "Google page did not load as expected"
