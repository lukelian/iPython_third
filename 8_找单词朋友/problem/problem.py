# -*- coding:utf-8 -*-

class Solution():
    def solve(self, x):
        dict = {}
        result_list = []
        for word in x:
            list_word = list(word)
            list_word.sort()
            list_word_sorted = "".join(list_word)
            if list_word_sorted in dict:
                value = dict[list_word_sorted]
                #注意元组一个元素的时候要加逗号
                temp = (word,)
                #注意元组添加元素的两种常用操作的区别，一种是value = (value, x)，另一种是value = value + x
                value = value + temp
                dict.update({list_word_sorted : value})
            else:
                value = (word,)
                dict.update({list_word_sorted : value})
        for key,value in dict.items():
            result_list.append(value)
        #list是unhash的，因此得用tuple存储
        result = set(result_list)
        print(result)
        return result
        pass
