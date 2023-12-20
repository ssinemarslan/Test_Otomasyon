#case1:
#Kullanıcı adı ve şifre alanları boş geçildiğinde uyarı mesajı olarak 
#"Epic sadface: Username is required" gösterilmelidir.
#case2:
#Sadece şifre alanı boş geçildiğinde uyarı mesajı olarak "Epic sadface: Password is required" gösterilmelidir.
#case3:
#Kullanıcı adı "locked_out_user" şifre alanı "secret_sauce" gönderildiğinde 
#"Epic sadface: Sorry, this user has been locked out." mesajı gösterilmelidir.
#case4:
#Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir. 
#Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır.
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep 

class testtry:
    #case1:
    def case1demo(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com")
        driver.maximize_window() #ekranı büyütür
        
        usernameInput = driver.find_element(By.ID,"user-name")
        usernameInput.send_keys("")
        sleep(5)
        passwordInput = driver.find_element(By.ID,"password")
        passwordInput.send_keys("")
        sleep(5)
        loginButton = driver.find_element(By.ID,"login-button")
        loginButton.click()
        sleep(5)
        
        errorMessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Username is required"
        print(f"TEST SONUCU: {testResult}")

    #case2
    def case2demo(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com")
        driver.maximize_window() #ekranı büyütür
        sleep(5)
        usernameInput = driver.find_element(By.ID,"user-name")
        usernameInput.send_keys("locked_out_user")
        sleep(5)
        passwordInput = driver.find_element(By.ID,"password") 
        passwordInput.send_keys("")
        sleep(5)
        loginButton = driver.find_element(By.ID,"login-button")
        loginButton.click()
        sleep(5)
        
        errorMessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Password is required"
        print(f"TEST SONUCU: {testResult}")

    #case3
    def case3demo(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com")
        driver.maximize_window() #ekranı büyütür
        sleep(5)
        usernameInput = driver.find_element(By.ID,"user-name")
        usernameInput.send_keys("locked_out_user")  
        sleep(5)
        passwordInput = driver.find_element(By.ID,"password") 
        passwordInput.send_keys("secret_sauce")
        sleep(5)
        loginButton = driver.find_element(By.ID,"login-button")
        loginButton.click()
        sleep(5)
        
        errorMessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"TEST SONUCU: {testResult}")

    #case4
    def case4demo(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com")
        driver.maximize_window() #ekranı büyütür
        sleep(5)
        usernameInput = driver.find_element(By.ID,"user-name")
        usernameInput.send_keys("standard_user")  
        sleep(5)
        passwordInput = driver.find_element(By.ID,"password") 
        passwordInput.send_keys("secret_sauce")
        sleep(4)
        loginButton = driver.find_element(By.ID,"login-button")
        loginButton.click()
        sleep(2)
        listOfCourses = driver.find_elements(By.CLASS_NAME, "inventory_item")
        testResult = len(listOfCourses) == 6
        print(f"Test Sonucu: {testResult}")
        sleep(5)


testClass = testtry()
testClass.case1demo()
testClass.case2demo()
testClass.case3demo()
testClass.case4demo()











