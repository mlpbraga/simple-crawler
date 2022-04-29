class BaseParser:
    """
    Parser class, containing general attributes and methods to all possible parsers.
    ...
    Attributes
    ----------
    data_sample: dict
        a structured dictionary containing all relevant data that needs to be retrieved from HTML
    item_selector: Selector
        a Selector object from parsel lib
    """
    data_sample = {
        'CPU/VCPU': '',
        'MEMORY': '',
        'STORAGE/SSD DISK': '',
        'BANDWIDTH/TRANSFER': '',
        'PRICE [$/mo]': ''
    }

    def __init__(self) -> None:
        pass

    def xp(self, x):
        """
        Returns string containing HTML retrieved using current selector's xpath method
        ...
        Parameters
        ----------
        x: str
            string containing xpath to be found by selector xpath method
        """
        return self.item_selector.xpath(x).getall()
