from classes.classes import Goods

Goods.instantiate_from_csv()  # создание объектов из данных файла
print(len(Goods.objects_list))  # в файле 5 записей с данными по товарам
