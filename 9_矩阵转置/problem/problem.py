# -*- coding:utf-8 -*-
import numpy as np
class Solution():
    def solve(self, x):
        arr = np.array(x)
        #注意arr.T后失去了tolist()方法
        transpose_arr = arr.T
        result_array = np.array(transpose_arr)
        result = result_array.tolist()
        print(result)
        return result
        pass