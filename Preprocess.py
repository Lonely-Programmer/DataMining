import os
import soundex
import time

class Preprocess:
    def __init__(self):
        #self.doc_name = ["raw\\2013\\09\\07\\#kubuntu-devel.txt"]
        self.doc_name = []
        self.posting = dict()
        self.fuzzy = dict()

    def gen_file_list(self,file):
        self.doc_name = []
        self.posting = dict()
        self.fuzzy = dict()
        for root, dirs, files in os.walk(file):
            for f in files:
                self.doc_name.append(os.path.join(root, f))
                if len(self.doc_name) % 10000 == 0:
                    print(os.path.join(root, f))

    def gen_inverted_index(self):
        for i in range(len(self.doc_name)):
            name = self.doc_name[i]
            try:
                with open(name,"r",encoding="ISO8859-1") as f:
                    if i % 1000 == 0:
                        print(i,name)
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
                            if word not in self.posting:
                                self.posting[word] = [i]
                            elif self.posting[word][-1] != i:
                                self.posting[word].append(i)
            except:
                pass

    def gen_fuzzy_index(self):
        cnt = 0
        for key in self.posting.keys():
            if cnt % 1000000 == 0:
                print(cnt)
            cnt += 1
            sound = soundex.soundex(key)
            if len(sound) == 0:
                continue
            if sound not in self.fuzzy:
                self.fuzzy[sound] = [key]
            else:
                self.fuzzy[sound].append(key)

    def output_file_list(self,year):
        name = "processed\\files_" + str(year) + ".txt"
        with open(name,"w",encoding="ISO8859-1") as f:
            for obj in self.doc_name:
                f.write(obj + "\n")

    def output_inverted_index(self,year):
        key = self.posting.keys()
        key = sorted(key)
        name = "processed\\posting_" + str(year) + ".txt"
        
        with open(name,"w",encoding="ISO8859-1") as f:
            for obj in key:
                if len(obj) == 0:
                    continue
                line = obj
                for docid in self.posting[obj]:
                    line += " " + str(docid)
                f.write(line + "\n")

    def output_fuzzy_index(self,year):
        key = self.fuzzy.keys()
        #key = sorted(key)
        name = "processed\\fuzzy_" + str(year) + ".txt"
        
        with open(name,"w",encoding="ISO8859-1") as f:
            for obj in key:
                if len(obj) == 0:
                    continue
                line = obj
                for sound in self.fuzzy[obj]:
                    line += " " + str(sound)
                f.write(line + "\n")

def main():
    t = time.time()
    name = 2015
    a = Preprocess()
    print("Parsing...")
    a.gen_file_list("raw\\")
    print("Creating index...")
    a.gen_inverted_index()
    print("Outputting file list...")
    a.output_file_list(name)
    print("Outputting index...")
    a.output_inverted_index(name)
    print("Creating fuzzy index...")
    a.gen_fuzzy_index()
    print("Outputting fuzzy index...")
    a.output_fuzzy_index(name)
    print(time.time() - t)

main()

