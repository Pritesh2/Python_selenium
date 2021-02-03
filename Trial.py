from selenium import webdriver


driver = webdriver.Chrome(
            executable_path="C:\\Users\\pritesh.gethewale\\PycharmProjects\\Train1\\chromedriver.exe")

driver.get('http://spo.iitk.ac.in/company_list.html')
driver.implicitly_wait(10)
driver.maximize_window()

#/html/body/div[4]/div/ul/table/tbody/tr[5]/td[2]/li
#/html/body/div[4]/div/ul/table/tbody/tr[83]
#/html/body/div[4]/div/ul/table/tbody/tr[8]/td[2]/li

rows=driver.find_elements_by_xpath('/html/body/div[4]/div/ul/table/tbody/tr')
col=driver.find_elements_by_xpath('/html/body/div[4]/div/ul/table/tbody/tr[8]/td')
print(len(rows),len(col),sep='X')

r=len(rows)
c=len(col)

for i in range(1,r+1):
    for j in range(1,c+1):
        rc=driver.find_element_by_xpath('/html/body/div[4]/div/ul/table/tbody/tr['+str(i)+']/td['+str(j)+']/li')
        print(rc.text)
driver.close()