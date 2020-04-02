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
'''
import re

from collections import Counter as C
import time

def textQueries(sentences, queries):
    # 1. build the hash map
    start=time.time()
    word_map = {}
    for query in queries:
        for query_word in query.split():
            for i, sentence in enumerate(sentences):
                if query_word in sentence:
                    word_map.setdefault(query_word, []).append(i)
    for query in queries:
        # 2. look up in the hash map
        final_set = set()
        for word in query.split():
            if not final_set:
                final_set = set(word_map.get(word, []))
            else:
                final_set = final_set.intersection(word_map.get(word, []))
            if not final_set:
                break
        # 3. print the indices
        if final_set:
            print(' '.join(str(i) for i in sorted(final_set)))
            # or
            #print(*sorted(final_set), sep=' ')
        else:
            print(-1)
    end=time.time()
    print("time taken ===========",end-start)
    return 1
'''
'''
import time
def textQueries(sentences,queries):
    start=time.time()
    dicT={}
    for ind,i in enumerate(sentences):
        for j in i.split():
            if j not in dicT.keys():
                dicT[j]=[str(sentences[ind])]
            else:
                dicT[j]+=[str(sentences[ind])]
    for i in queries:
        z={}
        for j in i.split():
            if z!={}:
                z=z.intersection(*map(set,dicT[j]))
            else:
                z=set(dicT[j])
        print(" ".join(sorted(list(z))))
    #
    end=time.time()
    print("time taken ===========",end-start)
    return 1

'''

from collections import defaultdict
import time
def textQueries(sentences, queries):
    word_indices = defaultdict(set)
    for i, s in enumerate(sentences):
        for w in s.split():
            word_indices[w].add(i)
    n=[]
    for i in [[str(i) for i in sorted(set.intersection(*[word_indices[w] for w in q.split()]))] for q in queries]:
        n.append(" ".join(i))
    return n


if __name__ == '__main__':
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
    start=time.time()
    print("\n".join(textQueries(sentences, queries)))
    print("",time.time()-start)
