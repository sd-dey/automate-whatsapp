import schedule
from selenium import webdriver

drive = webdriver.Chrome("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\chromedriver.exe")
drive.get("https://web.whatsapp.com/")
input("Press ENTER after scanning the code")

def message():
  name="Saptashwa"
  msg="Good Night"
  count=int(1)

  user=drive.find_element_by_xpath('//span[@title = "{}"]'.format(name))
  user.click()

  msg_box=drive.find_element_by_class_name('_3uMse')

  for i in range(count):
	     msg_box.send_keys(msg)
	     button=drive.find_element_by_class_name('_1U1xa')
	     button.click()

schedule.every(2).seconds.do(message)

while True:
	schedule.run_pending()

drive.quit()