from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://mail.google.com')
emailElem = browser.find_element_by_id('login-username')
emailElem = send_keys('not_my_real_email')
passwordElem = browser.find_element_by_id('login-passwd')
passwordElem.send_keys('12345')
passwordElem.submit()