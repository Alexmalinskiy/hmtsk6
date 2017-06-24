def read_receipt_file():
    cook_book = {}
    with open("receipt.txt", encoding="utf8") as file:
        for line in file:
            tempname = line.strip().replace("\n", "").lower()
            cook_book[tempname] = []
            for i in range(int(file.readline().strip().replace("\n", ""))):
                data = file.readline().strip().replace("\n", "").split(" | ")
                cook_book[tempname].append({"ingr_name": data[0], "quantity": int(data[1]), "measure": data[2]})
    return cook_book


def get_shop_list_by_dishes(cook_book, dishes, person_count):
    shop_list = {}
    for dish in dishes:
        dish = dish.strip()
        try:
            for ingredient in cook_book[dish]:
                new_shop_list_item = ingredient
                new_shop_list_item['quantity'] *= person_count
                if new_shop_list_item['ingr_name'] not in shop_list:
                    shop_list[new_shop_list_item['ingr_name']] = new_shop_list_item
                else:
                    shop_list[new_shop_list_item['ingr_name']]['quantity'] += new_shop_list_item['quantity']
        except KeyError:
            print("Блюдо {0} не найдено".format(dish))
            continue
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingr_name'], shop_list_item['quantity'],
                                shop_list_item['measure']))


def create_shop_list():
    cook_book = read_receipt_file()
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ').lower().split(',')
    shop_list = get_shop_list_by_dishes(cook_book, dishes, person_count)
    print_shop_list(shop_list)


if __name__ == '__main__':
      create_shop_list()
