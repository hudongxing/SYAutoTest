__author__ = "VioLet"
from appium import webdriver

from math_random import random_math
from mk_event.mk_back import bake_event
from mk_event.mk_content import content_event
from mk_event.mk_tap import tap_event
from mk_event.mk_swipe import swipe_event
from mk_event.mk_submit import submit_event
from mk_event.mk_tap_point import tap_point_event
from mk_event.mk_share import share_event
from mk_event.mk_home import home_event
from mk_event.mk_launch import launch_event


class Appium:
    driver = None

    def __init__(self):

        self.backX = 25
        self.backY = 40

        self.driver = webdriver.Remote(
                command_executor='http://127.0.0.1:4723/wd/hub',
                desired_capabilities={
                    'automationName': "xcuitest",
                    'platformName': 'iOS',
                    'platformVersion': '10.3.2',
                    'deviceName': 'iphone 7Plus',
                    'bundleId': 'com.uni-cocloud.emoHome',
                    'udid': '3eb2d8922537303ac252997f48523d04813b1df6'
                })

    def info(self):

        Appium().run_event()

    def run_event(self):

        eventfun = 0
        width = self.driver.get_window_size().get('width')
        height = self.driver.get_window_size().get('height')
        submitX_max = width - 1
        submitX_mim = width / 10
        submitY_max = height - 1
        submitY_mim = height / 10 * 9

        contentX_max = width - width / 10
        contentX_mim = width / 10
        contentY_max = height / 2 + height / 10
        contentY_mim = height / 2 - height / 10

        special_point_x = width / 2
        special_point_y = int(height * 0.94)
        while True:
            num = random_math().percentage_random()
            if num == 0:
                tap_event(self.driver, width, height)

            elif num == 1:
                swipe_event(self.driver, width, height)

            elif num == 2:
                bake_event(self.driver, self.backX, self.backY)

            elif num == 3:
                submit_event(self.driver, submitX_max, submitX_mim, submitY_max, submitY_mim)

            elif num == 4:
                content_event(self.driver, contentX_max, contentX_mim, contentY_max, contentY_mim)

            elif num == 5:
                tap_point_event(self.driver, special_point_x, special_point_y)

            elif num == 6:
                share_event(self.driver, width)
            elif num == 7:
                home_event(self.driver, "3eb2d8922537303ac252997f48523d04813b1df6", "com.uni-cocloud.emoHome")

            eventfun += 1

            print('[ RUN ] Event number:  %d ' % eventfun)


if __name__ == "__main__":
    testRun = Appium()
    testRun.info()
