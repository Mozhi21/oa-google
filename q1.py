"""
给一个数列，一次可以让连续的分段加1， 问要怎么才能从000变成给的数列
213： 000 111 211 212 213
单调栈， 当你遇到的数减小的时候，就可以吧之前坑填上了
遍历完以后再把stack里剩的填了
"""

def minimum_move(arr):
    stack =[]
    total_move = 0

    for i in arr:
        while stack and i <= stack[-1]:
            total_move += (stack[-1] - i)
            stack.pop()
        stack.append(i)
    
    total_move += stack[-1]

    return total_move

print(minimum_move([2,1,3]))
print(minimum_move([2,1,3,1]))
print(minimum_move([2,1,3,1,0,2]))
print(minimum_move([2,0,1,2]))

