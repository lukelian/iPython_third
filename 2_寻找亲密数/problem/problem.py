# -*- coding:utf-8 -*-

class Solution():
    def solve(self, x):
        result = []
        for i in range(1, x):
            res = self.check(i)
            if i!=res and self.check(res)==i:
                #temp = [i, res]
                temp = (i, res)
                result.append(temp)
        resultSet = set(result)
        print(resultSet)
        return resultSet
        pass

    def check(self, n):
        '''
        计算各因子之和模块
        '''
        s = 0
        for i in range(1, int(n / 2) + 1):
            if n % i == 0:
                s += i
        return s