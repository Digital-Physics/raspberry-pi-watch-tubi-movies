from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys  # Import Keys class
from selenium.webdriver.common.by import By
import os
import time

os.environ['DISPLAY'] = ':0' # to avoid error when ssh
os.system("amixer set Master 60%")  # Linux way to set the audio

# url = "https://tubitv.com/movies/100005567/cosmodrama"
url = "https://tubitv.com/movies/100015091/digital-physics"
chrome_service = Service('/usr/lib/chromium-browser/chromedriver')
driver = webdriver.Chrome(service=chrome_service)

driver.get(url)

time.sleep(4)

play_btn = driver.find_element(By.CSS_SELECTOR, "div.web-iconButton")
play_btn.click()

# Wait for the video to start playing
time.sleep(4)

# Find and click the full-screen button
full_screen_btn = driver.find_element(By.CSS_SELECTOR, "span#fullscreenArea button.web-iconButton-container")
full_screen_btn.click()

time.sleep(3)

jump = driver.find_element(By.TAG_NAME, 'body')

# modify this if you want to skip ahead in the movie
for _ in range(5):
  time.sleep(1)
  # jumps 30 seconds
  jump.send_keys(Keys.ARROW_DOWN + 'l')

while True:
  pass
