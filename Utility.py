import re
from PreferenceLists import PreferenceLists

class Utility:

    def read_file(self, input_file):
            f = open(input_file, 'r')
            num = int(f.readline())
            women_preferences = {}
            for w in range(1, num + 1):
                preferences = []
                line = re.split('\W+', f.readline())
                for x in range(0, num):
                    preferences.append(int(line[x]))
                women_preferences[w] = preferences

            men_preferences = {}

            for m in range(1, num + 1):
                preferences = []
                line = re.split('\W+', f.readline())
                for x in range(0, num):
                    preferences.append(int(line[x]))
                men_preferences[m] = preferences
            return PreferenceLists(women_preferences, men_preferences)
