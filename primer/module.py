#!/usr/bin/env python
# _*_ coding: utf-8 _*_

'Test module'

try:
    import cStringIO as StringIO
except ImportError:
    import StringIO

try:
    import json
except ImportError:
    import simplejson as json

import sys

__author__ = "kylingo"


def test():
    argv = sys.argv
    if len(argv) == 1:
        print ("Hello, world!")
    elif len(argv) == 2:
        print ("Hello, %s!" % argv[1])
    else:
        print ("Too many arguments!")


if __name__ == '__main__':
    test()


class Bike(object):
    # 限制类的属性
    __slots__ = ('name', 'price', '__level', '_color')

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.__level = 1

    def get_level(self):
        print ("bike get level")
        return self.__level

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    def run(self):
        print('Bike run')


class RunnableMixin(object):
    def run(self):
        print('RunnableMixin run')


class MountainBike(Bike, RunnableMixin):
    def get_level(self):
        super(MountainBike, self).get_level()
        return 2
