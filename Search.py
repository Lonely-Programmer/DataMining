from typing import ClassVar
import Boolean
import Fuzzy
import Proximity
import time
import os
import heapq
import re
import zList
import utility
    
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
        zList.zList.full = len(self.file_list)
   
    def get_length(self):
        return self.boolean.get_length()
    def get_docid(self,word):   #返回单词word的docid列表
        return self.boolean.get_docid(word)

    def b_search(self,logic,listA,listB):   #对两个docid列表进行运算
        if logic == "and":   #交集，listA & listB
            return self.boolean.get_docid_and(listA,listB)
        elif logic == "or":   #并集，listA | list B
            return self.boolean.get_docid_or(listA,listB)
        elif logic == "and_not":   #差集，listA \ listB
            return self.boolean.get_docid_not(listA,listB)

    def f_search(self,word,max_len=15):    #返回单词word的拼写建议，最多max_len个
        fuzzy = self.fuzzy.get_fuzzy(word,max_len)
        return fuzzy
    def output_window(self,lst,w1,w2 = None,must = None):    #给定文件路径列表和关键词w1、w2（可选），必须包含的词must（可选），返回摘要信息（window）
        ans = []
        for obj in lst:
            w = utility.get_window(obj,w1,w2,must)
            ans.append(w)
        return ans
    def filter_docid(self,logic,lst,w1,w2,d = None):   #过滤文件列表lst，只保留符合条件的文件路径。
        ans = []
        if logic == "word":   #单词w1和w2的距离至多为d
            for obj in lst:
                file = obj
                flag = self.proximity.word_proximity(file,w1,w2,d)
                if flag:
                    ans.append(obj)
        elif logic == "para":   #单词w1和w2必须在同一段（d参数无效）
            for obj in lst:
                file = obj
                flag = self.proximity.para_proximity(file,w1,w2)
                if flag:
                    ans.append(obj)
        elif logic == "bracket":   #单词w1和w2必须在同一个括号内（d参数无效）
            for obj in lst:
                file = obj
                flag = self.proximity.bracket_proximity(file,w1,w2)
                if flag:
                    ans.append(obj)
        else:
            return lst
        return ans

    def output_by_date(self,docid,max_len=30):   #输入：docid列表，长度限制max_len   输出：最新的max_len个docid对应的文件路径
        ans = []
        if len(docid) < max_len:
            tmp = docid[::-1]
        else:
            tmp = docid[-1:-max_len-1:-1]
        for i in range(len(tmp)):
            ans.append(self.file_list[tmp[i]])
        return ans

    def output_by_size(self,docid,max_len=30):  #输入：docid列表，长度限制max_len   输出：最大的max_len个docid对应的文件路径
        ans = []
        size = []
        max_len = min(max_len,len(docid))
        if len(docid) > 5 * max_len:
            import random
            random.seed(0)
            docid = random.sample(docid,5 * max_len)
        for obj in docid:
            size.append(os.path.getsize(self.file_list[obj]))
        idx = list(map(size.index, heapq.nlargest(max_len,size)))
        for obj in idx:
            ans.append(self.file_list[docid[obj]])
        return ans
    #def abs_search(self,docids,ws):
     #   if len(ws)==1:

    def normal_search(self,query,sort=0):
        flag = False
        logic = "None"
        distance = 0
        zlists = []
        suggest = []
        valid = []
        q_l = query.split("/")
        tokens = utility.divide(q_l[0])
        index = 0
        if len(q_l)==2:
            if(q_l[1].isdigit()):
                logic = "word"
                distance = int(q_l[1])
            elif(q_l[1]=="p"):
                logic = "para"
            elif(q_l[1]=="b"):
                logic = "bracket"
        for i in range(len(tokens)):
            if tokens[i].isalpha():
                t = self.get_docid(tokens[i])
                zlists.append(zList.zList(t))
                if len(t)==0:
                    flag = True
                    sug = self.f_search(tokens[i])[0]
                    suggest.append(sug)
                else:
                    valid.append(tokens[i])
                    suggest.append(tokens[i])
                tokens[i]="zlists["+str(index)+"]"
                index+=1
            else:
                suggest.append(tokens[i])
                #zlists.append(tokens[i])
        command = utility.combine(tokens)
        print(command)
        docids = eval(command).list
        if(sort==0):
            docids = self.output_by_date(docids)
        else:
            docids = self.output_by_size(docids)
        abs = []
        if(len(valid)>=2):
            if(logic!="None"):
                docids = self.filter_docid(logic,docids,valid[0],valid[1],distance)
            abs = self.output_window(docids,valid[0],valid[1])
        elif(len(valid)==1):
            abs = self.output_window(docids,valid[0])
        docmsgs = [(docids[j],abs[j]) for j in range(len(docids))]
        if(flag):
            return (docmsgs,"Do you mean: "+utility.combine(suggest)+" ?\n")
        else:
            return (docmsgs,"")
                


        
    

                

        
