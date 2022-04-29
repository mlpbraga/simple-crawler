from .base import BaseParser


class HostgatorParser(BaseParser):
    """
    Specific parser to hostgator content
    ...
    Attributes
    ----------
    data_sample: dict
        a structured dictionary containing all relevant data that needs to be retrieved from HTML
    item_selector: Selector
        a Selector object from parsel lib
    """
    def execute(self, item_selector):
        """
        Returns structured data retrieved from item_selector HTML content
        ...
        Parameters
        ----------
        item_selector: Selector
        a Selector object from parsel lib
        """
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
