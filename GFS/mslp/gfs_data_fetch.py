# !pip install beautifulsoup4
from bs4 import BeautifulSoup
import requests
import re

DATA_URLS = []

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

def parse_all_entry_urls(page_content, base_url):
    DATA_URLS = []
    soup = BeautifulSoup(page_content, 'html.parser')
    entries = soup.find_all('b')
    for entry in entries:
        data_url = entry.find_next('a')['href']
        if not data_url.startswith(base_url):
            data_url = base_url + data_url
        DATA_URLS.append(data_url)
    return DATA_URLS

def extract_date_from_url(url):
    match = re.search(r'gfs(\d{8})', url)
    if match:
        return match.group(1)
    else:
        return None

def fetch_all_data(base_url):
    date_url_content = fetch_page_content(base_url)
    all_data_urls = parse_all_entry_urls(date_url_content, base_url)

    return all_data_urls

def fetch_gfs_mslp():
    all_date_urls = fetch_all_data(base_url)
    last = all_date_urls[-1]
    second_last = all_date_urls[-2]

    last_data_urls = fetch_all_data(last)
    second_last_data_urls = fetch_all_data(second_last)

    # Combine the two lists
    combined = second_last_data_urls + last_data_urls;

    # Filter out the ".info" files
    # filtered_urls = [url for url in combined if url.endswith(".info")]

    # Sort the filtered list to preserve the original order
    # filtered_urls.sort()

    for url in combined:
        print(url)
    return combined

# fetch_gfs_mslp()

export = fetch_gfs_mslp