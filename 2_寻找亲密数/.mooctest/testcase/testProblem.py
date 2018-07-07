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
    @timeout.timeout(seconds=60)
    def test_isprime_common(self):
        """score:70"""
        A = 20000
        output = self.test_class.solve(A)
        expected_output = {(10744, 10856), (10856, 10744), (1184, 1210), (14595, 12285), (17296, 18416), (18416, 17296), (1210, 1184), (284, 220), (220, 284), (5020, 5564), (5564, 5020), (6368, 6232), (6232, 6368), (12285, 14595), (2620, 2924), (2924, 2620)}
        self.assertEqual(output, expected_output,
                         'Input: ' + str(A) + ', Expected Output: ' + str(expected_output) + ', Output: ' + str(output))


if __name__ == '__main__':
    CODE_PATH = sys.argv[1]
    mc = mc_unittest.MC_Unittest(MTestCase)
    mc.run_testcase()