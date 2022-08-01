# coding=utf-8
__author__ = 'Eva Sokolyanskaya'

import random
import sys
import csv


class Extension:
    def __init__(self, title_ru, title_eng, title_ukr, squares, elements, base_square_used=True):
        self.title_ru = title_ru
        self.title_eng = title_eng
        self.title_ukr = title_ukr
        self.squares = squares
        self.elements = elements
        self.base_square_used = base_square_used


ext_list = []

# with open('Extensions.csv', encoding="utf8") as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=';')
#     for row in csv_reader:
#         ext_list.append(Extension(row[0], row[1], row[2], row[3], row[4], row[5]))

csv_srt = "Таверны и Соборы;;;18;Big followers;True\n" \
          "Купцы и Строители;;;24;Pigs, Builders, Goods tokens;True\n" \
          "Король (и Атаман);;;5;King and Chieftain tokens;True\n" \
          "Принцесса и Дракон;;;30;Fairy and Dragon;True\n" \
          "Башня;;;18;Tower elements;True\n" \
          "Аббат и Мэр;;;12;Mayors, Storehouses, Wagons, Abbey-squares;True\nГраф;;;12;Earl;False\n" \
          "Культ;;;5;;True\n" \
          "Река;;;12;;False\n" \
          "Круги на полях;;;12;;True\n" \
          "Летательные аппараты;;;8;Cube;True\n" \
          "Маг и Ведьма;;;8;The Wizard and the Witch;True\n" \
          "Гонцы;;;0;Messengers, 8 messages;True\n" \
          "Грабители;;;8;Robbers;True\nПаромы;;;8;8 ferry-tokens;True\n" \
          "Золотые рудники;;;8;16 golden-tokens;True\n" \
          "Колесо Фортуны;;;88;Pink Pig, tablet, 72 special base squares;False\n" \
          "Мосты, замки и базары;;;12;Bridges and Castles;True\n" \
          "Холмы и овцы;;;18;2 wolves, 16 sheeps, 6 shepherds, bag;True\n" \
          "Бродячий цирк;;;20;16 animals, 1 tent, 6 circus chefs;True"
reader = csv.reader(csv_srt.split('\n'), delimiter=';')
for row in reader:
    ext_list.append(Extension(row[0], row[1], row[2], row[3], row[4], row[5]))


def print_extension_ru(ext_object: Extension, max_name):
    out_str = '%s ...%s %s squares' % (ext_object.title_ru,
                                       '.' * (max_name - len(ext_object.title_ru)),
                                       '{:>2}'.format(ext_object.squares))
    if len(ext_object.elements) > 0:
        addings = ' ... and ... %s' % ext_object.elements
        out_str += addings
    print(out_str)


def print_including_extensions_list(extensions: Extension):
    additional_squares_number = 0
    base_squares = 72
    max_name = 0

    for ext in extensions:
        additional_squares_number += int(ext.squares)
        max_name = len(ext.title_ru) if len(ext.title_ru) > max_name else max_name
        if not ext.base_square_used:
            base_squares -= 1

    print('-' * 35, '\nBase squares ', base_squares)
    print('Total number of squares is {}\n{}'.format(base_squares + additional_squares_number, '-' * 35))
    for ext in extensions:
        print_extension_ru(ext, max_name)


def print_count_error_message(count, list_size):
    output_string = 'You want {} extensions from list of {}. \nIt is impossible :-( ' \
                    '\nChoose number between 1 and {}, please.'.format(count, list_size, list_size)
    print(output_string)


def gen(included_number=4):
    print('Total extensions number:', len(ext_list))
    total = len(ext_list)
    if included_number <= total:
        including_extensions_numbers_list = random.sample(ext_list, included_number)
        print_including_extensions_list(including_extensions_numbers_list)

    else:
        print_count_error_message(included_number, total)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        gen()

    elif len(sys.argv) == 2:
        try:
            gen(int(sys.argv[1]))
        except ValueError:
            print('Expected argument to be integer')
