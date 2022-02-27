import unittest
import adshopcart_methods as methods
import adshopcart_locators as locators

class AdShopAppPositiveTestCases(unittest.TestCase):

    @staticmethod
    def new_test():
        methods.setUp()
        methods.tearDown()
