from classes.goods import Goods
from exceptions.ex_goods import InstantiateCSVError


def test_goods_init():
    """Тестирует инициализацию класса Goods"""
    goods = Goods('товар', 25.05, 25)
    assert goods.goods_name == 'товар'
    assert goods.price == 25.05
    assert goods.count == 25


def test_goods_objects_list():
    """Тестирует наполнение списка объектов"""
    Goods.objects_list = []
    goods_1 = Goods('товар', 25.05, 25)
    goods_2 = Goods('товар', 25.05, 25)
    assert len(Goods.objects_list) == 2


def test_goods_price_calc():
    """Тестирует расчет цены по позиции"""
    goods_3 = Goods('товар', 25.05, 2)
    assert goods_3.price_calc() == 50.1


def test_goods_sale_calc():
    """Тестирует применение скидки на товар"""
    goods_3 = Goods('товар', 100, 2)
    goods_3.sale_calc()
    assert goods_3.price == 85.0


def test_goods_goods_name():
    """Тестирует коррекктность работы проверки
     на длинну символов атрибута goods_name"""
    goods_4 = Goods('товар', 100, 2)
    assert len(goods_4.goods_name) == 5

    try:
        goods_5 = Goods('товар_2585544', 100, 2)
    except Exception as _ex:
        except_text = 'Длина наименования товара превышает 10 символов.'
        assert str(_ex) == except_text


def test_instantiate_from_csv_():
    """Тестирует создание объектов класаа из CSV"""
    Goods.objects_list = []
    Goods.instantiate_from_csv()
    goods_5 = Goods.objects_list[0]
    assert len(Goods.objects_list) == 5
    assert goods_5.goods_name == 'Смартфон'
    assert goods_5.price == 100
    assert goods_5.count == 1

    try:
        Goods.instantiate_from_csv(path='nofile')
    except FileNotFoundError as _ex:
        assert str(_ex) == "Отсутствует файл nofile"

    try:
        Goods.instantiate_from_csv(path='items_t.csv')
    except InstantiateCSVError as _ex:
        assert str(_ex) == "Файл items_t.csv поврежден"



def test_is_integer():
    """Тестирует метод определения 'целого числа'"""
    assert Goods.is_integer(5) is True
    assert Goods.is_integer(5.0) is True
    assert Goods.is_integer(5.5) is False


def test_repr():
    """Тестирует магический метод __repr__"""
    goods_6 = Goods('товар', 25.05, 25)
    assert goods_6.__repr__() == "Goods('товар', 25.05, 25)"


def test_str():
    """Тестирует магический метод __str__"""
    goods_7 = Goods('товар', 25.05, 25)
    assert str(goods_7) == 'товар'