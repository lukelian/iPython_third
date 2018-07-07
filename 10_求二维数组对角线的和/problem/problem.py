# -*- coding:utf-8 -*-

class Solution():
    def solve(self, x):
        sum = 0
        count = 0
        rows_count = len(x)
        flag = 0
        if rows_count%2 != 0:
            flag = 1
        for i in range(rows_count):
            sum = sum + x[i][count] + x[i][-(count + 1)]
            count = count + 1
        if flag ==1: #奇数行
            #print(int(rows_count/2))
            t = int(rows_count / 2)
            sum = sum - x[t][t]
        print(sum)
        return sum
        pass