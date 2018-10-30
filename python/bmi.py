#!/usr/bin/env python
# -*- coding: utf-8 -*-


def bmi(m,w):
    return m / (w/100)**2


def main(args):

    masa = int(input('Podaj mase(kg):'))
    wzrost = int(input('Podaj wzrost(cm):'))
    a = bmi(masa, wzrost)
    print('BMI: {:.2f}'.format(a))
    if a >= 30:
        print('Otyłość')
    elif a >= 25:
        print('Nadwaga')
    elif a >= 18.5:
        print('Norma')
    else:
        print('Niedowaga')



    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
