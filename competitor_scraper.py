import requests
from bs4 import BeautifulSoup
import pandas as pd

# --------------------------------------------------
# 1. Website
# --------------------------------------------------

url = "https://www.madrasironingcompany.com/steam-ironing.html"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/154.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.google.com/"
}

# --------------------------------------------------
# 2. Download webpage
# --------------------------------------------------

response = requests.get(
    url,
    headers=headers,
    timeout=30
)

print("Status Code:", response.status_code)

response.raise_for_status()

# --------------------------------------------------
# 3. Parse webpage
# --------------------------------------------------

soup = BeautifulSoup(response.text, "html.parser")

title = soup.title.get_text(strip=True) if soup.title else "Not Available"

print("\nWebsite Title:")
print(title)

# --------------------------------------------------
# 4. Extract page text
# --------------------------------------------------

page_text = soup.get_text(" ", strip=True)

# --------------------------------------------------
# 5. Search important information
# --------------------------------------------------

keywords = [
    "From ₹15",
    "From ₹20",
    "From ₹10",
    "steam ironing",
    "pickup",
    "delivery",
    "urgent",
    "T. Nagar",
    "Choolaimedu"
]

print("\nRelevant Information Found:")

for keyword in keywords:
    if keyword.lower() in page_text.lower():
        print("Found:", keyword)

# --------------------------------------------------
# 6. Create competitor record
# --------------------------------------------------

competitor_data = {
    "Company Name": "Madras Ironing Company",
    "Service": "Steam Ironing",
    "Location": "Chennai",
    "Starting Price": "From ₹15",
    "Pickup & Delivery": "Available subject to conditions",
    "Turnaround": "Not specified",
    "Urgent / Express": (
        "May be available depending on workload, "
        "garment quantity and service timing"
    ),
    "Online Booking": "Call / WhatsApp",
    "Service Areas": "T. Nagar, Choolaimedu and nearby Chennai areas",
    "Source URL": url
}

# --------------------------------------------------
# 7. Create DataFrame
# --------------------------------------------------

df = pd.DataFrame([competitor_data])

print("\nCompetitor Data:")
print(df.to_string(index=False))

# --------------------------------------------------
# 8. Save to Excel
# --------------------------------------------------

output_file = (
    r"D:\IronHub_Startup_Validation\Python"
    r"\madras_ironing_scraped_data.xlsx"
)

df.to_excel(
    output_file,
    index=False
)

print("\nData saved successfully!")
print(output_file)
