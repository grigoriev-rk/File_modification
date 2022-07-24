#HW 'Opening, reading and writing a file'

from pprint import pprint

def dict_cookbook_func(cookbook):                       # Func for task 1
    '''
The function takes the name of the file, opens it for reading, finds the name of the dish, determines the number of ingredients, 
then looks for the parameters of the ingredients written through a splitter and then collects all this into one dictionary, 
where the keys are the names of the dishes, the value is the ingredients and their parameters.
    '''
    with open(cookbook, encoding = 'utf-8') as file:
        book = {}
        for line in file:                 
            dish_name = line.strip() 
            ingridients = []
            for i in range(int(file.readline())): 
                dict_ingredients = {} 
                i1, i2, i3 = file.readline().split("|") 
                dict_ingredients['ingredient_name'] = i1.strip(' ')
                dict_ingredients['quantity'] = i2.strip(' ')
                dict_ingredients['measure'] = i3.strip(' \n') 
                ingridients.append(dict_ingredients)
            book[dish_name] = ingridients 
            file.readline()
    return (book)

def get_shop_list_by_dishes(cookbook, dishes, persons):     # Func for task 2
    '''
The function takes a dictionary which returns the dict_cookbook_func a list of dishes and the number of persons, 
then for dishes from the list print a dictionary of ingredients and their quantity for the required number of persons.
    '''
    dict_ingridient_list = {}
    for item in dishes:
        for keys, values in dict_cookbook_func(cookbook).items():
            if keys == item:
              for item__ in values:
                item__['quantity'] = float(item__['quantity']) * persons
                dict_ingridient_list[item__.pop('ingredient_name')] = item__
    pprint(dict_ingridient_list)

def read_file(files_list):              # Func for task 3
    '''
    The function opens each file from list, then returns two dictionaries with the contents and number of lines of content.
    '''
    content = {}
    lines_number = {}
    for item in files_list:
        with open(item, encoding = 'utf-8') as file:
            strings = []
            for line in file:
                strings.append(line.strip())
        lines_number[len(strings)] = item
        content[len(strings)] = strings
    return [content, lines_number]

def write_file(new_file, content_info):         # Func for task 3
    '''
    The function takes the return of the read_file function, sorts by the number of lines, adds the required information, and writes it to a new file.
    '''
    sorted_content = {}
    content = content_info[0]
    lines_number = content_info[1]
    with open(new_file, "w+") as file:
        sorted_keys = sorted(content, key=content.get, reverse=True)
        for key__ in sorted_keys:
            sorted_content[key__] = content[key__]
        for keys, items in sorted_content.items():
            for key_name, value_name in lines_number.items():
                if key_name == keys:
                    file.write(f'Название файла: {value_name} \n')
            file.write(f'Количество строк: {str(keys)} \n')
            for _ in items:
                file.write(f'{_} \n')
            file.write('\n')
    return 0

  
print('\tЗадача №1, вывод словаря со списком рецептов\n')   # Task 1
pprint(dict_cookbook_func("recipes.txt"))

dishes = ['Утка по-пекински', 'Запеченный картофель']       # Task 2
persons = 4
print('\n\tЗадача №2, вывод словаря со списком требуемых ингридиентов для блюд\n')
get_shop_list_by_dishes("recipes.txt", dishes, persons)

files_list = ['1.txt', '2.txt', '3.txt']                    # Task 3
new_file = '123.txt'
print('\n\tЗадача №3, объединение файлов')  
content_info = read_file(files_list)
write_file(new_file, content_info)
print(f'\nФайлы {files_list} объединены, создан новый файл {new_file}!')
