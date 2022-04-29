import calendar
import time
from constans import url_mapper, RESULTS_PATH
import argparse
import pandas as pd
import requests as req
from parsel import Selector
from parsers import VultrParser, HostgatorParser

def crawller(url):
    parser = None
    list_rows = []
    columns = ['CPU/VCPU', 'PRICE [$/mo]', 'STORAGE/SSD DISK',
               'MEMORY', 'BANDWIDTH/TRANSFER', ]
    response = req.get(url)
    html_text = response.text
    selector = Selector(text=html_text)

    if 'vultr' in url:
        ul_list = selector.css('.col-lg-3').getall()
        parser = VultrParser()

    elif 'hostgator' in url:
        ul_list = selector.css('.pricing-card').getall()
        parser = HostgatorParser()

    for item in ul_list:
        item_selector = Selector(text=item)
        data =  parser.execute(item_selector)
        if data:
            list_rows.append(data)

    df = pd.DataFrame(list_rows, columns=columns)
    return df

gmt = time.gmtime()
ts = calendar.timegm(gmt)

parser = argparse.ArgumentParser(description='Crawller.')
parser.add_argument('target', type=str,
                    help='target URL to retrieve information')
parser.add_argument('--print', default=True,
                    action='store_true', help='print crawller results')
parser.add_argument('--save_csv', default=False,
                    action='store_true', help='save crawller results to csv file')
parser.add_argument('--save_json', default=False,
                    action='store_true', help='save crawller results to json file')
args = parser.parse_args()

try:
    results_path = f'{RESULTS_PATH}{url_mapper[args.target]}_{ts}'
    results = crawller(args.target)
    if args.print:
        print(results)
    if args.save_csv:
        results.to_csv(f'{results_path}.csv', index=False)
    if args.save_json:
        results.to_json(f'{results_path}.json')
except Exception as e:
    print(f'ERROR: Failed retrieve information from {args.target}. Please, use a valid URL.')
