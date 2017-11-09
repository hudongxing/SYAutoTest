__author__ = "VioLet"

import random

def submit_event(driver, submitX_max, submitX_mim, submitY_max, submitY_mim):

    x = random.randint(0,submitX_max) % (submitX_max - submitX_mim + 1) + submitX_mim
    y = random.randint(0,submitY_max) % (submitY_max - submitY_mim + 1) + submitY_mim
    print('[ RUN ] sending Event : Submit->( %s , %s )' %(x, y))
    json = [(x, y),]
    driver.tap(json)
    return True