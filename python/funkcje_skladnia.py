#!/usr/bin/env python
# -*- coding: utf-8 -*-

a, b = 5, 10
print('5:', a + b)
# zmienna globalna (variable)
# zasieg globalny (global)
# przestrzeń nazw modułu (namespace)
# print(a,b)


def sumuj1():  # tworzy nowa przestrzen nazw, przestrzen funkcji
    print('13: Suma z funkcji:', a + b)


def main(args):
    global a, b
    a, b = 2, 3  # zmienne lokalne, zasieg lokalny, przestrzen funkcji
    print("17 ,Suma z main:", a + b)
    sumuj1()  # wywolanie funkcji


def odejmij(x, y): # a,b - parametry pozycyjne
    print(x - y)
    x, y = 4, 3

def odejmij2(lista):
    lista.append(lista[0] - lista[1])


def main2(args):
    # a, b = 2, 3  # zmienne lokalne, zasieg lokalny, przestrzen funkcji
    # print(a - b)
    # odejmij(a, b)  # wywolanie funkcji
    # print(a - b)
    l = [3, 4]
    odejmij2(l)
    print(l)

    return 0

# print("po:", a, b)


if __name__ == '__main__':
    # skrypt został uruchomiony a nie zaimportowany
    import sys
    sys.exit(main2(sys.argv))
