from selenium import webdriver
userStr = 'your_ID'
passStr = 'your_Password'
browser = webdriver.Chrome()
browser.get('https://www.topcashback.co.uk/logon?PageRequested=https%3a%2f%2fwww.topcashback.co.uk%2fHome')
email = browser.find_element_by_id('txtEmail')
email.send_keys(userStr)
password = browser.find_element_by_id('ctl00_GeckoOneColPrimary_Login_txtPassword')
password.send_keys(passStr)
loginButton = browser.find_element_by_css_selector('#Loginbtn').send_keys('\n')
#wait = webdriver.wait(browser,10)
#loginButton.click()

