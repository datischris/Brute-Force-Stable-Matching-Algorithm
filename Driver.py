import sys
from Utility import Utility
from Solution import Solution

class Driver:

    def __init__(self):
        if len(sys.argv) < 2:
            print("Please provide the testcase filepath as a command line argument")
            return
        input = Utility().read_file(sys.argv[1])
        s = Solution(len(input.women_preferences), input.women_preferences, input.men_preferences)
        sol = s.output_stable_matchings()
        for match in sol: #Sort by women 
            match.sort()
        sol.sort() #sorting across differnt matchings
        print(len(sol))
        for m in sol:
            print(m)

Driver()
