from playwright.sync_api import sync_playwright
import datetime

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://www.naukri.com/mnjuser/profile")
    
    # Login
    page.fill('//input[@id="usernameField"]', "ENTER YOUR EMAIL ID")
    page.fill('//input[@id="passwordField"]', "ENTER YOUR PASSWORD")
    page.wait_for_selector('//button[contains(text(), "Login")]')
    page.click('//button[contains(text(), "Login")]')
    page.wait_for_event("load")
    page.wait_for_timeout(1000)

    # Navigate to Profile Section
    page.goto("https://www.naukri.com/mnjuser/profile")
    page.wait_for_timeout(2000)
    
    # Click on "Profile Summary" to edit
    page.locator('//span[contains(text(), "Profile summary")]').click()
    page.wait_for_timeout(1000)

    # Click on the edit (pencil) icon
    page.locator('//*[@id="lazyProfileSummary"]/div/div/div/div[1]/span[2]').click()
    page.wait_for_timeout(1000)

    # Click "Save" to apply changes
    page.locator("//button[@class='btn-dark-ot' and @type='submit']").click()
    page.wait_for_timeout(1000)

    # Log the update
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"Profile Summary Updated Successfully - {timestamp}\n"
    with open("/Users/thepranjalrajput/VS CODE/Logs.txt", "a") as logfile:
        logfile.write(log_message)

    print("Profile Summary Updated Successfully")
    # browser.close()