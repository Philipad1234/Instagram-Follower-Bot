from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep

SIMILAR_ACCOUNT = "TARGET_ACCOUNT_TO_FOLLOW"
USERNAME = "YOUR_INSTAGRAM_USERNAME"
PASSWORD = "YOUR_INSTAGRAM_PASSWORD"


class InstaFollower:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(chrome_options)

    def login(self):
        instagram_url = " https://www.instagram.com/accounts/login/"
        self.driver.get(instagram_url)

        sleep(5)
        username = self.driver.find_element(By.NAME, "username")
        username.send_keys(USERNAME)
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(PASSWORD)

        sleep(5)
        login_button = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        login_button.click()

        sleep(30)
        not_now_button = self.driver.find_element(By.XPATH, "//div[contains(text(), 'Not now')]")
        not_now_button.click()

    def find_followers(self):
        target_url = f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers"
        self.driver.get(target_url)

        sleep(10)
        modal_xpath = "/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div"
        modal = self.driver.find_element(By.XPATH, modal_xpath)
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            sleep(5)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, value='._aano button')

        for button in all_buttons:
            try:
                button.click()
                sleep(1.1)

            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()


follower_bot = InstaFollower()
follower_bot.login()
follower_bot.find_followers()
follower_bot.follow()
