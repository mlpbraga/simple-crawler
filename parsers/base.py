class BaseParser:
    data_sample = {
        'CPU/VCPU': '',
        'MEMORY': '',
        'STORAGE/SSD DISK': '',
        'BANDWIDTH/TRANSFER': '',
        'PRICE [$/mo]': ''
    }
    def __init__(self) -> None:
        pass

    # parsel internal xpath usage
    def xp(self, x):
        return self.item_selector.xpath(x).getall()
