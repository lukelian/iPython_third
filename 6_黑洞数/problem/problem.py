# -*- coding:utf-8 -*-
from functools import reduce
class Solution():
    def solve(self, x):
        result = []
        while(True):
            list_origion = list(str(x))
            list_origion_num = [int(i) for i in list_origion]

            list_origion_num.sort()
            list_sort_min = list_origion_num
            num_list_min = [int(i) for i in list_sort_min]
            minsum = reduce(lambda x ,y : 10 * x + y, num_list_min)

            list_origion_num.sort(reverse=True)
            list_sort_max = list_origion_num
            num_list_max = [int(i) for i in list_sort_max]
            maxsum = reduce(lambda x, y : 10 * x + y, num_list_max)

            if len(str(minsum)) < 4:
                len_temp = 4 - len(str(minsum))
                minsum = '0'*len_temp + str(minsum)
            if len(str(maxsum)) < 4:
                len_temp = 4 - len(str(maxsum))
                maxsum = str(maxsum) + '0'*len_temp

            Difference = int(maxsum) - int(minsum)

            str_result = str(maxsum) + "-" + str(minsum) + "=" + str(Difference)
            result.append(str_result)
            print(str(maxsum) + "-" + str(minsum) + "=" + str(Difference))
            if (Difference == 6174)|(Difference == 0):
                break
            x = Difference
        print(result)
        return result
        pass