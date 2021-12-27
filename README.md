# Realtor Deals Analyzer
This is a Python scraper of Realtor.ca that analyzes multi-family deals and notifies you when it finds a good deal. It uses Selenium to scrape the javascript enabled [realtor.ca website](https://realtor.ca)

# How to run

1. Download Chrome Driver from [this link](https://chromedriver.chromium.org/downloads)
2. Add the executable to a folder in your PATH
3. Create a venv with the following command `python3 -m venv venv`
4. Activate the virtual environment (command depends on the platform you are using, in Windows Powershell Command is `.\\venv\\Scripts\\Activate.ps1`, in Linux it's `source venv/bin/activate`)
5. Install dependecies in the venv using `pip install -r requirements.txt`
6. Run the scraper `python3 scraper/realtor.py`

# TO DO

1. Bypass Captcha verifier after a few properties are scraped. Maybe relaunching another instance of the driver so Realtor thinks it's another user in the same network.
2. Analyze of data collected to figure out when it's a good deal
3. Send email when a good deal has been found.
4. Flask web application that can show the information collected from the scraper in real time.