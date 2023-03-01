from classes.goods import Goods


class Phone(Goods):
    def __init__(self, goods_name, price, count, sim_cnt: int):
        """Инициализация с наследованием Goods"""
        Goods.__init__(self, goods_name, price, count)
        self.__sim_cnt = sim_cnt

    @property
    def sim_cnt(self) -> int:
        """Возвращает количество сим-карт"""
        return self.__sim_cnt

    @sim_cnt.setter
    def sim_cnt(self, cnt: int) -> None:
        """Проверяет кол-во сим карт на целое число и > 0"""
        if cnt < 1 or type(cnt).__name__ != 'int':
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
        self.__sim_cnt = cnt

    def __repr__(self):
        """Отображает информацию об объекте класса в режиме отладки (для разработчиков)"""
        return f"{super().__repr__().replace(')', ',')} {self.sim_cnt})"

    def __add__(self, other):
        """Позволяет складывать кол-во товара классов: 'Phone', 'Goods' """
        valid_classes = ['Phone', 'Goods']

        if type(self).__name__ in valid_classes\
                and type(other).__name__ in valid_classes:
                    return self.count + other.count
        else:
            raise TypeError('Данные классы запрещено складывать')
