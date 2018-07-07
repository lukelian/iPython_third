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
        A = 8
        output = self.test_class.solve(A)
        expected_output = [[1], [3, 5], [7, 9, 11], [1, 3, 5, 7, 9, 11, 13, 15], [21, 23, 25, 27, 29], [7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29], [43, 45, 47, 49, 51, 53, 55], [17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]]
        self.assertEqual(output, expected_output,
                         'Input: ' + str(A) + ', Expected Output: ' + str(expected_output) + ', Output: ' + str(output))

    # test input array with other item
    @timeout.timeout(seconds=10)
    def test_isprime_other(self):
        """score:30"""
        A = 1
        output = self.test_class.solve(A)
        expected_output = [[1]]
        self.assertEqual(output, expected_output,
                         'Input: ' + str(A) + ', Expected Output: ' + str(expected_output) + ', Output: ' + str(output))


if __name__ == '__main__':
    CODE_PATH = sys.argv[1]
    mc = mc_unittest.MC_Unittest(MTestCase)
    mc.run_testcase()