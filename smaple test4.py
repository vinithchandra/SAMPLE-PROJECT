from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# Start the WebDriver and open the HTML page
service = Service(executable_path='/usr/local/bin/chromedriver/chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(service=service, options=options)

# Open the webpage
driver.get("https://vinithchandra.github.io/SAMPLE-PROJECT/")

# Wait for the webpage to load
print("Waiting for the webpage to load...")
time.sleep(5)

# Check the webpage title
print("Checking the webpage title...")
assert "Sample Project" in driver.title

# Print the webpage title
print("Webpage title:", driver.title)

# Take a screenshot
timestamp = time.strftime("%Y%m%d-%H%M%S")
screenshot_file = f"screenshot_{timestamp}.png"
driver.save_screenshot(screenshot_file)
print(f"Screenshot saved to {screenshot_file}")

# Close the WebDriver
driver.close()
print("WebDriver closed.")
