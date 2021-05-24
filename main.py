import time
import Search

def test():
    t = time.time()
    a = Search.Search()
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
    f = a.f_search("rooot")
    print(len(f))
    print(f[0:10])
    print(time.time() - t)

    #lst = list(range(5000))
    lst = lc
    d = a.filter_docid("word",c,"ubuntu","good",10)
    print(len(d))
    print(d)
    print(time.time() - t)

test()
