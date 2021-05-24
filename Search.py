import Boolean
import Fuzzy
import Proximity
import time
import os
import heapq

class Search:
    def __init__(self):
        self.proximity = Proximity.Proximity()

    def load(self,year):
        self.boolean = Boolean.Boolean()
        self.boolean.load(year)
        self.fuzzy = Fuzzy.Fuzzy()
        self.fuzzy.load(year)
        self.file_list = []
        with open("processed\\files_" + str(year) + ".txt","r") as f:
            for line in f:
                self.file_list.append(line.strip("\n"))

    def get_docid(self,word):
        return self.boolean.get_docid(word)

    def b_search(self,logic,listA,listB):
        if logic == "and":
            return self.boolean.get_docid_and(listA,listB)
        elif logic == "or":
            return self.boolean.get_docid_or(listA,listB)
        elif logic == "and_not":
            return self.boolean.get_docid_not(listA,listB)

    def f_search(self,word):
        fuzzy = self.fuzzy.get_fuzzy(word)
        original = self.boolean.get_docid(word)
        rank = []
        for obj in fuzzy:
            r = self.boolean.get_docid_and(original,self.boolean.get_docid(obj))
            rank.append(r)

        sorted_rank = sorted(enumerate(rank),key=lambda x:x[1])
        idx = [i[0] for i in sorted_rank]
        fuzzy = [fuzzy[i] for i in idx]
        return fuzzy[::-1]

    def filter_docid(self,logic,lst,w1,w2,d = None):
        ans = []
        if logic == "word":
            for obj in lst:
                file = obj
                flag = self.proximity.word_proximity(file,w1,w2,d)
                if flag:
                    ans.append(obj)
        elif logic == "para":
            for obj in lst:
                file = obj
                flag = self.proximity.para_proximity(file,w1,w2)
                if flag:
                    ans.append(obj)
        elif logic == "bracket":
            for obj in lst:
                file = obj
                flag = self.proximity.bracket_proximity(file,w1,w2)
                if flag:
                    ans.append(obj)
        return ans

    def output_by_date(self,docid,max_len=15):
        ans = []
        if len(docid) < max_len:
            tmp = docid[::-1]
        else:
            tmp = docid[-1:-max_len-1:-1]
        for i in range(len(tmp)):
            ans.append(self.file_list[tmp[i]])
        return ans

    def output_by_size(self,docid,max_len=15):
        ans = []
        size = []
        max_len = min(max_len,len(docid))
        for obj in docid:
            size.append(os.path.getsize(self.file_list[obj]))
        idx = list(map(size.index, heapq.nlargest(max_len,size)))
        for obj in idx:
            ans.append(self.file_list[docid[obj]])
        return ans

t = time.time()
a = Search()
a.load(2015)
print(time.time() - t)
print(len(a.file_list))
la = a.get_docid("removed")
print(len(la))
lb = a.get_docid("root")
print(len(lb))
lc = a.b_search("and",la,lb)
print(lc[0:10])
print(len(lc))
print(time.time() - t)
b = a.output_by_date(lc)
print(b)
c = a.output_by_size(lc)
print(c)
print(time.time() - t)
print(len(a.f_search("root")))
print(time.time() - t)

#lst = list(range(5000))
lst = lc
d = a.filter_docid("word",c,"ubuntu","good",10)
print(len(d))
print(d)
print(time.time() - t)