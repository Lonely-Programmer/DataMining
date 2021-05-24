import re

class Proximity:
    def __init__(self):
        pass

    def load_word(self,file):
        ans = []
        name = file
        with open(name,"r",encoding="ISO8859-1") as f:
            for line in f:
                line = line.lower()
                tmp = line.split()
                for j in range(len(tmp)):
                    if len(tmp[j]) > 0 and tmp[j][0] in "<[":
                        continue
                    for s in "()":
                        tmp[j] = tmp[j].replace(s,"")
                    for s in " ,.:?!\'\n":
                        tmp[j] = tmp[j].strip(s)
                for j in range(len(tmp)):
                    word = tmp[j]
                    ans.append(word)
        return ans

    def load_para(self,file):
        ans = []
        name = file
        with open(name,"r",encoding="ISO8859-1") as f:
            for line in f:
                ans.append([])
                line = line.lower()
                tmp = line.split()
                for j in range(len(tmp)):
                    if len(tmp[j]) > 0 and tmp[j][0] in "<[":
                        continue
                    for s in "()":
                        tmp[j] = tmp[j].replace(s,"")
                    for s in " ,.:?!\'\n":
                        tmp[j] = tmp[j].strip(s)
                for j in range(len(tmp)):
                    word = tmp[j]
                    ans[-1].append(word)
        return ans

    def load_bracket(self,file):
        ans = []
        name = file
        with open(name,"r",encoding="ISO8859-1") as f:
            for line in f:
                stack = False
                ans.append([])
                line = line.lower()
                brackets = re.findall(r'[(](.*?)[)]', line)
                for obj in brackets:
                    tmp = obj.split()
                    for j in range(len(tmp)):
                        if len(tmp[j]) > 0 and tmp[j][0] in "<[":
                            continue
                        for s in " ,.:?!\'\n":
                            tmp[j] = tmp[j].strip(s)
                    for j in range(len(tmp)):
                        word = tmp[j]
                        ans[-1].append(word)
        return ans

    def word_proximity(self,file,w1,w2,d):
        data = self.load_word(file)
        p1 = -1
        p2 = -1
        min_d = 100000
        for i in range(len(data)):
            if data[i] == w1:
                p1 = i
            if data[i] == w2:
                p2 = i
            if p1 != -1 and p2 != -1:
                min_d = min(min_d,abs(p1 - p2))
        if p1 != -1 and p2 != -1 and min_d <= d:
            return True
        return False

    def para_proximity(self,file,w1,w2):
        data = self.load_para(file)
        for obj in data:
            if w1 in obj and w2 in obj:
                return True
        return False

    def bracket_proximity(self,file,w1,w2):
        data = self.load_bracket(file)
        for obj in data:
            if w1 in obj and w2 in obj:
                return True
        return False


##a = Proximity()
##print(a.word_proximity("raw\\2014\\01\\04\\#ubuntu.txt","graphics","revert",5))
##print(a.para_proximity("raw\\2014\\01\\04\\#ubuntu.txt","graphics","revert"))
##print(a.bracket_proximity("raw\\2014\\01\\04\\#ubuntu.txt","around","2010"))

    
