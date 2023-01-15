# Avoid IP Ban

This project is a script that uses Selenium and webdriver-manager to automate the Google search process using a list of proxies read from a CSV file. The script reads the list of proxies from a CSV file named 'Free_Proxy_List.csv' and then uses each proxy to open a Google search page for a specified query. The script uses the Chrome driver and rotates through the list of proxies, setting the proxy server for each instance of the driver. After each search, the driver is closed. This code can be used to conduct multiple searches on Google with different proxies to bypass IP bans and access blocked content.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
- Python 3.x
- Selenium
- webdriver-manager
- Chrome browser

### Installing
pip install selenium
pip install webdriver-manager

### Run
python app.py

### Replace "Search Query Here" with your desired search query.

## Acknowledgments
* Selenium and webdriver-manager documentation for guidance on setting up the script.
* The proxy list can be found at https://geonode.com/free-proxy-list/
