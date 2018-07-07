# -*- coding:utf-8 -*-

class Solution():

    def solve(self, x):
        result = []
        for i in range(1, x+1):
            result.append(self.Nicol(i))
        print(result)
        return result
        pass

    def Nicol(self, x):
        num = x**3
        result = []
        i = 1
        while i <= num:
            result = []
            if i%2 != 0:
                flag = 0
                sum = 0
                j = i
                while j <= num:
                    sum = sum + j
                    result.append(j)
                    j = j + 2
                    if sum > num:
                        flag = 0
                        break
                    elif sum == num:
                        flag = 1
                        break
                if flag == 1:
                    break
            i = i + 1
        return result