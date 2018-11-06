#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# reszta.py


def pobierzNominaly():
    nominaly = set([200, 100, 50, 20, 10, 5, 2, 1])
    n = int(input('Podaj nominal lub 0 aby zakonczyc:'))
    listaNm = []

    while n > 0:
        if n in nominaly:
            listaNm.append(n)
        else:
            print('Nie ma takiego nominału!')
        n = int(input('Podaj nominal lub 0 aby zakonczyc:'))

    listaNm.sort(reverse=True)  # sortowanie malejace
    return listaNm


def wydajReszte1(r, l):
    i = 0  # index nominału
    while r > 0:
        if r >= l[i]:
            ileNm = int(r / l[i])
            r -= ileNm * l[i]
            print('{} x {} zł'.format(ileNm, l[i]))
        i += 1


def wydajReszte2(r, l):
    i = 0  # index nominału
    liczbaNm = len(l)  # liczba nominałów
    while r > 0 and i < liczbaNm:
        while i < liczbaNm and r < l[i]:
            i += 1
        if i < liczbaNm and r >= l[i]:
            nominal = l[i]
            ileNm = int(r / nominal)
            if ileNm > l.count(nominal):
                ileNm = l.count(nominal)
            r -= ileNm * nominal
            for j in range(ileNm):
                l.remove(nominal)
                liczbaNm -= 1
            i = 0
            print("{} x {}".format(ileNm, nominal))
    if r > 0:
        print("Brak nominałów do wydania reszty z {} zł.".format(r))


def main(args):
    # listaNm = [200, 100, 50, 20, 10, 5, 2, 1]  # dostepne nominaly
    listaNm = pobierzNominaly()
    # print(listaNm)
    reszta = int(input('Podaj reszte: '))

    # wydajReszte1(reszta, listaNm)
    wydajReszte2(reszta, listaNm)

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
