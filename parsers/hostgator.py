from .base import BaseParser


class HostgatorParser(BaseParser):
    def execute(self, item_selector):
        self.item_selector = item_selector
        data = dict(self.data_sample)
        data['CPU/VCPU'] = item_selector.css('.pricing-card-title::text').get()
        data['PRICE [$/mo]'] = ''.join(item_selector.css(
                '.pricing-card-price::text').getall()[:2])
        data['MEMORY'] = self.xp('//li[1]/text()')[0].replace(' RAM',
                                                        '').replace(' ', '').replace('GB', ' GB')
        data['STORAGE/SSD DISK'] = self.xp('//li[3]/text()')[0]
        data['BANDWIDTH/TRANSFER'] = self.xp('//li[4]/text()')[0]
        return data
