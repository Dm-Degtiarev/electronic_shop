class Goods:
    sale_percent = 0.85
    objects_list = []

    def __init__(self, goods_name: str, price: float, count: int):
        """Инициализация класса"""
        self.goods_name = goods_name
        self.price = price
        self.count = count
        self.objects_list.append(self)


    def price_calc(self) -> float:
        """Вычисляет сумму по позиции"""
        goods_price = self.price * self.count
        return goods_price


    def sale_calc(self) -> None:
        """Применяет скидку на товар"""
        self.price *= self.sale_percent

