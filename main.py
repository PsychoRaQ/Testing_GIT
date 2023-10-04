import requests
from utils import DEFAULT_URL, DEFAULT_URL_2
from utils import DEFAULT_HEADERS

def choose_market(item_count: int = 100 ,name: str = 'Wildberries') -> tuple:  # выбор маркетплейса для поиска и количество товаров. По умолчанию - Wildberries, 100 товаров
    if name == 'Wildberries':

        url_list = ()
        page = str(item_count // 100) if item_count % 100 == 0 else str(item_count // 100 + 1) # получаем номер страницы для поиска. Максимум на странице - 100 товаров
        HEADERS = DEFAULT_HEADERS

        for i in range(1,int(page)+1): # в кортеж добавляются ссылки на каждую страницу
            URL = DEFAULT_URL + page + DEFAULT_URL_2
            url_list += (URL,)
            page = str(i + 1)


    return url_list, HEADERS, item_count


def get_data(url_list: tuple, HEADERS: dict) -> tuple:  # отправка запроса и получение списка всех товаров

    data_list = ()

    for URL in url_list:
        data = requests.get(URL, headers=HEADERS).json()['data']['products']
        data_list += (data,)

    return data_list


def get_product_list(data_list: tuple, count) -> list:  # сортировка нужных данных списка / на вход получаем кортеж из списков (в каждом списке по 100 товаров)

    product_list = []
    n = 1
    for data in data_list: #
        for item in data:

            color = [i['name'] for i in item.get('colors', 'Цвет неизвестен')]  # получение списка из одного элемента с наименованием цвета

            for i in color:  # извлечение цвета из списка / простая распаковка не работает
                color = i

            product_list.append({
                'id': n,
                'brand': item['brand'],
                'model': item['name'],
                'color': color,
                'full_price': item['priceU'] / 100,
                'sale_price': item['salePriceU'] / 100,
                'sale_%': item['sale'],
                'market': 'Wildberries'
            })
            n += 1

            if n > count: # закончить выполнение функции, если получено нужное количество товаров
                break

    return product_list


def main():
    URL, HEADERS, item_count = choose_market(int(input('Введите количество товаров: ')))
    response = get_data(URL,HEADERS)

    for i in get_product_list(response,item_count):
        print(i)


if __name__ == '__main__':
    main()


print('первый-коммит')