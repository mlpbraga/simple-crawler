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
