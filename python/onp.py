#!/usr/bin/env python
# -*- coding: utf-8 -*-
# onp.py

from stos_obj import Stos  # modul


def czy_poprawne(onp):
    for el in onp:
        if el.isalpha():
            return False
    return True


def main(args):
    stos = Stos()
    onp = input(
        "Podaj wyrażenie ONP, oddzielająć oprerandy i operatory spacjami: \n")
    # 3 3 7 + * ---- (3+7)*3 = 30
    if not czy_poprawne(onp):
        print("Błąd wyrażenia!")
        return 0
    onp = onp.split(" ")

    for el in onp:
        if el.isdigit():
            stos.push(el)
        else:
            a = stos.pop()
            b = stos.pop()
            if el == '/' and a == '0':
                print("Nie dzielimy przez 0")
                return 0
            else:
                stos.push(str(eval(b + el + a)))

    print("Wynik: ", stos.pop())
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
