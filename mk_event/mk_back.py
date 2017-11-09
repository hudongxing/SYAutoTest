__author__ = "VioLet"


def bake_event(driver, backX, backY):
    print('[ RUN ] sending Event : Back->( %s , %s )' %(backX, backY))
    json = [(backX, backY),]
    driver.tap(json)
    return True