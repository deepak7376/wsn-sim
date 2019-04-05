#!/usr/bin/env python3
from timeitd import timeit
from time import sleep


@timeit(number=100, unit="ns")
def testfunc():
    sleep(0.001)
