# -*- coding:utf-8 -*-

class Solution():
    def solve(self, x):
        x.sort()
        l = x
        flag = 0
        for num in l:
            if num == 0:
                flag = 1
        if flag == 1:
            print(len(l))
            for i in range(len(l)):
                if l[i] != 0:
                    l[0] = l[i]
                    l[i] = 0
                    break
        strl = [ str(i) for i in l ]
        result = ""
        t = result.join(strl)
        #输出为str
        print(t)
        return t
        pass