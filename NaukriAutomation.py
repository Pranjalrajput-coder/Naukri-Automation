from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Setup WebDriver (Make sure ChromeDriver is installed)
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open Naukri login page
driver.get("https://www.naukri.com/mnjuser/profile")
time.sleep(2)

# Enter login credentials
email_input = driver.find_element(By.ID, "usernameField") 
email_input.send_keys("ENTER YOUR EMAIL ID")

password_input = driver.find_element(By.ID, "passwordField") 
password_input.send_keys("ENTER YOUR PASSWORD")
password_input.send_keys(Keys.RETURN)  # Press Enter to login

time.sleep(2)  # Wait for login to complete

# Navigate to "View Profile" page
driver.get("https://www.naukri.com/mnjuser/profile")
time.sleep(3)

# Click on "Profile Summary" section to edit
profile_summary = driver.find_element(By.XPATH, '//span[contains(text(), "Profile summary")]')
profile_summary.click()

# Click on the edit (pencil) icon
profile_summary_pencil = driver.find_element(By.XPATH, '//span[@class="edit icon" and contains(text(), "editOneTheme")]')
profile_summary_pencil.click()

time.sleep(2)

# Click "Save" after editing 
save_button = driver.find_element(By.XPATH, "//button[@class='btn-dark-ot' and @type='submit']")
save_button.click()

time.sleep(3)  # Allow time for changes to save

# Close browser after update
driver.quit()