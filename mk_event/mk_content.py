__author__ = "VioLet"
import random

def content_event(driver, contentX_max, contentX_min, contentY_max, contentY_mim):

    x = random.randint(0,contentX_max) % (contentX_max - contentX_min + 1) + contentX_min
    y = random.randint(0,contentY_max) % (contentY_max - contentY_mim + 1) + contentY_mim
    print('[ RUN ] sending Event : Content->( %s , %s )' %(x, y))
    json = [(x, y), ]
    driver.tap(json)
    return True