def textQueriesRevised(sentences, queries):
    # 1. build the hash map
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
