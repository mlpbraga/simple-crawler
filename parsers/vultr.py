import re
from .base import BaseParser


class VultrParser(BaseParser):
    """
    Specific parser to vultr content
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
        cpu_data = item_selector.css('.package__title::text').get()
        price_data = item_selector.css('.price__value b::text').get()
        if cpu_data and price_data:
            cpu_text = re.sub(r'\t|\n', '', cpu_data)
            data['CPU/VCPU'] = cpu_text
            data['PRICE [$/mo]'] = re.sub(r'\t|\n', '', price_data)
            data['STORAGE/SSD DISK'] = self.xp('//li[1]//b/text()')[0]
            if (cpu_text == 'AMD EPYC 7443P'):
                data['MEMORY'] = self.xp('//li[5]//b/text()')[0]
                data['BANDWIDTH/TRANSFER'] = self.xp('//li[6]//b/text()')[0]
            else:
                data['MEMORY'] = self.xp('//li[3]//b/text()')[0]
                data['BANDWIDTH/TRANSFER'] = self.xp('//li[5]//b/text()')[0]
            return data
        return None
