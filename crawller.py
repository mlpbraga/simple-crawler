import re
import pandas as pd
import requests as req
from parsel import Selector

URL_1 = 'https://www.vultr.com/products/bare-metal/#pricing'
URL_2 = 'https://www.hostgator.com/vps-hosting'


response = req.get(URL_1)
html_text = response.text
selector = Selector(text=html_text)
ul_list = selector.css('.col-lg-3').getall()

columns = ['CPU/VCPU', 'PRICE [$/mo]', 'STORAGE/SSD DISK',
           'MEMORY', 'BANDWIDTH/TRANSFER', ]

list_rows = []
for item in ul_list:
    data_format = {
        'CPU/VCPU': '',
        'MEMORY': '',
        'STORAGE/SSD DISK': '',
        'BANDWIDTH/TRANSFER': '',
        'PRICE [$/mo]': ''
    }
    item_selector = Selector(text=item)

    # parsel internal xpath usage
    def xp(x): return item_selector.xpath(x).getall()

    cpu_data = item_selector.css('.package__title::text').get()
    price_data = item_selector.css('.price__value b::text').get()
    if cpu_data and price_data:
        data_format['CPU/VCPU'] = re.sub(r'\s', '', cpu_data)
        data_format['PRICE [$/mo]'] = re.sub(r'\s', '', price_data)
        data_format['STORAGE/SSD DISK'] = xp('//li[1]//b/text()')[0]
        data_format['MEMORY'] = xp('//li[4]//b/text()')[0]
        if (data_format['CPU/VCPU'] == 'AMD EPYC 7443P'):
            data_format['BANDWIDTH/TRANSFER'] = xp('//li[3]//b/text()')[0]
        else:
            data_format['BANDWIDTH/TRANSFER'] = xp('//li[5]//b/text()')[0]

        list_rows.append(data_format)

df = pd.DataFrame(list_rows, columns=columns)