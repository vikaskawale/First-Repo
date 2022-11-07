'''Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

Example
arr = [1, 3, 5, 7, 9]
The minimum sum is 1+3+5+7 = 16 and the maximum sum is 3+5+7+9 = 24 . The function prints 16 24'''
# By Vikas Kawale

def miniMaxSum(arr):
    # Write your code here
    print('Min sum is: ', sum(arr)-max(arr))
    print('Max sum is: ', sum(arr)-min(arr))
arr = list(map(int, input('Enter 5 numbers: ').rstrip().split()))

miniMaxSum(arr)
