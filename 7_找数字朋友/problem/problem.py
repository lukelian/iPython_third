# -*- coding:utf-8 -*-

class Solution():
    def solve(self, x):
        dict = {}
        for num in x:
            list_num_str = list(str(num))
            list_num = [int(i) for i in list_num_str]
            list_sum = sum(list_num)
            if list_sum in dict:
                dict_list = dict[list_sum]
                dict_list.append(num)
                dict.update({list_sum:dict_list})
            else:
                dict_list = [num]
                dict.update({list_sum:dict_list})

        keys = list(dict.keys())
        keys.sort()
        result = []
        for key in keys:
            key_list = dict[key]
            key_list.sort()
            result.append(key_list)
        print(result)
        return result
        pass