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
        A = "Hope is a good thing and maybe the best of things. And no good thing ever dies."
        output = self.test_class.solve(A)
        expected_output = {('things', 1), ('ever', 1), ('maybe', 1), ('and', 2), ('the', 1), ('of', 1), ('best', 1), ('hope', 1), ('is', 1), ('a', 1), ('thing', 2), ('good', 2), ('dies', 1), ('no', 1)}
        self.assertEqual(output, expected_output,
                         'Input: ' + str(A) + ', Expected Output: ' + str(expected_output) + ', Output: ' + str(output))


if __name__ == '__main__':
    CODE_PATH = sys.argv[1]
    mc = mc_unittest.MC_Unittest(MTestCase)
    mc.run_testcase()