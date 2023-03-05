from classes.mixins import MixinChangeLang
from pytest import raises



def test_mixinchangelang_init():
    """Тестирует инициализацию класса Goods"""
    ch_lng_1 = MixinChangeLang()
    assert ch_lng_1.language == 'EN'

    ch_lng_1 = MixinChangeLang('RU')
    assert ch_lng_1.language == 'RU'


def test_mixinchangelang_language():
    ch_lng_1 = MixinChangeLang()

    with raises(AttributeError, match="property 'language' of 'MixinChangeLang' object has no setter"):
        ch_lng_1.language = 'CH'


def test_mixinchangelang_change_lang():
    ch_lng_1 = MixinChangeLang()
    assert ch_lng_1.language == 'EN'
    ch_lng_1.change_lang()
    assert ch_lng_1.language == 'RU'
    ch_lng_1.change_lang()
    assert ch_lng_1.language == 'CH'
    ch_lng_1.change_lang()
    assert ch_lng_1.language == 'EN'





