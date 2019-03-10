from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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


tweetBoxElem = browser.find_element_by_class_name('tweet-box')
tweetBoxElem.send_keys('this is a tweet')

