问题：
循环移动子串
知识点：算法，函数
题目描述：自定义函数solve(s, flag, n)，将传入的字符串s按照flag（1代表循环左移，2代表循环右移）的要求左移或右移n位（例如对于字符串S1S2S3S4S5，循环左移两位后的结果为S3S4S5S1S2，循环右移两位后的结果为S4S5S1S2S3）。
输入字符串、左移和右移标记以及移动的位数，若移动位数合理则将移动后的字符串输出，否则，返回结果“the value of n is too big”。
[输入样例1]
'I love Python',1,3
[输出样例1]
ove PythonI l
[输入样例2]
'I love Python',2,3
[输出样例2]
honI love Pyt
[输入样例3]
'I love Python',1,15
[输出样例3]
the value of n is too big

注：所有结果以字符串类型返回