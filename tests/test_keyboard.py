from classes.keyboard import Keyboard


def test_mixinchangelang_init():
    """Тестирует инициализацию класса Keyboard"""
    kb_1 = Keyboard('товар', 25.05, 25)
    assert kb_1.goods_name == 'товар'
    assert kb_1.price == 25.05
    assert kb_1.count == 25
    assert kb_1.language == 'EN'
