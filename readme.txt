🚀 Automate Naukri Profile Update using Selenium

This script automates the process of logging into Naukri.com, navigating to the profile section, and updating the profile. It uses Selenium WebDriver for automation.

------------------------------------------------------------
📌 Prerequisites  

Before running the script, ensure you have the following installed:

1. Python (>=3.8) → Download from https://www.python.org/downloads/  
2. Google Chrome (Latest version) → Download from https://www.google.com/chrome/  
3. ChromeDriver (Automatically managed using webdriver-manager)  
4. Selenium Python Library  -> pip install selenium webdriver-manager (run this if selenium is not present in your PC)
------------------------------------------------------------
📦 Installation  

1️⃣ Clone the Repository  
   Open your terminal and run the following commands:  

   git clone https://github.com/yourusername/naukri-automation.git  
   cd naukri-automation  

2️⃣ Create a Virtual Environment (Recommended)  

   For Windows:  
   python -m venv venv  
   venv\Scripts\activate  

   For Mac/Linux:  
   python3 -m venv venv  
   source venv/bin/activate  

3️⃣ Install Required Dependencies  

   pip install -r requirements.txt  

------------------------------------------------------------
⚡ How to Run the Script  

   python naukri_update.py  

This script will:  
- Open Naukri.com in Chrome  
- Log in using your credentials  
- Navigate to the profile section  
- Update your profile summary  
- Save changes and close the browser  

------------------------------------------------------------
💡 Troubleshooting  

1. "ImportError: No module named selenium"  
   Solution:  
   pip install selenium webdriver-manager  

2. "SessionNotCreatedException" Error  
   Solution:  
   Ensure Google Chrome and ChromeDriver are updated.  

3. "Element Not Found" Error  
   Solution:  
   - The website UI may have changed.  
   - Use Inspect Element (Press F12 in Chrome) to find updated ID/XPath of elements.  

------------------------------------------------------------
👨‍💻 Author  

Pranjal Rajput  
Connect with me on LinkedIn: https://www.linkedin.com/in/pranjal-rajput-b235a61bb/
