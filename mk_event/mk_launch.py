__author__ = "VioLet"

import os,time,threading


def launch_event(driver, udid, bundleId):
    def Tread():
        print('[ RUN ] sending launch Event.')
        try:
            time.sleep(2)
            os.system('pkill -9 idevicedebug')
            print('[ RUN ] idevicedebut stop')
        except Exception as e:
            print('\n[ ERROR ] '+str(e) + '\n')
    threading.Thread(target=Tread).start()

    print('[ RUN ] launch App : ' + bundleId)
    try:
        os.system('idevicedebug -u %s run %s' %(udid, bundleId))
        time.sleep(3)
        return True
    except Exception as e:
        print('\n[ ERROR ] '+str(e) + '\n')
