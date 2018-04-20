import selenium,captcha,base64
from selenium import webdriver


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
password.send_keys("0521158427")
username.send_keys("96521092")
captcha_input.send_keys(cap.txt)
driver.find_element_by_id("login_btn_submit").click()