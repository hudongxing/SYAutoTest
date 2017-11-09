__author__ = "VioLet"


def share_event(driver, width):

    x = width / 10
    y = 25
    print('[ RUN ] sending Event : Share->( %s , %s )' %(x, y))
    json = [(x, y)]
    driver.tap(json)
    return True