from bs4 import BeautifulSoup
import json
import requests
from scraper_api import ScraperAPIClient
client = ScraperAPIClient('8016d3a7f5044f408e92dc752356c419')

url = 'https://panolam.com/pattern-search/'


def get_filters():
    # r = requests.get(url)
    # print(r.status_code)

    result = client.get(url)
    # print(result.text)

    soup = BeautifulSoup(result.text, 'lxml')
    scripts = soup.find_all('script', type='text/javascript')

    for script in scripts:
        try:
            if 'function html_pattern_div(){' in script.string:
                raw_str = script.string
                json_data_index = raw_str.find('var data = ') + 11
                json_data_raw = raw_str[json_data_index:]
                end_json = json_data_raw.find(';')
                json_data_str = json_data_raw[:end_json]

                json_data = json.loads(json_data_str)

                for element in json_data:
                    print(element)

                print(len(json_data))
        except Exception:
            pass


if __name__ == '__main__':
    get_filters()

