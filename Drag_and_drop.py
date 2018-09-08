from selenium import webdriver
import time
from selenium.webdriver import ActionChains

#Set-up
driver = webdriver.Chrome()
action_chains = ActionChains(driver)
driver.maximize_window()

#Step 1: Go to url : http://quickfuseapps.com/
driver.get("http://quickfuseapps.com/")
time.sleep(5)

#Step 2: Click on Create an App
driver.find_elements_by_id("link-create")[0].click()
time.sleep(5)

#Step 3: You will land up on default page and then click “Lets’ get started”
driver.find_element_by_xpath('//button[contains(text(), "Let\'s get started!")]').click()
time.sleep(2)

#Step 4: Create a new page and give it a name
driver.find_elements_by_id("add-page")[0].click()
driver.find_elements_by_class_name('submitonenter')[0].send_keys("hitesh_test")
driver.find_elements_by_xpath('//button[contains(text(), "Create")]')[1].click()

#Step 5: Click on “Messaging” group appearing on the left pane under MODULES
driver.find_elements_by_partial_link_text("Messaging")[0].click()

#Step 6: Drag component “Send an SMS” to the main app page &amp; join the line from start acting as connector
element = driver.find_elements_by_class_name('module-item-green')[2]
time.sleep(1)
action_chains.drag_and_drop_by_offset(element, 500, 0).perform()
time.sleep(2)

node1 = driver.find_elements_by_class_name('syn-node-active')[1]
time.sleep(2)
target1 = driver.find_elements_by_class_name('syn-receptor-draggable')[0]
time.sleep(2)
action_chains.drag_and_drop(node1, target1).perform()
time.sleep(3)

#Step 7: Fill the details of Phone Number and Message text
driver.find_elements_by_name('phone_constant')[0].send_keys("1234567890")
time.sleep(1)
driver.find_elements_by_name('message_phrase[]')[0].send_keys("Hello Hitesh")
time.sleep(1)

#Step 8:Drag component “Send an email” from the left module and join line from “Not sent” output port.Also fill all the details of the mail as shown
Send_an_email = driver.find_elements_by_class_name('module-item-green')[1]
time.sleep(1)
action_chains.drag_and_drop_by_offset(Send_an_email, 700, 200).perform()
time.sleep(2)
node2 = driver.find_elements_by_class_name('syn-node-active')[2]
time.sleep(1)
target2 = driver.find_elements_by_class_name('syn-receptor-draggable')[3]
time.sleep(1)
action_chains.drag_and_drop(node2, target2).perform()
time.sleep(2)
driver.find_elements_by_name('smtp_url')[0].send_keys("hiteshtest@smtp.com")
driver.find_elements_by_name('port')[0].send_keys("1234")
driver.find_elements_by_name('username')[0].send_keys("hitesh")
driver.find_elements_by_name('password')[0].send_keys("Welcome@123")
driver.find_elements_by_name('from_constant')[0].send_keys("hiteshbisht@hello.com")
driver.find_elements_by_name('to_constant')[0].send_keys("hiteshbisht@hello1.com")
driver.find_elements_by_name('subject_constant')[0].send_keys("Welcome@123")
driver.find_elements_by_name('cc_constant')[0].send_keys("Welcome@123")

#Step 9: Click on component “Basic” on left Module and drag “Exit App” joining to “Sent” output port of Sent an sms box
driver.find_elements_by_css_selector('span.ui-icon-triangle-1-e')[4].click()
time.sleep(2)
exit1 = driver.find_elements_by_css_selector('span.ui-icon-alert')[0]
time.sleep(1)
action_chains.drag_and_drop_by_offset(exit1, 200, 200).perform()
time.sleep(2)
node2 = driver.find_elements_by_class_name('syn-node-active')[5]
time.sleep(1)
target2 = driver.find_elements_by_class_name('syn-receptor-draggable')[6]
time.sleep(1)
action_chains.drag_and_drop(node2, target2).perform()
time.sleep(2)

#Step 10: Similarly, Join all the open output ports of “Send an Email” to Exit app by dragging
driver.find_elements_by_css_selector('span.ui-icon-triangle-1-e')[3].click()
time.sleep(2)
exit1 = driver.find_elements_by_css_selector('span.ui-icon-alert')[0]
time.sleep(1)
action_chains.drag_and_drop_by_offset(exit1, 500, 400).perform()
time.sleep(2)
node2 = driver.find_elements_by_class_name('syn-node-active')[9]
time.sleep(1)
target2 = driver.find_elements_by_class_name('syn-receptor-draggable')[9]
time.sleep(1)
action_chains.drag_and_drop(node2, target2).perform()
time.sleep(2)

#Tear-down
driver.quit()