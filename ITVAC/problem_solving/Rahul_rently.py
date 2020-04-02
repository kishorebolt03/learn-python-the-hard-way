from collections import Counter as cs
def textQueries(sentences, queries):
    if(1<=len(sentences)<=10*4 and 1<=len(queries)<=10*4):
        temp=' '.join(sentences).split()
        for i in queries:
            t=[]
            if(set(i.split()).issubset(set(temp))):
                for j in sentences:
                    if(set(i.split()).issubset(set(j.split()))):
                        a=cs(j.split())
                        z=[a[i] for i in i.split()]
                        t.extend(str(sentences.index(j))*min(z))
                        #t.append(str(sentences.index(j)))
                if(t!=[]): print(' '.join(t))
                else: print(-1)
            else:
                print(-1)
        del(t,sentences,queries,temp)
    else:
        print(-1)
if _name_ == '_main_':
    sentences_count = int(input().strip())

    sentences = []

    for _ in range(sentences_count):
        sentences_item = input()
        sentences.append(sentences_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    textQueries(sentences, queries)
'''
3
bob and alice like to text
bob does not like
Alice like
3
bob alice
like
alice
'''
