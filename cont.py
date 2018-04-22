from selenium import webdriver

priorities = {}
driver = webdriver.Chrome('chromedriver.exe')
input()
#driver.get("http://stu.iust.ac.ir/loginpage.rose")
driver.find_element_by_id('nextWeekBtn').click()
lst = []
for i in range(21):
    try:
        f=driver.find_element_by_id('foodNameSpan'+str(i))
        if '1' in f.text:
            lst.sort(key = lambda x:priorities[x.text.split('|')[-1]])
            try:
                lst[0].click()
            except:
                pass
            lst=[f]
        else:
            lst.append(f)
    except:
        break
lst.sort(key = lambda x:priorities[x.text.split('|')[-1]])
try:
    lst[0].click()
except:
    pass

