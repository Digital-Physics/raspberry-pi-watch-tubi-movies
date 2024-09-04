from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys  # Import Keys class
from selenium.webdriver.common.by import By
import os
import time
import random

os.environ['DISPLAY'] = ':0' # to avoid error when ssh
os.system("amixer set Master 50%")  # Linux way to set the audio

chrome_service = Service('/usr/lib/chromium-browser/chromedriver')
driver = webdriver.Chrome(service=chrome_service)

site = "youtube" if random.random() < 0.2 else "tubi"

if site == "youtube":
  url = "https://www.youtube.com/watch?v=9uVKwhU2lp0&t=40s"

  driver.get(url)
  time.sleep(4)
  
  # play
  body = driver.find_element(By.TAG_NAME, 'body')
  body.send_keys(Keys.ARROW_UP + " ")
 
  # full-screen
  body.send_keys("f")
elif site == "tubi":
  url = "https://tubitv.com/movies/100015091/digital-physics"
  
  driver.get(url)
  time.sleep(4)
  
  #play
  play_btn = driver.find_element(By.CSS_SELECTOR, "div.web-iconButton")
  play_btn.click()

  #full-screen button
  full_screen_btn = driver.find_element(By.CSS_SELECTOR, "span#fullscreenArea button.web-iconButton-container")
  full_screen_btn.click()

  time.sleep(10)

  # Locate the video element
  video = driver.find_element(By.TAG_NAME, 'video')

  # jump ahead
  # Set the video time to your desired time in seconds since you can't add it to the URL in Tubi
  desired_time = 71*60
  driver.execute_script(f"arguments[0].currentTime = {desired_time};", video)

# don't let this script complete or your webdriver will go away
while True:
  pass

