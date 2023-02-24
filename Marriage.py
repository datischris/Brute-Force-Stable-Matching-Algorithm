class Marriage:

    def __init__(self, male_val, female_val):
        self.m = male_val
        self.w = female_val

    def set_man(self, male_val):
        self.m = male_val

    def set_woman(self, female_val):
        self.w = female_val

    def man(self):
        return self.m
    def woman(self):
        return self.w

    def equals(self, marriage):
        return (marriage.man() == self.m) and (marriage.woman() == self.w)

    def __str__(self):
        return "(" + str(self.m) + ", " + str(self.w) + ")"

    __repr__ = __str__

    def __lt__(self, other):
        return self.w < other.woman()

    def __eq__(self, other):
        return self.w == other.woman() and self.m == other.man()
