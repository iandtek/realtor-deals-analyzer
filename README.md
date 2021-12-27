# Realtor Deals Analyzer
This is a Python scraper of Realtor.ca that analyzes multi-family deals and notifies you when it finds a good deal. It uses Selenium to scrape the javascript enabled [realtor.ca website](https://realtor.ca)

# How to run

1. Download Chrome Driver from [this link](https://chromedriver.chromium.org/downloads)
2. Add the executable to a folder in your PATH
3. Create a venv with the following command `python3 -m venv venv`
4. Activate the virtual environment (command depends on the platform you are using, in Windows Powershell Command is `.\\venv\\Scripts\\Activate.ps1`, in Linux it's `source venv/bin/activate`)
5. Install dependecies in the venv using `pip install -r requirements.txt`
6. Run the scraper `python3 scraper/realtor.py`

# Collected Data Example

1. Property List from Search
    ```js
        [
            "https://www.realtor.ca/real-estate/23716262/527-6th-st-humboldt",
            "https://www.realtor.ca/real-estate/23859932/130-142-rue-masson-sainte-th%C3%A8cle",
            "https://www.realtor.ca/real-estate/23512053/105-mueller-by-annaheim",
            "https://www.realtor.ca/real-estate/23735887/275-277-rue-l%C3%A9on-xiii-nicolet",
            "https://www.realtor.ca/real-estate/23431029/665-667-rue-principale-sainte-rose-de-watford",
            "https://www.realtor.ca/real-estate/23807274/215-217-main-street-plaster-rock",
            "https://www.realtor.ca/real-estate/23436684/91-99-7e-rue-e-d%C3%A9gelis",
            "https://www.realtor.ca/real-estate/22928580/172-178-rue-champoux-disraeli-ville",
            "https://www.realtor.ca/real-estate/23362680/101-107-rue-st-andr%C3%A9-m%C3%A9tabetchouanlac-%C3%A0-la-croix",
            "https://www.realtor.ca/real-estate/23828362/1127-boul-blanche-baie-comeau-mingan",
            "https://www.realtor.ca/real-estate/23733089/135-chemin-canada-edmundston",
            "https://www.realtor.ca/real-estate/23425937/709-w-1st-st-assiniboia",
            "https://www.realtor.ca/real-estate/23619687/221-1st-ave-n-sturgis",
            ...
        ]
    ```

    See full output [here](data/example/properties_in_search.json)

2. Property Information
    ```js
        [
            {
                "url": "https://www.realtor.ca/real-estate/23716262/527-6th-st-humboldt",
                "address": "527 6th ST, Humboldt, Saskatchewan S0K2A1",
                "price": "$80,000",
                "description": "Excellent investment property. Fixer upper. 5 plex building in the heart of downtown Humboldt. Near many amenities, school and park. Large lot and great potential for rental. Units consist of 2 bachelor suites and 3 self contained suites with 1 bedroom and bathroom. Property for sale as is. Hot water heating system. Please read the attached supplements. Call your realtor to view. (24589931)",
                "summary": {
                    "Property Type": "Multi-family",
                    "Building Type": "Multi-Family",
                    "Storeys": "1.5",
                    "Title": "Freehold",
                    "Built in": "1932",
                    "Annual Property Taxes": "$2,000",
                    "Total Parking Spaces": "0",
                    "Time on REALTOR.ca": "80 days",
                    "Features": "Treed",
                    "Total Units": "5",
                    "Heating Type": "Hot Water",
                    "Landscape Features": "Lawn, Fully landscaped"
                }
            },
            {
                "url": "https://www.realtor.ca/real-estate/23859932/130-142-rue-masson-sainte-th%C3%A8cle",
                "address": "130-142 Rue Masson, Sainte-Th\u00e8cle, Quebec G0X3G0",
                "price": "$95,000",
                "description": "See listing broker(s) (37755765)",
                "summary": {
                    "Property Type": "Multi-family",
                    "Building Type": "Multi-Family",
                    "Storeys": "3",
                    "Land Size": "9798 sqft",
                    "Age Of Building": "Age is unknown",
                    "Time on REALTOR.ca": "28 days",
                    "Features": "Wood windows, Crank windows",
                    "Style": "Detached",
                    "Total Units": "6",
                    "Heating Type": "(Electric)",
                    "Utility Sewer": "Municipal sewage system",
                    "Water": "Municipal water",
                    "Farm Type": "Other"
                }
            },
            ...
        ]
    ```
    See full output [here](data/example/properties_info.json)

# TO DO

1. Bypass Captcha verifier after a few properties are scraped. Maybe relaunching another instance of the driver so Realtor thinks it's another user in the same network.
2. Analyze of data collected to figure out when it's a good deal
3. Send email when a good deal has been found.
4. Flask web application that can show the information collected from the scraper in real time.

