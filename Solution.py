from Marriage import Marriage
from itertools import permutations

class Solution:

    def __init__(self, number, women, men):
        """
        The constructor exists only to initialize variables. You do not need to change it.
        :param number: The number of members
        :param men: The preference list of men, as a dictionary.
        :param women: The preference list of the women, as a dictionary.
        """
        self.num = number
        self.men = men
        self.women = women
        self.count = 0
        self.stable_matchings = []
    
    def determine_stability(self,pairs):
        for pair in pairs:
            m = pair.man()
            w = pair.woman()
            for other in pairs:
                mprime = other.man()
                wprime = other.woman()
                
                #preference list assertions
                mprefwprime = self.men[m].index(wprime) #current man's preference for other woman
                mpref = self.men[m].index(w) #current man's preference for current woman
                wprefm = self.women[wprime].index(m) #other woman's preference for current man
                wprimepref = self.women[wprime].index(mprime) #other womans's preference for other man

                #if current man's preference for other woman is higher than current woman AND the other woman's preference for current man is higher than other man
                if mprefwprime < mpref and wprefm < wprimepref: 
                    return 0
        return 1
                        

    def output_stable_matchings(self):
        perms = permutations(list((self.men).keys()),self.num)
        pairlist = list()
        r = list(range(0,self.num))

        for men in perms:
            for i in r:
                m = men[i]
                w = i + 1
                pairlist.append(Marriage(m,w))
     
            if self.determine_stability(pairlist) == 1:
                self.stable_matchings.append(pairlist)

            pairlist = list()

        return self.stable_matchings



    #potential solution 2
    '''
    def output_stable_matchings(self):

        perm = permutations(list((self.men).keys()),self.num)
        pairlist = list()
        r = list(range(0,self.num))
        unstabletick = 0

        for men in perm:
            for i in r:
                m = men[i]
                w = i + 1
                pairlist.append(Marriage(m,w))
            
            for pair in pairlist:
                m = pair.man()
                w = pair.woman()

                for other in pairlist:
                    mprime = other.man()
                    wprime = other.woman()

                    #preference list assertions
                    mprefwprime = self.men[m].index(wprime)
                    mpref = self.men[m].index(w)
                    wprefm = self.women[wprime].index(m)
                    wprimepref = self.women[wprime].index(mprime)

                    if mprefwprime < mpref and wprefm < wprimepref:
                        unstabletick = 1
                        break

                if unstabletick == 1:
                    break

            if unstabletick == 0:
                self.stable_matchings.append(pairlist)

            pairlist = list()
            unstabletick = 0
        
        return self.stable_matchings
    '''