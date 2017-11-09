__author__ = "VioLet"


def tap_point_event(driver, special_point_x, special_point_y):
    print('[ RUN ] sending SpecialPoint Tap Event : Tap->( %s , %s )' %(special_point_x,special_point_y))
    json = [(special_point_x, special_point_y),]
    driver.tap(json)
    return True
