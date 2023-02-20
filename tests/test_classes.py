from classes.classes import Goods


def test_goods_init():
    goods = Goods('товар', 25.05, 25)
    assert goods.goods_name == 'товар'
    assert goods.price == 25.05
    assert goods.count == 25


def test_goods_objects_list():
    Goods.objects_list = []
    goods_1 = Goods('товар', 25.05, 25)
    goods_2 = Goods('товар', 25.05, 25)
    assert len(Goods.objects_list) == 2


def test_goods_price_calc():
    goods_3 = Goods('товар', 25.05, 2)
    assert goods_3.price_calc() == 50.1


def test_goods_sale_calc():
    goods_3 = Goods('товар', 100, 2)
    goods_3.sale_calc()
    assert goods_3.price == 85.0
