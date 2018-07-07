# -*- coding:utf-8 -*-

class Solution():
    def solve(self, s, flag, n):
        if n>len(s):
            return 'the value of n is too big'
        if flag == 1:
            subs = s[:n]
            subs_remain = s[n:]
            subs_reverse = subs[::-1]
            result = subs_remain + subs
            print(result)
            return result
        else:
            subs = s[-n:]
            subs_remain = s[:len(s) - n]
            result = subs + subs_remain
            print(result)
            return result
        pass