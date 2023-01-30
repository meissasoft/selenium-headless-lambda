from selenium import webdriver
from tempfile import mkdtemp
from selenium.webdriver.common.by import By
import json
import logging
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def handler(event=None, context=None):
    try:
        options = webdriver.ChromeOptions()
        options.binary_location = '/opt/chrome/chrome'
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1280x1696")
        options.add_argument("--single-process")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-dev-tools")
        options.add_argument("--no-zygote")
        options.add_argument(f"--user-data-dir={mkdtemp()}")
        options.add_argument(f"--data-path={mkdtemp()}")
        options.add_argument(f"--disk-cache-dir={mkdtemp()}")
        options.add_argument("--remote-debugging-port=9222")
        driver = webdriver.Chrome("/opt/chromedriver",
                                options=options)

        driver.set_page_load_timeout(30)

        result = "browse website"
        print(result)

        driver.get("https://google.com")
        result = "google get"
        print(result)

        searchbar = driver.find_element(By.NAME, "q")
        result = "find element in google"
        print(result)

        searchbar.clear()
        searchbar.send_keys('Starbucks 1912 pike place')
        searchbar.send_keys(Keys.ENTER)

        result = "get the phone number and screenshot"
        print(result)

        resultFromChrome = driver.find_element(
            By.XPATH, '//*[@id="result-stats"]').text

        print(resultFromChrome)

        result = "exit driver"
        print(result)

        driver.quit()

    except Exception as e:
        result = str(e)
        print(result)
        result = '(!) Result not found: ' + result
        resultFromChrome = result

    print(result)

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "selenium run successfully",
                "result": resultFromChrome
            }
        ),
    }