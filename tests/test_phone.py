from classes.Phone import Phone, Goods
from pytest import raises


def test_phone_init():
    """Тестирует инициализацию класса Goods"""
    phone = Phone('товар', 25.05, 25, 2)
    assert phone.goods_name == 'товар'
    assert phone.price == 25.05
    assert phone.count == 25
    assert phone.sim_cnt == 2


def test_sim_cnt():
    phone = Phone('товар', 25.05, 25, 2)
    phone.sim_cnt = 5
    assert phone.sim_cnt == 5
    with raises(ValueError, match='Количество физических SIM-карт должно быть целым числом больше нуля.'):
        phone.sim_cnt = 0
    with raises(ValueError, match='Количество физических SIM-карт должно быть целым числом больше нуля.'):
        phone.sim_cnt = 0.5


def test_add():
    class Iphone(Phone):
        pass

    goods = Goods('товар', 25.05, 25)
    phone = Phone('товар', 25.05, 25, 2)
    iphone = Iphone('товар', 25.05, 25, 2)

    with raises(TypeError, match='Данные классы запрещено складывать'):
        iphone + phone
    with raises(TypeError, match='Данные классы запрещено складывать'):
        iphone + goods

    assert phone + goods == 50


def test_repr():
    """Тестирует магический метод __repr__"""
    phone = Phone('товар', 25.05, 25, 2)
    assert phone.__repr__() == "Phone('товар', 25.05, 25, 2)"