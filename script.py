from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

# Set up the driver
options = Options()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome()
driver.maximize_window()

## Bank 1 Loop
# Open the website
driver.get("https://www.youtube.com/")

# Navigate to the login

# Plug in credentials
email = driver.find_element_by_id("identifierId")
passowrd = driver.find_element_by_id("password")

email.send_keys(os.environ.get("EMAIL"))
email.submit()

# Input Token

# Naviagate to balance summary etc.

# Copy Summary

# Make new tab

# Open the Google Sheet

# Paste the summary

## Bank 2 Loop

# Plug in credentials

# Naviagate to balance summary etc.

# Copy Summary

# Switch to the Google Sheet

# Switch Sheet

# Paste the summary

## Bank 3 Loop 


