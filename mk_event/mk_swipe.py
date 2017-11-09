__author__ = "VioLet"


import math, random


def swipe_event(driver, width, height):
    startX = math.ceil(random.random() * (width - 1))
    startY = math.ceil(random.random() * (height - 1))
    entY = math.ceil(random.random() * (height - 1))
    print('[ RUN ] sending Swipe Event : Swipe-> [start(%s , %s ), end( %s , %s)]' %(startX, startY, startX, entY))

    driver.swipe(startX, startY, startX, entY, 1)
    return True
