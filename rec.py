# def num(n):
#     sum = 0
#     while n != 0:
#         sum = sum + (n % 10)
#         n = n // 10
#         print(n)
#     return sum
#
# num(112)

# def sumofdigit(n):
#     if n == 0:
#         return 0
#     else:
#         return n % 10 + sumofdigit(n // 10)
#
#
# print(sumofdigit(112))


# power of number

# decimal to binary
#
# def dec_bin(n):
#     if n == 0:
#         return 0
#     else:
#         return n % 2 + 10 * dec_bin(int(n / 2))
#
#
# print(dec_bin(10))

# def dec(n):
#     q = []
#     while n != 0:
#         n = int(n) // 2
#         q.append(int(n))
#     r = [str(i % 2) for i in q]
#     return int(''.join(r))
#
#
# print(dec(10))

string = "abcd"

# new = ""
# for i in string:
#     new=i+new
# print(new)

# print(string[0:-1])


#
# def rev(string):
#     if len(string) <= 1:
#         return string
#     return string[-1] + rev(string[0:-1])
#
#
# print(rev(string))
# string = 'abaaba'
#
# print(string[0:-1])
# def palindrm(string):
#     if len(string) == 0:
#         return True
#     elif string[0] != string[-1]:
#         return False
#     return palindrm(string[1:-1])


# print(palindrm(string))


# # flatten
# def flatten1(arr):
#     result_array = []
#     for item in arr:
#         if isinstance(item, list):
#             result_array.extend(flatten(item))
#         else:
#             result_array.append(item)
#     return result_array
#
# def flatten(arr):
#     new = []
#     for i in arr:
#         if isinstance(i, list):
#             [new.append(item) for item in i]
#         else:
#             new.append(i)
#     return new
#
# print(flatten1(arr=[[1,2,3], [1,5,6], 1,2,3,4]))

# def cap(arr):
#     res = []
#     if len(arr) == 0:
#         return res
#     res.append(arr[0][0].upper() + arr[0][1:])
#     return res+cap(arr[1:])

# def cap(arr):
#     res = []
#     [res.append(item[0].upper() + item[1:]) for item in arr]
#     return res
#
#
# print(cap(arr=['pritam', 'sujit']))
#
# def stringfy(obj):
#     newobj = obj
#     for key in newobj:
#         if isinstance(newobj[key], int):
#             newobj[key] = str(newobj[key])
#         if isinstance(newobj[key], dict):
#            newobj[key] = stringfy(newobj[key])
#
#     return newobj

# def collectstring(obj):
#     newobj = []
#     for key in obj:
#         if isinstance(obj[key], str):
#             newobj.append(obj[key])
#         if isinstance(obj[key], dict):
#             newobj += collectstring(obj[key])
#
#     return newobj


# nested object sum
obj = {
    "num": 2,
    "num1": 'qwe',
    'num3': {
        "n": 2,
        "m": 3,
        'c': {
            'd': 2,
            'v': {
                'g': 4,
                'h': [3]
            }
        }
    },
    'nk': 4

}

# def nestedSum(obj):
#     sum = 0
#     for i in obj:
#         if isinstance(obj[i], int):
#             sum += obj[i]
#         if isinstance(obj[i], dict):
#             sum += nestedSum(obj[i])
#         elif isinstance(obj[i], list):
#             for i in obj[i]:
#                 sum += i
#     return sum
#
#
# print(nestedSum(obj))

# find  a missing element
#
# a = [1, 2, 3, 4, 5, 6, 7, 9, 10]
# le = int(len(a))
# sum1 = (le+1)*(le+2)/2
# print(sum1-sum(a))
# print(sum(a))

# def findpairs(nums, target):
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             # while nums[i]!=nums[j]:
#             if nums[i] + nums[j] == target:
#                 print(i, j)
#
#
# print(findpairs(nums=[1, 2, 3, 4, 6], target=6))
#
import numpy as np

