import soundex

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
        
    def get_fuzzy(self,word):
        sound = soundex.soundex(word)
        if sound in self.fuzzy:
            ans = self.fuzzy[sound][::]
            if word in ans:
                ans.remove(word)
            return ans
        return []

##a = Fuzzy()
##a.load(2013)
##b = a.get_fuzzy("read")
##print(b)
##b = a.get_fuzzy("root")
##print(b)
