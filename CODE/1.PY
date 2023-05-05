from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Edge()

driver.get('https://htdecl.chinaport.gov.cn/htdeclweb/home/pages/healthDeclare/declare.html')
time.sleep(0.2)

CLOSE = driver.find_element(By.CSS_SELECTOR,'#modal_1 > button').click()
time.sleep(0.2)

AGREE = driver.find_element(By.ID,'alSt_1').click()
time.sleep(0.2)

HKORMC = driver.find_element(By.ID,'fromMacao_0').click()
time.sleep(0.2)

EXOREN = driver.find_element(By.ID,'iEFlag_I').click()
time.sleep(0.2)

NAME = driver.find_element(By.ID,'name')
NAME.send_keys('陈起明')
time.sleep(0.2)

GENDER = driver.find_element(By.ID,'sex_m').click()
time.sleep(0.2)

NANDR = driver.find_element(By.ID,'passNaText')
NANDR.send_keys('中国')
time.sleep(0.1)
S1 = driver.find_element(By.CSS_SELECTOR,'#passengerformtmpl > div:nth-child(7) > div.inline-item.inline-wrapper > div.inline-item > div > div > button')
time.sleep(0.1)
ActionChains(driver).move_to_element(S1).move_by_offset(0,30).click().perform()
time.sleep(0.2)

OCC = driver.find_element(By.ID,'jobTypeText')
OCC.send_keys('其他运输工具工作人员 Other transport staff')
time.sleep(0.1)
S2 = driver.find_element(By.CSS_SELECTOR,'#passengerformtmpl > div:nth-child(8) > div.inline-item.inline-wrapper > div.inline-item > div > div > button')
time.sleep(0.1)
ActionChains(driver).move_to_element(S2).move_by_offset(0,30).click().perform()
time.sleep(0.2)

BRID = driver.find_element(By.ID,'birthDate')
BRID.send_keys('2000-06-29')
time.sleep(0.2)

PSPT = driver.find_element(By.ID,'certTypeText')
PSPT.send_keys('护照 Passport')
time.sleep(0.1)
S3 = driver.find_element(By.CSS_SELECTOR,'#passengerformtmpl > div:nth-child(11) > div.inline-item.inline-wrapper > div.inline-item > div > div > button')
time.sleep(0.1)
ActionChains(driver).move_to_element(S3).move_by_offset(0,30).click().perform()
time.sleep(0.2)

PSPN = driver.find_element(By.ID,'certNo')
PSPN.send_keys('P00000000')
time.sleep(0.2)

IMO = driver.find_element(By.ID,'flightNo')
IMO.send_keys('9809999')
time.sleep(0.2)

SEATNO = driver.find_element(By.ID,'seatNo')
SEATNO.send_keys('1')
time.sleep(0.2)

PHO1 = driver.find_element(By.ID,'phoneType_0').click()
time.sleep(0.2)

PHO1NO = driver.find_element(By.ID,'telephone')
PHO1NO.send_keys('+8666666666')
time.sleep(0.2)

OTHERCONT1 = driver.find_element(By.ID,'otherContact1')
OTHERCONT1.send_keys('陈起明')
time.sleep(0.2)

OTHERCONT1 = driver.find_element(By.ID,'otherContact2')
OTHERCONT1.send_keys('13777777777')
time.sleep(0.2)