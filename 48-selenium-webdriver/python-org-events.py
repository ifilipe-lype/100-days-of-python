from selenium import webdriver

chrome_driver_path = '/home/ifilipe-lype/.local/share/chrome/chromedriver'

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('https://www.python.org')

event_items = driver.find_elements(by='css selector', value='.medium-widget.event-widget.last ul.menu li')

events_dic = {}

for i, event_item in enumerate(event_items):
    event_date = event_item.find_element(by='tag name', value='time').get_attribute("datetime")
    event_name = event_item.find_element(by='tag name', value='a').text

    events_dic[i] = { "name": event_name, "date": event_date }

print(events_dic)

# close the tab
driver.close()

# close the hole browser
driver.quit()
