import utility
import heapq

class Fuzzy:
    def __init__(self):
        self.fuzzy = dict()

    def load(self,year):
        name = "processed\\fuzzy_" + str(year) + ".txt"
        with open(name,"r",encoding="ISO8859-1") as f:
            for line in f:
                tmp = line.split()
                a = tmp[0]
                b = tmp[1:]
                self.fuzzy[a] = b
        
    def get_fuzzy(self,word,max_len=15):
        sound = utility.soundex(word)
        if sound in self.fuzzy:
            ans = self.fuzzy[sound]

            fuzzy = []
            for obj in ans:
                if obj != word and obj.isalpha() and len(obj) <= 10:
                    fuzzy.append(obj)
            rank = []
            for obj in fuzzy:
                r = utility.edit_dist(obj,word)
                rank.append(r)

            ans = []
            data = heapq.nsmallest(max_len, enumerate(rank), key=lambda x:x[1])
            idx, val = zip(*data)
            for obj in idx:
                ans.append(fuzzy[obj])
            return ans

        return []

##a = Fuzzy()
##a.load(2013)
##b = a.get_fuzzy("read")
##print(b)
##b = a.get_fuzzy("root")
##print(b)
