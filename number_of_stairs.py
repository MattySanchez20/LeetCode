import math as maths


class Solution(object):

    def climbStairs(self, n: int):
        """
        You are climbing a staircase. It takes n steps to reach the top.

        Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
        """
        self.n = n

        try:
            if n >= 1 and n <= 45:

                # calculating the maximum number of times 2 appears
                max_two = maths.floor(n/2)

                # Total Combinations variable to store number of combinations
                tot_comb = 0

                # looping through 0 to maximum number of 2s
                for i in range(0, max_two+1):

                    # Choose function to work out all combinations possible
                    combos = maths.comb(n - i, i)

                    # tracking number of combos calculated
                    tot_comb += combos

                return tot_comb
            else:
                return "Number of Steps Should be Between 1 and 45"
        except TypeError:
            return 'Please Enter a Number'
