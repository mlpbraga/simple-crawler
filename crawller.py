import pandas as pd
import requests as req
from parsel import Selector
from modules.vultr import vultr_parser

URL_1 = 'https://www.vultr.com/products/bare-metal/#pricing'
URL_2 = 'https://www.hostgator.com/vps-hosting'

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
            def xp(x): return item_selector.xpath(x).getall()
            data = {
                'CPU/VCPU': '',
                'MEMORY': '',
                'STORAGE/SSD DISK': '',
                'BANDWIDTH/TRANSFER': '',
                'PRICE [$/mo]': ''
            }
            data['CPU/VCPU'] =  item_selector.css('.pricing-card-title::text').get()
            data['PRICE [$/mo]'] = ''.join(item_selector.css(
                '.pricing-card-price::text').getall()[:2])
            data['MEMORY'] = xp('//li[1]/text()')[0].replace(' RAM', '').replace(' ', '').replace('GB', ' GB')
            data['STORAGE/SSD DISK'] = xp('//li[3]/text()')[0]
            data['BANDWIDTH/TRANSFER'] = xp('//li[4]/text()')[0]
            list_rows.append(data)
    df = pd.DataFrame(list_rows, columns=columns)
    return df
