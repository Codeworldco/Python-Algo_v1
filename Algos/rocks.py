"""
SpongBob can eat either 1, 2, or 3 crabby_patties at a time. If he were given a plate
of crabby_patties with n crabby_patties on it, how many ways could he eat all
n crabby_patties on the plate? 

Implement a function eating_crabby_patties that counts 
the number of possible ways SpongBob can eat all of the crabby_patties on the plate.

For example, for a plate of crabby_patties with n = 3 
(the plate has 3 crabby_patties on it), there are 4
possible ways for SpongBob to eat all the crabby_patties on it at a time:

He can eat 1 crabby_pattie at a time 3 times [1..2..3] 
He can eat 1 crabby_pattie, then 2 crabby_patties
He can eat 2 crabby_patties, then 1 crabby_pattie
He can eat 3 crabby_patties all at once.
****Thus, eating_crabby_patties(3) should return an answer of 4.

implement a solution that runs fast enough to pass the  input test below 

Input: an integer
Returns: an integer

uncomment code and begin!
"""


# def eating_crabby_patties(n):
#     # Your code here


# if __name__ == "__main__":
#     # Use the main function here to test out your implementation
#     num_crabby_patties = 7
   

#     print(f'There are {eating_crabby_patties(num_crabby_patties)} ways for SpongeBob to eat {num_crabby_patties} crabby patties')