import selenium,captcha,base64
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from food import food
love_list = ["جوجه کباب","زرشك پلو با مرغ","سبزی پلو با ماهی","چلو کباب کوبیده"]
driver = selenium.webdriver.Chrome()
driver.get("http://stu.iust.ac.ir/loginpage.rose")
username = driver.find_element_by_id("j_username")
password = driver.find_element_by_id("j_password")
captcha_input =driver.find_element_by_id("captcha_input")
ele_captcha = driver.find_element_by_id("captcha_img")

# get the captcha as a base64 string
img_captcha_base64 = driver.execute_async_script("""
    var ele = arguments[0], callback = arguments[1];
    ele.addEventListener('load', function fn(){
      ele.removeEventListener('load', fn, false);
      var cnv = document.createElement('canvas');
      cnv.width = this.width; cnv.height = this.height;
      cnv.getContext('2d').drawImage(this, 0, 0);
      callback(cnv.toDataURL('image/jpeg').substring(22));
    }, false);
    ele.dispatchEvent(new Event('load'));
    """, ele_captcha)

# save the captcha to a file
with open(r"captcha.jpg", 'wb') as f:
    f.write(base64.b64decode(img_captcha_base64))
cap = captcha.cap("captcha.jpg")
password.send_keys("0371774616")
username.send_keys("96521011")
captcha_input.send_keys(cap.txt)
driver.find_element_by_id("login_btn_submit").click()
driver.find_element_by_xpath('//img[@alt="/res?id=reserve48x48.png&dl=false&uId=132993"]').click()
driver.find_element_by_id("nextWeekBtn").click()
foods = []
# priorities = {}
# input()
# driver.find_element_by_id('nextWeekBtn').click()
# lst = []
# for i in range(21):
#         f=driver.find_element_by_id('foodNameSpan'+str(i))
#         if '1' in f.text:
#             lst.sort(key = lambda x:priorities[x.text.split('|')[-1]])
#             try:
#                 lst[0].click()
#             except:
#                 pass
#             lst=[f]
#         else:
#             lst.append(f)
# lst.sort(key = lambda x:priorities[x.text.split('|')[-1]])
# try:
#     lst[0].click()
# except:
#     pass
for i in range(15):
    try:
        name = driver.find_element_by_id("foodNameSpan"+str(i)).text
        element_to_hover_over = driver.find_element_by_id("foodNameSpan"+str(i))
        hover = ActionChains(driver).move_to_element(element_to_hover_over)
        hover.perform()
        price = driver.find_element_by_id("foodPriceTooltip"+str(i)).text.split()[1]
        foods.append(food(price,name,i))

    except:
        break
day = []
week_foods = []
for food in foods:
    if "1" in food.name and int(food.id)>0:
        week_foods.append(day)
        day = []
    print(food.name)
    day.append(food)
week_foods.append(day)
def select(foods,love_list):
    selected = []
    for love in love_list:
        for day in foods:
            for food in day:
                if love in food.name:
                    selected.append(food)
                    foods.remove(day)
    for day in foods:
        day = sorted(day, key=lambda h: (h.price))
        selected.append(day[0])
    return selected
select_list = select(week_foods,love_list)
for item in select_list:
    driver.find_element_by_id("userWeekReserves.selected" + str(item.id)).click()
driver.find_element_by_id("doReservBtn").click()

# else:
            #     day = sorted(day, key=lambda h: (h.price))
            #     # driver.find_element_by_id("userWeekReserves.selected"+str(food.id)).click()