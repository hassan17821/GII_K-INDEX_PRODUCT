# Import necessary libraries
from bs4 import BeautifulSoup
import requests
import re

# Global variables
base_url = "http://nomads.ncep.noaa.gov:80/dods/gfs_0p25_1hr"
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "max-age=0",
    "if-modified-since": "Sun, 14 Jul 2024 11:51:46 GMT",
    "priority": "u=0, i",
    "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1"
}

def fetch_latest_data_url(base_url):
    # Function to fetch the latest data URL
    def fetch_page_content(url):
        response = requests.get(url, headers=headers)
        return response.text

    def parse_latest_entry_url(page_content, base_url):
        soup = BeautifulSoup(page_content, 'html.parser')
        latest_entry = soup.find_all('b')[-1]
        latest_data_url = latest_entry.find_next('a')['href']
        if not latest_data_url.startswith(base_url):
            latest_data_url = base_url + latest_data_url
        return latest_data_url

    def extract_date_from_url(url):
        match = re.search(r'gfs(\d{8})', url)
        if match:
            return match.group(1)
        else:
            return None

    # Fetch the initial page content
    page_content = fetch_page_content(base_url)
    latest_data_url = parse_latest_entry_url(page_content, base_url)
    
    date_str = extract_date_from_url(latest_data_url)
    
    if date_str:
        # Example API call using the extracted date
        gfs_url = f"https://nomads.ncep.noaa.gov/dods/gfs_0p25_1hr/gfs{date_str}"
        gfs_url_content = fetch_page_content(gfs_url)
        # Process gfs_url_content as needed
        
        return latest_data_url, gfs_url_content
    else:
        return latest_data_url, None

# Usage example:
latest_data_url, gfs_url_content = fetch_latest_data_url(base_url)
print("Latest Data URL:", latest_data_url)
if gfs_url_content:
    print("GFS URL Content fetched successfully.")
else:
    print("No valid date found in the URL.")
