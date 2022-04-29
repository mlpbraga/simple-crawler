import pandas as pd
import requests as req
from parsel import Selector
from modules.vultr import vultr_parser
from modules.hostgator import hostgator_parser

def crawller(url):
    list_rows = []
    columns = ['CPU/VCPU', 'PRICE [$/mo]', 'STORAGE/SSD DISK',
               'MEMORY', 'BANDWIDTH/TRANSFER', ]
    response = req.get(url)
    html_text = response.text
    selector = Selector(text=html_text)

    if 'vultr' in url:
        ul_list = selector.css('.col-lg-3').getall()

        for item in ul_list:
            item_selector = Selector(text=item)
            data = vultr_parser(item_selector)
            if data:
                list_rows.append(data)
    elif 'hostgator' in url:
        ul_list = selector.css('.pricing-card').getall()

        for item in ul_list:
            item_selector = Selector(text=item)
            data = hostgator_parser(item_selector)
            list_rows.append(data)

    df = pd.DataFrame(list_rows, columns=columns)
    return df
