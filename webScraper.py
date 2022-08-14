# Author: Taseen Waseq
# Date Created: 2022-08-14
# This program will scrape YouTube using selenium and return the details for the desired YouTube Channel

from selenium import webdriver
from selenium.webdriver.common.by import By
import os

#Copy paste your path to chromedriver.exe, and desired youtube channel videos page URL
path = "YOUR PATH HERE"
youtubeURL = "YOUR YOUTUBE CHANNEL VIDEOS URL"

driver = webdriver.Chrome(executable_path=path)
driver.get(youtubeURL)

os.system('cls')


videoTitles = driver.find_elements(By.ID, "video-title")
videoViews = driver.find_elements(By.XPATH, '//*[@id="metadata-line"]/span[1]')
videoDates = driver.find_elements(By.XPATH, '//*[@id="metadata-line"]/span[2]')
subCount = driver.find_element(By.ID, "subscriber-count")

print("Subscriber Count:")
print(subCount.text)

print("\nCurrent Upload Details:")
for (title, views, date) in zip(videoTitles, videoViews, videoDates):
    print(title.text, views.text, date.text)

driver.quit()