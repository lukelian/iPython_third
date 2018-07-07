# -*- coding:utf-8 -*-
import sys
import imp
import unittest
import math
from unittest2 import mc_unittest
from unittest2 import timeout

CODE_PATH = ''


class MTestCase(unittest.TestCase):

    # initial the test_class object
    def setUp(self):
        unittest.TestCase.setUp(self)
        test_module = imp.load_source('module', CODE_PATH)
        self.test_class = test_module.Solution()

    # destroy the test_class object
    def tearDown(self):
        unittest.TestCase.tearDown(self)
        self.test_class = None

    # common test
    @timeout.timeout(seconds=10)
    def test_isprime_common(self):
        """score:70"""
        A = [138,632,458,345,121,543,232,921,130,421]
        output = self.test_class.solve(A)
        expected_output = [[121, 130], [232, 421], [632], [138, 345, 543, 921], [458]]
        self.assertEqual(output, expected_output,
                         'Input: ' + str(A) + ', Expected Output: ' + str(expected_output) + ', Output: ' + str(output))



if __name__ == '__main__':
    CODE_PATH = sys.argv[1]
    mc = mc_unittest.MC_Unittest(MTestCase)
    mc.run_testcase()