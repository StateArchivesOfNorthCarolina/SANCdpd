"""
This module runs the CLI for SANCdpd.
"""

import conf
import logger as lg


def welcome():
    print("hello, world")
    print("SANCdpd (alpha version)")


def menu(branch=[]):
    if len(branch) == 0:
        print("MAIN MENU")


def startcli():
    welcome()
    conf.read()
    lg.begin()
    conf.validate()
    menu()


if __name__ == '__main__':
    startcli()
