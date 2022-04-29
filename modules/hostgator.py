def hostgator_parser(item_selector):
    def xp(x): return item_selector.xpath(x).getall()
    data = {
        'CPU/VCPU': '',
        'MEMORY': '',
        'STORAGE/SSD DISK': '',
        'BANDWIDTH/TRANSFER': '',
        'PRICE [$/mo]': ''
    }
    data['CPU/VCPU'] = item_selector.css('.pricing-card-title::text').get()
    data['PRICE [$/mo]'] = ''.join(item_selector.css(
        '.pricing-card-price::text').getall()[:2])
    data['MEMORY'] = xp('//li[1]/text()')[0].replace(' RAM',
                                                     '').replace(' ', '').replace('GB', ' GB')
    data['STORAGE/SSD DISK'] = xp('//li[3]/text()')[0]
    data['BANDWIDTH/TRANSFER'] = xp('//li[4]/text()')[0]
    return data