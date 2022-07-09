from selenium import webdriver

chrome_driver_path = '/home/ifilipe-lype/.local/share/chrome/chromedriver'

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('https://www.amazon.com')


# close the tab
driver.close()

# close the hole browser
driver.quit()
