A=[100,200,99,98,97,2,3,5,4,1,6,88]
sequences={}
for a in A:
    if sequences.get(a): continue
    sequences[a] = 1
    if sequences.get(a + 1):
        sequences[a] += sequences[a + 1]
    while sequences.get(a - 1):
        sequences[a - 1] = 1 + sequences[a]
        a -= 1

print(max(sequences.values()))
