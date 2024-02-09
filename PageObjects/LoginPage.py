from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class LoginClass:
    Text_Email_Xpath = "//input[@id='Email']"
    Text_Password_Xpath = "//input[@id='Password']"
    Click_LoginButton_Xpath = "//button[@type='submit']"
    Click_LogoutButton_Xpath = "//a[normalize-space()='Logout']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)   # task poll frequency # default poll frequency
        # total 10... if the element visible in 3 sec then it will not take complete 10 sec for next operation

    def Enter_Email(self, email):
        self.driver.find_element(By.XPATH, self.Text_Email_Xpath).clear()
        self.driver.find_element(By.XPATH, self.Text_Email_Xpath).send_keys(email)

    def Enter_Password(self, password):
        self.driver.find_element(By.XPATH, self.Text_Password_Xpath).clear()
        self.driver.find_element(By.XPATH, self.Text_Password_Xpath).send_keys(password)

    def Click_Login(self):
        self.driver.find_element(By.XPATH, self.Click_LoginButton_Xpath).click()

    def Click_Logout(self):
        try:
            self.wait.until(expected_conditions.presence_of_element_located((By.XPATH,self.Click_LogoutButton_Xpath)))
            self.driver.find_element(By.XPATH, self.Click_LogoutButton_Xpath).click()
        except:
            pass

    def Verify_Login_Stauts(self):
        try:
            self.driver.find_element(By.XPATH, self.Click_LogoutButton_Xpath)
            return "Login Pass"
        except:
            return "Login Fail"
# 30
