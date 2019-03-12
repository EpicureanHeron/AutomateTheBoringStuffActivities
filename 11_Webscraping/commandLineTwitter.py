from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



import sys

tweet = ' '. join(sys.argv[1:])

browser = webdriver.Chrome()

print(tweet)

browser.get('https://twitter.com/login?lang=en')
emailElem = browser.find_element_by_class_name('js-username-field')
emailElem.click()
emailElem.send_keys('email@gmail.com')
passwordElem = browser.find_element_by_class_name('js-password-field')
passwordElem.click()
passwordElem.send_keys('password')
passwordElem.send_keys(Keys.ENTER)

tweetElem = browser.find_element_by_id('global-new-tweet-button')
tweetElem.click()


# tweetBoxElem = browser.find_element_by_class_name('modal-body')
# tweetBoxElem.click()
# tweetBoxElem.send_keys(tweet)

timeout = 5
element_present = EC.presence_of_element_located((By.CSS_SELECTOR, 'div.modal'))
WebDriverWait(browser, timeout).until(element_present)
print('success!')
tweetBoxElem = browser.find_element_by_id('Tweetstorm-dialog-dialog')
messageArea = tweetBoxElem.send_keys(Keys.TAB)
#tweetBoxElem.click()

messageArea.send_keys(tweet)