#
myarray = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# print(myarray)
# def rotate(myarray):
#     n = len(myarray)
#     for layer in range(n//2):
#         first = layer
#         last = n -layer -1
#         for i in range(first, last):
#             top = myarray[layer][i]
#             #move left edge element to top edge
#             myarray[layer][i] = myarray[-i-1][layer]
#             #move bottom edge  to left
#             myarray[-i - 1][layer] = myarray[-layer-1][-i-1]
#             #move right most element to bottom left
#             myarray[-layer - 1][-i - 1] = myarray[i][-layer-1]
#             #move top to right
#             myarray[i][-layer - 1] = top
#
#     return myarray
#
# def rotate(myarray):
#     n = len(myarray)
#     for layer in range(n // 2):
#         print(layer)
#         first = layer
#         last = n - layer - 1
#     for i in range(first, last):
#         top = myarray[layer][i]
#         # move down-left to top
#         myarray[layer][i] = myarray[-i - 1][layer]
#         myarray[-i - 1][layer] = myarray[-layer - 1][-i - 1]
#         myarray[-layer - 1][-i - 1] = myarray[i][-layer - 1]
#         myarray[i][-layer - 1] = top
#
#     return myarray


# mylist = [1,2,3,4]
# def middle(mylist):
#     return [i for i in range(mylist[1:-1])]
#
# print(middle(mylist))


# sum of diaglonal
# mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
#
# def diagno(mylist):
#     sum = 0
#     le = len(mylist)
#     for i in range(le):
#         print(mylist[i][i])
#
#         sum += mylist[i][i]
#     return sum
# print(mylist)
#
# print(diagno(mylist))

mylist = [84, 85, 87, 86, 87, 85, 90, 85, 83, 23, 45, 84, 1, 2, 0]


# def firstsecond(mylist):
#     size = len(mylist)
#
#     for i in range(size - 1):
#         for j in range(size - 1 - i):
#             if mylist[j] < mylist[j + 1]:
#                 temp = mylist[j]
#                 mylist[j] = mylist[j + 1]
#                 mylist[j + 1] = temp
#     print(mylist)
#     return [mylist[0], mylist[1]]
#
#
# print(firstsecond(mylist))


# def missing(li):
#     le = len(li)
#     sum1 = (le+1)*(le+2)//2
#     return sum1-sum(li)
# print(missing(li))
# def missing(li, count):
#     le = len(li)
#     sum1 = count * (count + 1) // 2
#     sum = 0
#     for i in li:
#         sum += i
#     return sum1 - sum
#
#
# print(missing(li, 6))
# li = [1, 2, 3, 4, 6,6]
# new = []
# for i  in li:
#     if i not in new:
#         new.append(i)
#
# print(new)

# li = [2, 3, 4, 3 ,5, -2, 5, 2,8, 9]
#
# for i in range(len(li)):
#     for j in range(i+1,len(li)):
#         if li[i] + li[j] == 7:
#             print(li[i], li[j])

# st = "pritam"
# print('-'.join([i for i in st[::-1]]))
# # print(st[0].upper()+st[1:-1]+st[-1].upper())
#
# sentence = 'Sally sells sea sea shells sea by the sea'
# new = sentence.split()
# for i in range(len(new)):
#     if new[i] == "sea":
#         new[i] = "ocean"
# print(' '.join(new))
#

# largest element

# max = a[0]
# for i in range(1,len(a)):
#     if a[i] > max:
#         max = a[i]
# print(max)


# rotate array by d elements

def rotatearray(arr, n, d):
    arr[:] = [i for i in range(d + 1, n + 1)] + [arr[i] for i in range(0, d)]
    return arr


a = [2, 3, 4, 1]

# def twosum(a, target):
#     edict = {}
#     for index,number in enumerate(a):
#         diff = target - number
#         if diff in edict:
#             return edict[diff], index
#         else:
#             edict[number] = index
#
#
# print(twosum(a, 4))

# buy stock and sell
prices = [7, 1, 5, 3, 6, 4]

#
# def stock(prices):
#     buy, sell = 0, 1
#     maxprofit = 0
#
#     while sell < len(prices):
#         if prices[buy] < prices[sell]:
#             profit = prices[sell] - prices[buy]
#             maxprofit = max(maxprofit, profit)
#         else:
#             buy = sell
#         sell += 1
#     return maxprofit
#
#
# print(stock(prices))


prices = [7, 1, 5, 3, 6, 4]


def maxprof(prices):
    buy = 0
    selling = 1
    profit = 0
    while selling < len(prices):
        if prices[buy] < prices[selling]:
            target = prices[selling] - prices[buy]
            profit = max(profit, target)
        else:
            buy = selling
        selling += 1
    return profit

print(maxprof(prices))
