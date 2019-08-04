dataset = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],  # [0,0,1,1,1......]
           # ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
           # ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
           # ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
           # ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
           ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
vocabSet = set([])
for document in dataset:
    vocabSet = vocabSet | set(document)  # union of the two sets
print(list(vocabSet))
print(len(list(vocabSet)))
print([0]*12)
