class Analysis_data():
    def __init__(self, data: list, min_price=1.0):
        self.__data = data
        self.__revenue = 0
        self.__category = {}
        self.__exp_purch = []
        self.__mean_purch = {}
        self.__min_price = min_price

    def __total_revenue(self):  # total_revenue(purchases)
        '''
        Рассчет общей выручки (цена * количество для всех записей)
        '''
        for i in self.__data:
            self.__revenue = self.__revenue + i.get('price') * i.get('quantity')

    def __items_by_category(self):  # items_by_category(purchases)
        '''
        формирование словаря с уникальными товарами в категории
        '''
        for dict_val in self.__data:
            self.__category[dict_val['category']] = []

        for dict_val in self.__data:
            if dict_val['category'] in self.__category:
                self.__category[dict_val.get('category')].append(dict_val.get('item'))

    def __expensive_purchases(self):  # expensive_purchases(purchases, min_price)
        '''
        Формирование списка покупок, где цена товара больше или равна min_price
        '''
        for dict_val in self.__data:
            if dict_val.get('price') >= self.__min_price:
                self.__exp_purch.append(dict_val)

    def __average_price_by_category(self):  # average_price_by_category(purchases)
        '''
        Вычисление средней цены товаров по каждой категории.
        '''
        for dict_val in self.__data:
            self.__mean_purch[dict_val['category']] = 0

        cnt_categoty = self.__how_many_category()

        for dict_val in self.__data:
            self.__mean_purch[dict_val['category']] += dict_val.get('price') / cnt_categoty.get(dict_val['category'])

    def __how_many_category(self):
        '''
        Вычисление количества категорий в списке товаров
        '''
        dct_category = {}

        for dict_val in self.__data:
            dct_category[dict_val.get('category')] = 0

        for dict_val in self.__data:
            dct_category[dict_val.get('category')] += 1

        return dct_category

    def __most_frequent_category(self):  # most_frequent_category(purchases)
        '''
        Поиск категории, по которой куплено
        больше всего единиц товаров (учитывайте поле quantity).
        '''
        cnt_category = self.__how_many_category()
        result = next((key for key, value in cnt_category.items() if value == max(list(cnt_category.values()))), None)
        return result

    def get_info(self):
        '''
        Вывод всей обобщенной информации
        '''
        self.__total_revenue()
        self.__items_by_category()
        self.__expensive_purchases()
        self.__average_price_by_category()
        popular_category = self.__most_frequent_category()

        print(
            f'''
        Общая выручка:\t{self.__revenue}\n
        Товары по категориям:\n\t\t{self.__category}\n
        Покупки дороже {self.__min_price}:\n\t\t{self.__exp_purch}\n
        Средняя цена по категориям:\n\t\t{self.__mean_purch}\n
        Категория с наибольшим количеством проданных товаров: {popular_category}
            ''')


def __main__():
    purchases = [
        {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
        {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
        {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
        {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
    ]
    result = Analysis_data(data=purchases)
    result.get_info()


__main__()
