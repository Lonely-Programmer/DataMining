import bisect

class Boolean:
    def __init__(self):
        self.word = []
        self.docid = []

    def binary_search_bisect(self,lst,val):
        i = bisect.bisect_left(lst, val)
        if i != len(lst) and lst[i] == val:
            return i
        return -1

    def load(self,year):
        name = "processed\\posting_" + str(year) + ".txt"
        with open(name,"r",encoding="ISO8859-1") as f:
            for line in f:
                tmp = line.split()
                a = tmp[0]
                b = []
                for obj in tmp[1:]:
                    b.append(int(obj))
                self.word.append(a)
                self.docid.append(b)

    def get_docid(self,word):
        idx = self.binary_search_bisect(self.word,word)
        if idx == -1:
            return []
        return self.docid[idx]

    def get_docid_and(self,listA,listB):
        ans = []
        pa = 0
        pb = 0
        na = len(listA)
        nb = len(listB)
        while pa < na and pb < nb:
            if listA[pa] == listB[pb]:
                ans.append(listA[pa])
                pa += 1
                pb += 1
            elif listA[pa] < listB[pb]:
                pa += 1
            else:
                pb += 1
        return ans

    def get_docid_and_not(self,listA,listB):
        ans = []
        pa = 0
        pb = 0
        na = len(listA)
        nb = len(listB)
        while pa < na:
            while pb < nb and listB[pb] < listA[pa]:
                pb += 1
            if pb == nb:
                break
            if listA[pa] != listB[pb]:
                ans.append(listA[pa])
            pa += 1
        
        ans += listA[pa:]
        return ans

    def get_docid_or(self,listA,listB):
        ans = []
        pa = 0
        pb = 0
        na = len(listA)
        nb = len(listB)
        while pa < na and pb < nb:
            if listA[pa] == listB[pb]:
                ans.append(listA[pa])
                pa += 1
                pb += 1
            elif listA[pa] < listB[pb]:
                ans.append(listA[pa])
                pa += 1
            else:
                ans.append(listB[pb])
                pb += 1
        
        ans += listA[pa:]
        ans += listB[pb:]
        return ans


##a = Boolean()
##a.load(2013)
##b = a.get_docid("removed")
##print(b)
##b = a.get_docid_not("removed")
##print(b)
