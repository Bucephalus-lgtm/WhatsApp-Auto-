from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from time import sleep
from selenium.common.exceptions import NoSuchElementException



driver_location = '' #Insert driver location here
print("Enter number of users")
n = int(input())

users = []

for i in range(n):
    print(f"Enter name of {i+1}'th user")
    users.append(input())



driver = webdriver.Chrome(driver_location)
driver.get("https://web.whatsapp.com")
sleep(10)
for username in users:
    driver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[2]/div/span').click()

    driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div[1]/div/label/div/div[2]').send_keys(username)

    sleep(5)

    
    try: 
        address = '//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div[2]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/span/span'
        driver.find_element_by_xpath(address).click()
    except NoSuchElementException:
        address = '//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div[2]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/div/span'
        driver.find_element_by_xpath(address).click()
        
        
   
    sleep(5)

    message_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')


    message_box.send_keys('"Hello! This is an automated message"')
    message_box.send_keys(u'\ue007')
    sleep(2)

    message_box.send_keys('Sent using a WhatsApp bot, that Gaurav has built')
    message_box.send_keys(u'\ue007')
    sleep(2)

driver.quit()








