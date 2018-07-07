# -*- coding:utf-8 -*-

class Solution():
    def solve(self, num, n):
        num_rep = {2: '2',
                   3: '3',
                   4: '4',
                   5: '5',
                   6: '6',
                   7: '7',
                   8: '8',
                   9: '9'}
        new_num_string = ''
        current = num
        while current != 0:
            remainder = current % n
            if 10 > remainder > 1:
                remainder_string = num_rep[remainder]
            elif remainder >= 10:
                remainder_string = '(' + str(remainder) + ')'
            else:
                remainder_string = str(remainder)
            new_num_string = remainder_string + new_num_string
            current = int(current / n)
        result = str(num) + "=" + "(" + new_num_string + ")" + str(n)
        print(result)
        return result