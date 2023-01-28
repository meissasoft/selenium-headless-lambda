

def lambda_handler(event, context):

    try:
        import json
        import logging
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        from selenium.webdriver.common.keys import Keys
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        result = "initiate drivers"
        print(result)

        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-gpu-sandbox')
        chrome_options.add_argument("--single-process")

        driver = webdriver.Chrome(
            '/opt/chrome/chromedriver', chrome_options=chrome_options)

        # driver.maximize_window()

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
