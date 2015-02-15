# coding=utf-8
__author__ = 'Eva Sokolyanskaya'

import random
import os
import codecs
import sys

extensions_list_file = 'ExtensionsList.txt'
predefined_extensions_names = ['1)  Таверны и Соборы',
                               '2)  Купцы и Строители',
                               '3)  Король (и Атаман)',
                               '4)  Принцесса и Дракон',
                               '5)  Башня',
                               '6)  Аббат и Мэр',
                               '7)  Граф',
                               '8)  Культ',
                               '9)  Река',
                               '10) Круги на полях',
                               '11) Летательные аппараты',
                               '12) Маг и Ведьма',
                               '13) Гонцы',
                               '14) Грабители',
                               '15) Паромы',
                               '16) Золотые рудники']


def gen(including_extensions_count=4, my_file=extensions_list_file):
    if os.path.isfile(my_file):
        extensions_names_list = get_extensions_list_from_file(my_file)
    else:
        extensions_names_list = predefined_extensions_names
    extensions_list_length = len(extensions_names_list)

    # if including_extensions_count <= extensions_list_length or not str(including_extensions_count).isdigit:
    if including_extensions_count in range(1, extensions_list_length + 1):
        extensions_numbers = range(1, extensions_list_length + 1)

        including_extensions_numbers_list = random.sample(extensions_numbers, including_extensions_count)
        including_extensions_numbers_list.sort()

        # print including_extensions_numbers_list
        print_including_extensions_list(including_extensions_numbers_list, extensions_names_list)

    else:
        print_count_error_message(including_extensions_count, extensions_list_length)


def print_including_extensions_list(including_extensions_numbers_list, extensions_names):
    for extension in including_extensions_numbers_list:
        number = int(extension)
        print extensions_names[number-1]


def get_extensions_list_from_file(file_name):
        with codecs.open(file_name, 'r', encoding='utf8') as f:
            all_extensions_list = f.read().splitlines()
            clean_list = []
            for line in all_extensions_list:

                if len(line) != 0:
                    if ord(line[0]) == 65279:
                        line = line[1:]
                    clean_list.append(line)
        # print unichr(65279)   # this char appears in the beginning of .txt file
        return clean_list


def print_count_error_message(count, list_size):
    output_string = 'You want {} extentions from list of {}. \nIt is impossible :-( ' \
                    '\nChoose number between 1 and {}, please.'.format(count, list_size, list_size)
    print output_string

if __name__ == '__main__':
    if len(sys.argv) == 1:
        gen()

    elif len(sys.argv) == 2:
        try:
            gen(int(sys.argv[1]))
        except ValueError:
            print 'Your first argument should be integer'

    # elif len(sys.argv) == 3:
    #     print '3 args ', sys.argv[1]
    #     try:
    #         gen(sys.argv[1], sys.argv[2])
    #     except ValueError:
    #         print 'Your first argument should be integer'