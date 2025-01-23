# Jai Shree Ram


from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import warnings
from selenium.webdriver.chrome.service import Service
import pathlib
import utils.utils as utils

def boilerplate():
    warnings.simplefilter("ignore")
    global url
    url = "https://mitaoe.codetantra.com/login.jsp"
    script_directory = pathlib.Path().absolute()
    chrome_driver_path = "./chromedriver.exe"
    chrome_options = Options()
    # chrome_options.add_argument("--headless=new")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument('--log-level=3')
    user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) MicrosoftEdge/117.0.2045.36 Safari/537.2'
    chrome_options.add_argument(f'user-agent={user_agent}')

    service = Service(executable_path=chrome_driver_path)
    global driver
    driver = webdriver.Chrome(service=service, options=chrome_options)

def login():
    credentials = utils.readJsonFile("db/db.json")
    email = credentials.get("email")
    password = credentials.get("password")

    driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys(email)
    driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "#loginBtn").click()



boilerplate()







driver.get(url)




input("Press Enter to close the browser...")
