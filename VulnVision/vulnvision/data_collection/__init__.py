import requests
from bs4 import BeautifulSoup

class Scrapper():
    def collect(self, url):


        url = 'https://nvd.nist.gov/vuln/detail/CVE-2023-29298'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')


        print(response.text)
