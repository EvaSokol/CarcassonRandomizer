# coding=utf-8
__author__ = 'Eva Sokolyanskaya'

import random
import sys

'''format of extension record:
    [0] name
    [1] fields to add
    [2] other objects to add
    [3] length of name (to nice output, because og cyrillic issue)
    [4] -1 if base square numbers should be decreased
'''
predefined_extensions = [
                        ('1)  \'Таверны и Соборы\'', 18, 'Big followers', 16, 0),
                        ('2)  \'Купцы и Строители\'', 24, 'Pigs, Builders, Goods tokens', 17, 0),
                        ('3)  \'Король (и Атаман)\'', 5, 'King and Chieftain tokens', 17, 0),
                        ('4)  \'Принцесса и Дракон\'', 30, 'Fairy and Dragon', 18, 0),
                        ('5)  \'Башня\'', 18, 'Tower elements', 5, 0),
                        ('6)  \'Аббат и Мэр\'', 12, 'Mayors, Storehouses, Wagons, Abbey-squares', 11, 0),
                        ('7)  \'Граф\'', 12, 'Earl', 4, -1),
                        ('8)  \'Культ\'', 5, '', 5, 0),
                        ('9)  \'Река\'', 12, '', 4, -1),
                        ('10) \'Круги на полях\'', 12, '', 14, 0),
                        ('11) \'Летательные аппараты\'', 8, 'Cube', 20, 0),
                        ('12) \'Маг и Ведьма\'', 8, 'Wizard ans Witch', 12, 0),
                        ('13) \'Гонцы\'', 0, 'Messengers, 8 messages', 5, 0),
                        ('14) \'Грабители\'', 8, 'Robbers', 9, 0),
                        ('15) \'Паромы\'', 8, '8 ferry-tokens', 6, 0),
                        ('16) \'Золотые рудники\'', 8, '16 golden-tokens', 15, 0),
                        ('17) \'Колесо Фортуныэ\'', 88, 'Pink Pig, tablet, 72 special base squares', 15, 0),
                        ('18) \'Мосты, замки и базары\'', 12, 'Bridges and Castles', 21, 0),
                        ('19) \'Холмы и овцы\'', 18, '2 wolves, 16 sheeps, 6 shepherds, bag', 12, 0),
                        ('20) \'Бродячий цирк\'', 20, '16 animals, 1 tent, 6 circus chefs', 13, 0)
                         ]


def gen(including_extensions_count=20):
    extensions_list_length = len(predefined_extensions)

    if including_extensions_count in range(1, extensions_list_length+1):

        including_extensions_numbers_list = random.sample(range(0, extensions_list_length), including_extensions_count)
        including_extensions_numbers_list.sort()

        # print including_extensions_numbers_list
        print_including_extensions_list(including_extensions_numbers_list)

    else:
        print_count_error_message(including_extensions_count, extensions_list_length)


def print_including_extensions_list(including_extensions_numbers_list):
    additional_squares_number = 0
    base_squares = 72
    for extension in including_extensions_numbers_list:
        additional_squares_number += predefined_extensions[extension][1]
        if predefined_extensions[extension][4] < 0 and base_squares >= 72:
            base_squares -= 1

        blanks = 25-predefined_extensions[extension][3]

        output_string = '{}'.format(predefined_extensions[extension][0]) + '.'*blanks\
            + ' {:2} squares ... and ... {}'.format(predefined_extensions[extension][1], predefined_extensions[extension][2])

        print(output_string)
    print('Base squares ', base_squares)
    print('Total number of squares is {}'.format(base_squares + additional_squares_number))
    # print squares_number


def print_count_error_message(count, list_size):
    output_string = 'You want {} extentions from list of {}. \nIt is impossible :-( ' \
                    '\nChoose number between 1 and {}, please.'.format(count, list_size, list_size)
    print(output_string)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        gen()

    elif len(sys.argv) == 2:
        # print 'second arg: ', int(sys.argv[1])
        try:
            gen(int(sys.argv[1]))
        except ValueError:
            print('Your first argument should be integer')





