from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import csv

# Read the list of proxies from a csv file
with open('Free_Proxy_List.csv', 'r', encoding="utf-8") as f:
    reader = csv.reader(f)
    proxies = list(reader)

# Open the Google search page
query = "Search Query Here"
url = f"https://www.google.com/search?q={query}"

# Rotate through the proxies
for proxy in proxies:
    # Set the proxy server
    proxy_ip = proxy[0]
    proxy_port = proxy[7]
    proxy_server = f"{proxy_ip}:{proxy_port}"

    # Create a new instance of the Chrome driver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(f"--proxy-server={proxy_server}")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)
    driver.close()
