import re

def vultr_parser(item_selector):
    # parsel internal xpath usage
    def xp(x): return item_selector.xpath(x).getall()
    data = {
        'CPU/VCPU': '',
        'MEMORY': '',
        'STORAGE/SSD DISK': '',
        'BANDWIDTH/TRANSFER': '',
        'PRICE [$/mo]': ''
    }

    cpu_data = item_selector.css('.package__title::text').get()
    price_data = item_selector.css('.price__value b::text').get()
    if cpu_data and price_data:
        cpu_text = re.sub(r'\t|\n', '', cpu_data)
        data['CPU/VCPU'] = cpu_text
        data['PRICE [$/mo]'] = re.sub(r'\t|\n', '', price_data)
        data['STORAGE/SSD DISK'] = xp('//li[1]//b/text()')[0]
        if (cpu_text == 'AMD EPYC 7443P'):
            data['MEMORY'] = xp('//li[5]//b/text()')[0]
            data['BANDWIDTH/TRANSFER'] = xp('//li[6]//b/text()')[0]
        else:
            data['MEMORY'] = xp('//li[3]//b/text()')[0]
            data['BANDWIDTH/TRANSFER'] = xp('//li[5]//b/text()')[0]

        return data

    return None
