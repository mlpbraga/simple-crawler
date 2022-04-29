import pandas as pd
import requests as req
from parsel import Selector
from modules.vultr import vultr_parser

URL_1 = 'https://www.vultr.com/products/bare-metal/#pricing'
URL_2 = 'https://www.hostgator.com/vps-hosting'

def crawller(url):
    columns = ['CPU/VCPU', 'PRICE [$/mo]', 'STORAGE/SSD DISK',
               'MEMORY', 'BANDWIDTH/TRANSFER', ]
    response = req.get(url)
    html_text = response.text
    selector = Selector(text=html_text)
    ul_list = selector.css('.col-lg-3').getall()

    list_rows = []
    for item in ul_list:
        item_selector = Selector(text=item)
        data = vultr_parser(item_selector)
        if data:
            list_rows.append(data)

    df = pd.DataFrame(list_rows, columns=columns)
    return df
