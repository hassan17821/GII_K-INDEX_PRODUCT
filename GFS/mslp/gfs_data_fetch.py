# !pip install beautifulsoup4
from bs4 import BeautifulSoup
import requests
import re

DATA_URL=""
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

base_url = "http://nomads.ncep.noaa.gov:80/dods/gfs_0p25_1hr"

def fetch_page_content(url):
    response = requests.get(url, headers=headers)
    return response.text

def parse_latest_entry_url(page_content, base_url, offset=-1):
    soup = BeautifulSoup(page_content, 'html.parser')
    latest_entry = soup.find_all('b')[offset]
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
    
def fetch_latest_data(base_url):    
    date_url_content = fetch_page_content(base_url)
    latest_data_url = parse_latest_entry_url(date_url_content, base_url, -1)

    print(latest_data_url)

    date_str = extract_date_from_url(latest_data_url)
    if date_str:
        print(date_str)  # Outputs: 20240714
    else:
        print("No date found in the URL")

    # Fetch the GFS page content if a date was found
    if date_str:
        gfs_url = f"https://nomads.ncep.noaa.gov/dods/gfs_0p25_1hr/gfs{date_str}"
        gfs_url_content = fetch_page_content(gfs_url)
        # print(gfs_url_content)

        latest_data_url = parse_latest_entry_url(gfs_url_content, base_url, -1)

        if latest_data_url.endswith('.info'):
            latest_data_url = latest_data_url[:-5]

        DATA_URL = latest_data_url
        print(latest_data_url)

    return DATA_URL

export = fetch_latest_data