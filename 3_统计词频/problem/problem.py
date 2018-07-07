# -*- coding:utf-8 -*-

class Solution():
    def solve(self, x):
        arrStr = x.lower().split()
        dict = {}
        for i in range(len(arrStr)):
            str = arrStr[i]
            str = str.strip('.')
            if str in dict:
                temp = dict[str]
                temp = temp + 1
                dict.update({str:temp})
            else:
                dict.update({str:1})
        list = []
        for key, value in dict.items():
            list.append((key, value))
        s = set(list)
        print(s)
        return s
        pass