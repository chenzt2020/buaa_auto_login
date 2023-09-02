import time
from selenium import webdriver


def do_login(driver):
    driver.find_element(by="id", value="username").send_keys("***")
    driver.find_element(by="id", value="password").send_keys("***")
    driver.find_element(by="id", value="login").click()
    time.sleep(3)


if __name__ == '__main__':
    options = webdriver.FirefoxOptions()
    options.add_argument('-headless')
    driver = webdriver.Firefox(options=options)
    # driver = webdriver.Firefox()
    try:
        driver.get("https://gw.buaa.edu.cn/")
        time.sleep(3)
        if len(driver.find_elements(by="id", value="login")) == 0:
            print("Already logged in")
        else:
            do_login(driver)
            print("Successfully logged in")
    finally:
        driver.quit()
