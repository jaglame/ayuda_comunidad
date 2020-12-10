# -*- coding: utf-8 -*-


def run():
    """ """

    f = open("data.txt", "r")

    data = f.read()

    # texto = u"áéióúñ - " + data  # <- UnicodeDecodeError: 'ascii' codec can't decode byte 0xc3 in position 0: ordinal not in range(128)
    texto = u"áéióúñ - " + data.decode("utf-8")  # OK

    print(texto)


    f.close()



run()
