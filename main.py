import time
import Search

def test():
    t = time.time()
    a = Search.Search()
    a.load(2013)
    print(time.time() - t)
    print(len(a.file_list))
    la = a.get_docid("removed")   #获取含有removed的docid列表la
    print(len(la))
    lb = a.get_docid("root")   #获取含有root的docid列表lb
    print(len(lb))
    lc = a.b_search("and",la,lb)   #将la和lb取交集，得到同时含有removed和root的列表lc
    print(lc[0:10])
    print(len(lc))
    print(time.time() - t)
    b = a.output_by_date(lc)   #将docid转化为txt文件路径，并按照时间排序，默认15个，生成文件路径列表b
    print(b)
    c = a.output_by_size(lc)   #将docid转换为txt文件路径，并按照大小排列，默认15个，生成文件路径列表c
    print(c)
    print(time.time() - t)
    print(a.output_window(c,"removed","without","be")[0:5])    #返c中的摘要信息
    print(time.time() - t)
    f = a.f_search("rooot")    #返回与rooot发音相近且编辑距离最小的单词列表，默认15个
    print(f)
    print(time.time() - t)

    lst = lc
    d = a.filter_docid("word",c,"ubuntu","good",10)    #提取c中同时含有ubuntu和good且两单词距离不超过10的文档
    print(len(d))
    print(d)
    print(time.time() - t)

test()
