'''
Lonely Number
Given a non-empty array of integers where every element appears twice except for one. 
Find that single number.
Assume that there will always be one odd-number-out
and every other number in the input shows up exactly twice.

Examples
Sample input: [2, 2, 1]
Expected output: 1
Sample iput: [4, 1, 2, 1, 2]
Expected output: 4
Implement a solution that finds the single number in
one pass through the input array with O(1) space complexity

Input: a List of integers where every int except one shows up twice
Returns: an integer
Uncomment code and begin!
'''
from collections import Counter
import time

# def lonelyNumber(arr):
#     # Your code here


# if __name__ == '__main__':
#     # Use the main function to test your implementation
#     arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

#     print(f"The lonely number is {lonelyNumber(arr)}")