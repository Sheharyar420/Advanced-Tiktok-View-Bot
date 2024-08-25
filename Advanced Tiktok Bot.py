from playsound import playsound # type: ignore
import selenium
from selenium import webdriver
import selenium.common
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from PIL import Image
import pytesseract
import pyautogui
try:
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    service = Service(executable_path=r"C:\Users\Qais sherazi\Desktop\projects\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("https://zefoy.com/")
    captcha = driver.find_element(By.CLASS_NAME, "img-thumbnail")
    captcha.screenshot(r"C:\Users\Qais sherazi\Desktop\projects\ScreenShots\captcha.png")
    image = Image.open(r"C:\Users\Qais sherazi\Desktop\projects\ScreenShots\captcha.png")
    text = pytesseract.image_to_string(r"C:\Users\Qais sherazi\Desktop\projects\ScreenShots\captcha.png")
    captchafeild = driver.find_element(By.CLASS_NAME, "form-control")
    captchafeild.send_keys(text + Keys.ENTER)
    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "t-views-button"))
        )
    except selenium.common.exceptions.TimeoutException:
        captcahagain = driver.find_element(By.XPATH, "(//button[@class='btn btn-secondary col-sm'][normalize-space()='Close'])[4]")
        captcahagain.click()
        captcha = driver.find_element(By.CLASS_NAME, "img-thumbnail")
        captcha.screenshot(r"C:\Users\Qais sherazi\Desktop\projects\ScreenShots\captcha.png")
        image = Image.open(r"C:\Users\Qais sherazi\Desktop\projects\ScreenShots\captcha.png")
        text = pytesseract.image_to_string(r"C:\Users\Qais sherazi\Desktop\projects\ScreenShots\captcha.png")
        captchafeild = driver.find_element(By.CLASS_NAME, "form-control")
        captchafeild.send_keys(text + Keys.ENTER)
    views = driver.find_element(By.CLASS_NAME, "t-views-button")
    views.click()
    viewsfeild = driver.find_element(By.XPATH, "(//input[@placeholder='Enter Video URL'])[4]")
    viewsfeild.send_keys("https://www.tiktok.com/@imtiazahmed9933/video/7314981589006454018")
    viewsendbutton = driver.find_element(By.XPATH, "//div[@class='col-sm-5 col-xs-12 p-1 container t-views-menu']//button[@type='submit'][normalize-space()='Search']")
    def viewssending():
        for i in range(1, 9999999):
            time.sleep(3)
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='col-sm-5 col-xs-12 p-1 container t-views-menu']//button[@type='submit'][normalize-space()='Search']"))
            )
            viewsendbutton.click()
            time.sleep(3)
            timeleft = driver.find_element(By.XPATH, "//span[@class='br views-countdown']").text.split()
            mins = int(timeleft[2])
            seconds = int(timeleft[4])
            minsinseconds = mins * 60
            finaltime = minsinseconds + seconds
            time.sleep(finaltime)
            viewsendbutton.click()
            viewsendbutton.click()
            try:
                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[10]/div[1]/div[1]/div[1]/div[1]/form[1]/button[1]")))
            except selenium.common.exceptions.TimeoutException:
                viewsendbutton.click()
                time.sleep(1)
                viewsendbutton.click()
            finalviewssend = driver.find_element(By.XPATH, "/html[1]/body[1]/div[10]/div[1]/div[1]/div[1]/div[1]/form[1]/button[1]")
            finalviewssend.click()
            playsound(r"D:\AUDIO\Sent.mp3")
            time.sleep(4)
    try:
        viewsendbutton.click()
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[10]/div[1]/div[1]/div[1]/div[1]/form[1]/button[1]"))
        )
        finalviewssend = driver.find_element(By.XPATH, "/html[1]/body[1]/div[10]/div[1]/div[1]/div[1]/div[1]/form[1]/button[1]")
        finalviewssend.click()
        playsound(r"D:\AUDIO\Sent.mp3")
        viewssending()
    except selenium.common.exceptions.TimeoutException:
        for i in range(1, 9999999):
            viewsendbutton.click()
            time.sleep(2)
            timeleft = driver.find_element(By.XPATH, "//span[@class='br views-countdown']").text.split()
            mins = int(timeleft[2])
            seconds = int(timeleft[4])
            minsinseconds = mins * 60
            finaltime = minsinseconds + seconds
            time.sleep(finaltime)
            viewsendbutton.click()
            try:
                WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[10]/div[1]/div[1]/div[1]/div[1]/form[1]/button[1]")))
            except selenium.common.exceptions.TimeoutException:
                viewsendbutton.click()
                time.sleep(2)
                viewsendbutton.click()
                time.sleep(2)
            finalviewssend = driver.find_element(By.XPATH, "/html[1]/body[1]/div[10]/div[1]/div[1]/div[1]/div[1]/form[1]/button[1]")
            finalviewssend.click()
            time.sleep(4)
            playsound(r"D:\AUDIO\Sent.mp3")
except:
    playsound(r"D:\AUDIO\ERROR!.mp3")
