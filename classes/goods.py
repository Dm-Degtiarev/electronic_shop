import csv
from exceptions.ex_goods import InstantiateCSVError


class Goods:
    sale_percent = 0.85
    objects_list = []

    def __init__(self, goods_name: str, price: float, count: int):
        """Инициализация класса"""
        self.goods_name  = goods_name
        self.price = price
        self.count = count
        self.objects_list.append(self)
        super().__init__()

    def __repr__(self):
        """Отображает информацию об объекте класса в режиме отладки (для разработчиков)"""
        return f"{self.__class__.__name__}('{self.__goods_name}', {self.price}, {self.count})"

    def __str__(self):
        """отображает информацию о объекте класса для пользователей (print, str)"""
        return self.__goods_name

    @property
    def goods_name(self) -> str:
        """Возвращает наименование товара"""
        return self.__goods_name

    @goods_name.setter
    def goods_name(self, name: str) -> None:
        """Проверяет название товара на длинну до 10 символов"""
        if len(name) > 10:
            raise Exception('Длина наименования товара превышает 10 символов.')
        self.__goods_name = name

    def price_calc(self) -> float:
        """Вычисляет сумму по позиции"""
        goods_price = self.price * self.count
        return goods_price

    def sale_calc(self) -> None:
        """Применяет скидку на товар"""
        self.price *= self.sale_percent

    @classmethod
    def instantiate_from_csv(cls, path='items.csv', encoding='windows-1251'):
        """Создает объекты класса из CSV"""
        try:
            with open(path, 'r', encoding=encoding) as file:
                csv_file = csv.DictReader(file)
                parse_columns = ['name', 'price', 'quantity']

                # записываем данные из файла
                for line in csv_file:
                    if list(line.keys()) != parse_columns:
                        raise InstantiateCSVError(f'Файл {path} поврежден')
                    cls(
                        goods_name=line['name'],
                        price=float(line['price']),
                        count=int(line['quantity'])
                    )
        except FileNotFoundError:
            raise FileNotFoundError(f'Отсутствует файл {path}')

    @staticmethod
    def is_integer(attr):
        """Проверяет, является ли число целым"""
        if attr % 1 == 0:
            return True
        else:
            return False
